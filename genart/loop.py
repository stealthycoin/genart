import pygame

def iterate_on_model(model, max_iter=1000):
    iters = 0
    while iters < max_iter:
        model.update()
        iters += 1

def start(model, w=500, h=300):
    z = w,h
    display = pygame.display
    screen = display.set_mode(z)
    model.render(screen)
    pygame.display.flip()
    
    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
    finally:
        pygame.quit()
            
