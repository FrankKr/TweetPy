# Take webcam image

import pygame
import pygame.camera

class CamCapt():
    
    def __init__(self, outputdir='.'):
        pygame.camera.init()
        camports = self.find_cam_ports()
        self.camports = camports
        self.camport = self.camports[0]
        self.outputdir = outputdir
    
    def find_cam_ports(self):
        """Find list of working camera ports"""
        # find camera
        camlist = pygame.camera.list_cameras()
        if len(camlist) < 1:
            print('No camera found!')
            return None

        workingcams = []
        for camport in camlist:
            try:
                cam = pygame.camera.Camera(camport,(640,480),"RGB")
                cam.start()
                img = cam.get_image()
                cam.stop()
                pygame.image.save(img,"/tmp/tmp.jpg")
                #print('Image stored for port', camport)
                workingcams.append(camport)
                if len(workingcams) == 1:
                    self.cam = cam
            except Exception as e:
                #print('Did not work for port:', camport)
                pass
        return workingcams
    
    
    def take_image(self, name='img.jpg'):
        """Take image, store to default outputdir"""
        #cam = pygame.camera.Camera(self.camport,(640,480))
        self.cam.start()
        img = self.cam.get_image()
        pygame.image.save(img, name)
        self.cam.stop()
        print('Stored image to', name)

if __name__=='__main__':
    ccpt = CamCapt()
    ccpt.take_image()


