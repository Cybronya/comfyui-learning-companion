# PIP_图像联结

## 节点类型

`PIP_图像联结`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `direction:COMBO`（5 次）
- `max_dimension:INT`（5 次）
- `gap:INT`（5 次）
- `background_color:COMBO`（5 次）

## 输出

- `image:IMAGE`（5 次）
- `width_int:INT`（5 次）
- `height_int:INT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["左右", 1356, 0, "白色"]`（3 次）
- `["左右", 2048, 0, "白色"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
