# workflow>儿童AI摄影

## 节点类型

`workflow>儿童AI摄影`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-dev-fp8.safetensors", "fp8_e5m2", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "ae.s`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
