# AddLabel

## 节点类型

`AddLabel`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（7 次）
- `caption:STRING`（7 次）
- `text_x:INT`（7 次）
- `text_y:INT`（7 次）
- `height:INT`（7 次）
- `font_size:INT`（7 次）
- `font_color:STRING`（7 次）
- `label_color:STRING`（7 次）
- `font:COMBO`（7 次）
- `text:STRING`（7 次）

## 输出

- `IMAGE:IMAGE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 2, 82, 24, "white", "black", "FreeMono.ttf", "head_swap: start with <image1> as the base image, keeping its lightin`（1 次）
- `[10, 2, 48, 32, "white", "black", "FreeMono.ttf", "ZIT_", "overlay"]`（1 次）
- `[10, 2, 48, 32, "white", "black", "FreeMono.ttf", "qwen_image_21", "overlay"]`（1 次）
- `[10, 2, 48, 32, "white", "black", "FreeMono.ttf", "krea2_", "overlay"]`（1 次）
- `[15, 2, 48, 32, "white", "black", "FreeMono.ttf", "raw", "up"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
