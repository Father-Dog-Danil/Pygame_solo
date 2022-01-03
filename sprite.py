import pygame
pygame.init()

mushroom_enemy_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED8.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED9.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED10.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED11.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED12.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED13.png')]

cockroach_walk_up = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_WALK1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_WALK2.png')]

cockroach_sniffs_up = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_UP_SNIFFS7.png')]

cockroach_walk_down = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_WALK1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_WALK2.png')]

cockroach_sniffs_down = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/COCKROACH_DOWN_SNIFFS7.png')]


heart_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART4.png')]

padlock = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PADLOCK.png')
bg_house_shadow = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE2.png')
key_sprite = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/KEY.png')

passage_list = [pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR1.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR2.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR3.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR4.png')]

npc_list1 = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC6.png')]

npc_anime_list1 = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME8.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME9.png')]

torch_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH4.png')]

ball_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_8.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_9.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_10.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_11.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_12.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_13.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_14.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_15.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_16.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_17.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_18.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_19.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_20.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/ball_21.png')]

portal_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL1.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL2.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL3.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL4.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL5.png').convert()]

portal_tp_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_1.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_2.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_3.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_4.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_5.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_6.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_TP_7.png').convert()]

portal_list_anime = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME1.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME2.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME3.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME4.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME5.png').convert()]

hero_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus3.png')]

hero_walk_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_walk1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_walk2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_walk3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_walk4.png')]

log_enemy_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D1.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D2.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D3.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D4.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D5.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_Y_D6.png').convert()]
log_enemy_list_y = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R1.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R2.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R3.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R4.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R5.png').convert(),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/LOG_X_R6.png').convert()]
bg = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/MAP2.png').convert()
bg_house = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE1.png').convert()
bg_dung = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE3.png').convert()
bg_dung_p = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE4.png').convert()