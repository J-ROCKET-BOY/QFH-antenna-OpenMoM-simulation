#! /usr/bin/env python3
import numpy as np
import os
from operator import sub
import math

def generateModel(parameter):
        #model setting reading
        modelName = parameter[0]
        baseModel = parameter[1]

        modelData = ""

        print("------------ generating openMoM model ------------")
        print("modelName : " + modelName)

        modelFolder = "./" + modelName

        if(modelName == ""):
            print("No model name")
            print("------------ generating error ------------")
            return ""
        if(os.path.exists(modelFolder)):
            print("modelName : " + modelName + " exists already")
#            print("------------ generating error ------------")
#            return ""
        else:
            os.mkdir(modelFolder)

        with open(modelName + "/" + modelName + ".omm", mode="w") as modelFile:

            diaX = float(parameter[2])
            diaY = float(parameter[3])
            heiX = float(parameter[4])
            heiY = float(parameter[5])
            heiT = float(parameter[6])
            diaW = float(parameter[7])
            divN = int(parameter[8])

            #header
            modelData += "OpenMOM 1 7\n"
            #title
            modelData += "title = " + modelName + "\n"

            #feed point
            modelData += "geometry = 1 1 {0:.4f} {1:.4f} {1:.4f} {0:.4f} {2:.4f} {2:.4f} 1\n".format(-3*diaW/math.sqrt(2)/2,3*diaW/math.sqrt(2)/2,heiT)
            modelData += "feed = 1 0\n"
            modelData += "name = feed point\n"

            #top X wire
            modelData += "geometry = 1 1 {0:.4f} {1:.4f} {2:.4f} 0 {3:.4f} {3:.4f} 1\n".format(3*diaW/math.sqrt(2)/2,math.sqrt(2)*3*diaW/2,-3*diaW/math.sqrt(2)/2,heiT)
            modelData += "name = top horizontal X1-0\n"

            modelData += "geometry = 1 1 {0:.4f} {1:.4f} 0 0 {2:.4f} {2:.4f} {3:d}\n".format(math.sqrt(2)*3*diaW/2, diaX/2, heiT, int( (diaX/2-math.sqrt(2)*3*diaW/2)/(3/2*diaW) ))
            modelData += "name = top horizontal X1-1\n"

            modelData += "geometry = 1 1 {0:.4f} {1:.4f} {2:.4f} 0 {3:.4f} {3:.4f} 1\n".format(-3*diaW/math.sqrt(2)/2,-math.sqrt(2)*3*diaW/2,3*diaW/math.sqrt(2)/2,heiT)
            modelData += "name = top horizontal X2-0\n"

            modelData += "geometry = 1 1 {0:.4f} {1:.4f} 0 0 {2:.4f} {2:.4f} {3:d}\n".format(-math.sqrt(2)*3*diaW/2,-diaX/2,heiT,int( (diaX/2-math.sqrt(2)*3*diaW/2)/(3/2*diaW) ))
            modelData += "name = top horizontal X2-1\n"


            #top Y wire
            modelData += "geometry = 1 1 {0:.4f} 0 {1:.4f} {2:.4f} {3:.4f} {3:.4f} 1\n".format(-3*diaW/math.sqrt(2)/2,3*diaW/math.sqrt(2)/2,math.sqrt(2)*3*diaW/2,heiT)
            modelData += "name = top horizontal Y1-0\n"

            modelData += "geometry = 1 1 0 0 {0:.4f} {1:.4f} {2:.4f} {2:.4f} {3:d}\n".format(math.sqrt(2)*3*diaW/2,diaY/2,heiT,int( (diaY/2-math.sqrt(2)*3*diaW/2)/(3/2*diaW) ))
            modelData += "name = top horizontal Y1-1\n"

            modelData += "geometry = 1 1 {0:.4f} 0 {1:.4f} {2:.4f} {3:.4f} {3:.4f} 1\n".format(3*diaW/math.sqrt(2)/2,-3*diaW/math.sqrt(2)/2,-math.sqrt(2)*3*diaW/2,heiT)
            modelData += "name = top horizontal Y2-0\n"

            modelData += "geometry = 1 1 0 0 {0:.4f} {1:.4f} {2:.4f} {2:.4f} {3:d}\n".format(-math.sqrt(2)*3*diaW/2,-diaY/2,heiT,int( (diaY/2-math.sqrt(2)*3*diaW/2)/(3/2*diaW) ))
            modelData += "name = top horizontal Y2-1\n"


            for i in range(divN):

                #X helical
                X1 = diaX/2*math.cos(math.pi*i/divN)
                Y1 = diaX/2*math.sin(math.pi*i/divN)
                Z1 = heiT-heiX*i/divN
                X2 = diaX/2*math.cos(math.pi*(i+1)/divN)
                Y2 = diaX/2*math.sin(math.pi*(i+1)/divN)
                Z2 = heiT-heiX*(i+1)/divN
                L  = math.sqrt(math.pow((X2-X1),2)+math.pow((Y2-Y1),2)+math.pow((Z2-Z1),2))
                N  = int(L/(3/2*diaW))

                #+X -> -X helical
                modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(X1,Y1,Z1,X2,Y2,Z2,N)
                modelData += "name = helical +X->-X {}\n".format(i)
                
                #-X -> +X helical
                modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(-X1,-Y1,Z1,-X2,-Y2,Z2,N)
                modelData += "name = helical -X->+X {}\n".format(i)

                #Y helical
                X1 = -diaY/2*math.sin(math.pi*i/divN)
                Y1 =  diaY/2*math.cos(math.pi*i/divN)
                Z1 = heiT-heiY*i/divN
                X2 = -diaY/2*math.sin(math.pi*(i+1)/divN)
                Y2 =  diaY/2*math.cos(math.pi*(i+1)/divN)
                Z2 = heiT-heiY*(i+1)/divN
                L  = math.sqrt(math.pow((X2-X1),2)+math.pow((Y2-Y1),2)+math.pow((Z2-Z1),2))
                N  = int(L/(3/2*diaW))

                #+Y -> -Y helical
                modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(X1,Y1,Z1,X2,Y2,Z2,N)
                modelData += "name = helical +Y->-Y {}\n".format(i)
                
                #-Y -> +Y helical
                modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(-X1,-Y1,Z1,-X2,-Y2,Z2,N)
                modelData += "name = helical -Y->+Y {}\n".format(i)

            #X bottom
            X1 =  diaX/2
            Y1 = 0
            Z1 = heiT-heiX
            X2 = -diaX/2
            Y2 = 0
            Z2 = heiT-heiX
            L  = math.sqrt(math.pow((X2-X1),2)+math.pow((Y2-Y1),2)+math.pow((Z2-Z1),2))
            N  = int(L/(3/2*diaW))
            modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(-X1,-Y1,Z1,-X2,-Y2,Z2,N)
            modelData += "name = X bottom\n"

            #Y bottom
            X1 = 0
            Y1 =  diaY/2
            Z1 = heiT-heiY
            X2 = 0
            Y2 = -diaY/2
            Z2 = heiT-heiY
            L  = math.sqrt(math.pow((X2-X1),2)+math.pow((Y2-Y1),2)+math.pow((Z2-Z1),2))
            N  = int(L/(3/2*diaW))
            modelData += "geometry = 1 1 {0:.4f} {3:.4f} {1:.4f} {4:.4f} {2:.4f} {5:.4f} {6}\n".format(-X1,-Y1,Z1,-X2,-Y2,Z2,N)
            modelData += "name = Y bottom\n".format(i)

            #other setting from baseModel
            if(not(".omm" in baseModel)):
                baseModel += ".omm"
            with open(baseModel, mode = "r") as baseModelFile:
                baseModelData = baseModelFile.read()
                #Extract the back from the boundary condition and copy it.
                modelData += baseModelData[baseModelData.find("frequency"):]
#                print(baseModelData)


            modelFile.write(modelData)
            modelFile.close()
            
        print("------------ finish generating ------------")
