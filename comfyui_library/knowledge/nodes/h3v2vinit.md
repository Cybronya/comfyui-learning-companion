# H3V2VInit

## 节点类型

`H3V2VInit`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `samples:LATENT`（4 次）
- `oracle_samples:LATENT`（4 次）
- `length:INT`（4 次）
- `freeze_threshold:FLOAT`（4 次）
- `freeze_grow:INT`（4 次）
- `mask:MASK`（4 次）
- `audio_latent:LATENT`（4 次）

## 输出

- `LATENT:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 2]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
