# PainterQwenImageEditPlus

## 节点类型

`PainterQwenImageEditPlus`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `vae:VAE`（6 次）
- `image1:IMAGE`（6 次）
- `image2:IMAGE`（6 次）
- `image3:IMAGE`（6 次）
- `image1_mask:MASK`（6 次）
- `prompt:STRING`（6 次）
- `width:INT`（6 次）
- `height:INT`（6 次）

## 输出

- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `latent:LATENT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 512, 920]`（4 次）
- `["", 1080, 1080]`（1 次）
- `["写实近景美食摄影，竖版9:16，暖色室内灯光。画面主体是一张刚做好的人物糖画，放置在不锈钢金属台面上：糖画以透明琥珀金色糖浆勾勒并局部填充，线条有轻微厚薄变化，表面光泽强，可见细小气泡与凝固流纹，高光反射明显，插着一根浅黄竹签。糖画左下`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
