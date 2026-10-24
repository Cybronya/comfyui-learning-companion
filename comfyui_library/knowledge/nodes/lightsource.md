# LightSource

## 节点类型

`LightSource`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 20 个 workflow 中。

## 输入

- `prev_image:IMAGE`（20 次）
- `height:INT`（20 次）
- `width:INT`（19 次）
- `start_color:STRING`（10 次）
- `end_color:STRING`（9 次）
- `light_position:COMBO`（3 次）
- `multiplier:FLOAT`（3 次）
- `batch_size:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Top Left Light", 2.5, "#FFFFFF", "#000000", 512, 512, 1]`（3 次）
- `["Top Light", 2, "#FFFFFF", "#000000", 512, 512, 1]`（3 次）
- `["Bottom Left Light", 2, "#FFFFFF", "#000000", 512, 512, 1]`（3 次）
- `["Left Light", 1, "#FFFFFF", "#000000", 512, 512, 1]`（3 次）
- `["Left Light", 1.0000000000000002, "#FFFFFF", "#000000", 512, 512, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
