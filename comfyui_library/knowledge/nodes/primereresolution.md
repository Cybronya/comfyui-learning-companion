# PrimereResolution

## 节点类型

`PrimereResolution`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `seed:INT`（2 次）
- `model_version:STRING`（2 次）
- `model_concept:STRING`（2 次）
- `ratio:COMBO`（2 次）
- `resolution:BOOLEAN`（2 次）
- `sd1_res:COMBO`（2 次）
- `sdxl_res:COMBO`（2 次）
- `turbo_res:COMBO`（2 次）
- `rnd_orientation:BOOLEAN`（2 次）
- `orientation:COMBO`（2 次）

## 输出

- `WIDTH:INT`（2 次）
- `HEIGHT:INT`（2 次）
- `SQUARE_SHAPE:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Square [1:1]", true, 768, 1024, 512, false, "Horizontal", false, false, 1.6, 2.8]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
