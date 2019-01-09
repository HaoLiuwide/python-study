8067
# # 打开一张图
# img = Image.open('C:\\Users\\56942\\Desktop\\验证码\\42.png')
# # 图片尺寸
# img_size = img.size
# h = img_size[1]  # 图片高度
# w = img_size[0]  # 图片宽度
#
# x = 0.1 * w
# y = 0.38 * h
# w = 0.75 * w
# h = 0.6 * h
#
# # 开始截取
# region = img.crop((x, y, x + w, y + h))
# # 保存图片
# region.save("test.png")

