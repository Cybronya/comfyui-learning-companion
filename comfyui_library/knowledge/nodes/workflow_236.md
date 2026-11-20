# workflow>法线+深度

## 节点类型

`workflow>法线+深度`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pixels:IMAGE`（1 次）
- `model:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `LoadLotusModel model:COMBO`（1 次）
- `LoadLotusModel precision:COMBO`（1 次）
- `seed:INT`（1 次）
- `per_batch:INT`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）
- `LotusSampler seed:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `VAEDecode IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lotus/lotus-depth-g-v1-0-fp16.safetensors", "fp16", "vae-ft-mse-840000-ema-pruned.safetensors", "lotus/lotus-normal-g-`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
