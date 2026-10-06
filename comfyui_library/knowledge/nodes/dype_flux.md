# DyPE_FLUX

## 节点类型

`DyPE_FLUX`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（12 次）
- `width:INT`（12 次）
- `height:INT`（12 次）
- `model_type:COMBO`（12 次）
- `method:COMBO`（12 次）
- `yarn_alt_scaling:BOOLEAN`（12 次）
- `enable_dype:BOOLEAN`（12 次）
- `base_resolution:INT`（12 次）
- `dype_start_sigma:FLOAT`（12 次）
- `dype_scale:FLOAT`（12 次）

## 输出

- `Patched Model:MODEL`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2048, 2048, "auto", "vision_yarn", true, true, 1328, 1, 2, 2, 0.5, 1.15]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
