# AddWaterMarkNode

## 节点类型

`AddWaterMarkNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `input_img:IMAGE`（6 次）
- `font_path:PATH`（5 次）
- `text:STRING`（5 次）
- `text_color:STRING`（5 次）
- `text_size:INT`（5 次）
- `text_opacity:FLOAT`（5 次）
- `text_angle:INT`（5 次）
- `text_space:INT`（5 次）
- `image:IMAGE`（2 次）
- `watermark:IMAGE`（2 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["水印", "#FFFFFF", 30, 0.094, 30, 25]`（2 次）
- `["AIFSH", "#FFFFFF", 20, 0.15, 30, 25]`（2 次）
- `["AIFSH", "#FFFFFF", 20, 0.15, 30, 56]`（1 次）
- `["", "#FFFFFF", 30, 0.123, 30, 200]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
