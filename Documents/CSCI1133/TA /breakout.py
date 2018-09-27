import pygame
import sys
import random

def main():

    width = 600
    height = 600
    colorlist = [(255,0,0), (0,255,0), (0,0,255)]
    color = colorlist[0]
    fps = 60
    d = pygame.display.set_mode((width, height))
    c = pygame.time.Clock()

    bricklist =[]
    brick_image = pygame.image.load("Lab15_Images/bricks/brickGold.jpg")
    for i in range(2):
        bricklist.append([])
        for j in range(10):
            brick_rect = brick_image.get_rect()
            brick_rect.left = (j * 60)
            brick_rect.top = i*20
            bricklist[i].append(Brick(brick_image, brick_rect, 2 - i))
    
    pygame.display.set_caption("Evan's breakout game")


    block_im = pygame.image.load("Lab15_Images/blocks/blockRainbow.jpg")
    block_r = block_im.get_rect()
    block_r = block_r.move([50,50])
    direct_block = [2,2]

    paddle_im = pygame.image.load("Lab15_Images/paddles/paddleMaroonAndGold.jpg")
    paddle_r = paddle_im.get_rect()
    paddle_r.bottom = height - 20


    pygame.key.set_repeat(10,10)


    while True:
        d.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    d.fill(color)

                if event.key == pygame.K_LEFT:
                    if(paddle_r.left > 4):
                        paddle_r.left -= 4
                if event.key == pygame.K_RIGHT:
                    if(paddle_r.right < width - 4):
                        paddle_r.right += 4
        
        hitany = False
        for l in bricklist:
            for b in l:
                hitthis = hitbrick(block_r, b, direct_block)
                hitany = hitany or hitthis
                if(hitthis == True):
                    b.hits -= 1
                    if b.hits == 0:
                        l.remove(b)
                else:
                    d.blit(b.image,b.rect)
        if hitany:
            direct_block[1] = direct_block[1] * -1
            
        block_r = block_r.move(direct_block)
        direct_block = hitswall(block_r, direct_block, width, height)
        direct_block = hitspaddle(paddle_r, block_r, direct_block)
        
        
        
        
        c.tick(fps)
        d.blit(block_im, block_r)
        d.blit(paddle_im, paddle_r)
        pygame.display.flip()

        
  


def hitswall(rect, speed, w, h):
    finspeed = [speed[0], speed[1]]
    if rect.left < 0 or rect.right > w:
         finspeed[0] *= (-1)
    if rect.top < 0:
        finspeed[1] *= -1
    if rect.bottom > h:
        sys.exit()
    return finspeed

def hitspaddle(paddle, block, blockspeed):
    if paddle.colliderect(block):
        return [blockspeed[0], -1 * blockspeed[1]]
    else :
        return blockspeed


class Brick:
    def __init__(self, image, rect, hits = 1):
        self.image = image
        self.rect = rect
        self.hits = hits

def hitbrick(block, brick, speed):
    if brick.rect.colliderect(block):
        return True
    else :
        return False


if __name__ == "__main__" :
    main()
