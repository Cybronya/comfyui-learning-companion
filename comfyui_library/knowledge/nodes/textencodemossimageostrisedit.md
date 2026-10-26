# TextEncodeMOSSImageOstrisEdit

## 节点类型

`TextEncodeMOSSImageOstrisEdit`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `vae:VAE`（6 次）
- `image1:IMAGE`（6 次）
- `image2:IMAGE`（6 次）
- `image3:IMAGE`（6 次）
- `prompt:STRING`（6 次）

## 输出

- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（3 次）
- `["Use Picture 1 as the reference.\nKeep the same person, pose, camera angle,\nlighting, and background.\nChange only her`（2 次）
- `["Same adult woman, exact facial identity and photographic style as Picture 1. Keep her light-brown twin braids, brown e`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
