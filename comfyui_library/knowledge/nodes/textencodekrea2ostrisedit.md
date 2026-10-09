# TextEncodeKrea2OstrisEdit

## 节点类型

`TextEncodeKrea2OstrisEdit`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `prompt:STRING`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（2 次）
- `["transform the image to realistic photograph，The structural details of the image must remain consistent; only the style`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
