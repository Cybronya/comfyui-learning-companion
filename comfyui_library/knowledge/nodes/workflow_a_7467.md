# workflow>a

## 节点类型

`workflow>a`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `ControlNetApplyAdvanced image:IMAGE`（1 次）
- `KSampler negative:CONDITIONING`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `control_net_name:COMBO`（1 次）
- `lora_name:COMBO`（1 次）

## 输出

- `负面条件:CONDITIONING`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-dev-fp8.safetensors", "fp8_e4m3fn", "ae.sft", "FLUX.1-dev-Controlnet-Union-InstantX.safetensors", "F1人文摄影风格-富士胶片`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
