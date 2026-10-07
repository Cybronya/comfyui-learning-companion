# GrokImageEditNodeV2

## 节点类型

`GrokImageEditNodeV2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（14 次）
- `model.images.image_2:IMAGE`（14 次）
- `model.images.image_3:IMAGE`（1 次）

## 输出

- `IMAGE:IMAGE`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Keep the original robot design and framing.\nTransform the scene into a cyberpunk night environment.\nReplace the ligh`（1 次）
- `["Create a vertical beauty product photography image. Use the first reference image as the character reference, keeping `（1 次）
- `["Change the images style into pixel art, maintain identity", "grok-imagine-image", "1K", 1, "auto", 219950673, "randomi`（1 次）
- `["Change the images style into 3d animation, maintain identity", "grok-imagine-image", "1K", 1, "auto", 179373478, "rand`（1 次）
- `["Change the images style into claymation, maintain identity", "grok-imagine-image", "1K", 1, "auto", 1786379440, "rando`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
