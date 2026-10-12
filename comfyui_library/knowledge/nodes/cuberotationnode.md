# CubeRotationNode

## 节点类型

`CubeRotationNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（4 次）
- `rotation_style:COMBO`（4 次）
- `rotation_speed:FLOAT`（4 次）
- `duration:FLOAT`（4 次）
- `fps:INT`（4 次）
- `background_color:STRING`（4 次）
- `width:INT`（4 次）
- `height:INT`（4 次）
- `cube_size:FLOAT`（4 次）
- `perspective:FLOAT`（4 次）

## 输出

- `video:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["random_spin", 1.2, 1, 30, "#FFFFFF", 640, 960, 1, 1000]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
