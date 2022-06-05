import math
import random
import pygame

'''子弹类'''
#一级箭塔子弹
class bullet1(pygame.sprite.Sprite):
	def __init__(self,pos_x,pos_y,angle):
		pygame.sprite.Sprite.__init__(self)
		#载入子弹的图片
		image0 = pygame.image.load('./resource/bullets/法1.png').convert_alpha()
		self.image1= pygame.transform.scale(image0,(24,24))
		#self.image=pygame.transform.rotate(self.image1,math.pi/3)
		#self.image=pygame.transform.rotate(self.image1,math.radians(45))

		self.image2 = pygame.transform.rotate(self.image1,45)
		self.image = pygame.transform.rotate(self.image2,-180*angle/math.pi)
		self.rect = self.image.get_rect()
		self.position = pos_x,pos_y
		self.begin_pos=pos_x,pos_y
	    #self.begin_pos = self.position
		self.rect.left, self.rect.top = self.position
		# 与水平向左的直线所成的夹角, 顺时针为正
		self.angle = angle#子弹的射击角度
		self.speed=20#子弹的移动速度
		self.scope=200#子弹的射击范围
		self.attack_power=3#子弹的杀伤力
		self.active = True

	'''不停移动'''
	def move(self):

		self.rect.left = self.rect.left - self.speed * math.cos(self.angle)
		self.rect.top = self.rect.top - self.speed * math.sin(self.angle)
		#self.rect.left, self.rect.top = self.position
	'''重置子弹的位置'''
	# def reset(self, position, angle=None):
	# 	if angle is None:
	# 		angle = random.random() * math.pi * 2
	# 	self.position = position
	# 	self.angle = angle
	# 	self.rect = self.image.get_rect()