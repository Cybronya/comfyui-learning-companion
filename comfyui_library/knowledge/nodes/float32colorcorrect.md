# Float32ColorCorrect

## 节点类型

`Float32ColorCorrect`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `exposure:FLOAT`（4 次）
- `contrast:FLOAT`（4 次）
- `brightness:FLOAT`（4 次）
- `saturation:FLOAT`（4 次）
- `gamma:FLOAT`（4 次）
- `lift_r:FLOAT`（4 次）
- `lift_g:FLOAT`（4 次）
- `lift_b:FLOAT`（4 次）
- `gain_r:FLOAT`（4 次）

## 输出

- `image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, 0, 1, 2, 0, 0, 0, 1, 1, 1, "Rec.709 / sRGB", false]`（2 次）
- `[0, 1, 0, 1, 0.5, 0, 0, 0, 1, 1, 1, "Rec.709 / sRGB", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
