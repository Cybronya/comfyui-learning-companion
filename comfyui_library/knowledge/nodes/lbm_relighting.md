# LBM_Relighting

## 节点类型

`LBM_Relighting`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:COMBO`（3 次）
- `steps:INT`（3 次）
- `precision:COMBO`（3 次）
- `bridge_noise_sigma:FLOAT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["model.safetensors", 28, "bf16", 0.0010000000000000002]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
