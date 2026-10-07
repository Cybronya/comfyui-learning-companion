# BagelImageEdit

## 节点类型

`BagelImageEdit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:BAGEL_MODEL`（17 次）
- `image:IMAGE`（17 次）
- `prompt:STRING`（1 次）

## 输出

- `image:IMAGE`（17 次）
- `thinking:STRING`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["turn to 3d chibi", 833385, "randomize", 4, 2, 50, false, 0, 3, 1, "text_channel", 0.3]`（1 次）
- `["Help me generate a 3D PVC figure based on the image, which is placed in a plastic box.", 762610, "randomize", 4, 2, 50`（1 次）
- `["Transform the characters in the scene into a 3D chibi style and place them on a Polaroid photo. The photo paper is hel`（1 次）
- `["Change to clay style", 978922, "randomize", 4, 2, 50, true, 0, 3, 1, "global", 0.7000000000000001]`（1 次）
- `["Make her gives a thumbs-up", 309118, "randomize", 4, 2, 50, true, 0, 3, 1, "global", 0.7000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
