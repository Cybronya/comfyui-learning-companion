# WanAnimatePlus Uni3C ControlnetLoader

## 节点类型

`WanAnimatePlus Uni3C ControlnetLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（5 次）
- `model:COMBO`（5 次）
- `base_precision:COMBO`（5 次）
- `quantization:COMBO`（5 次）
- `load_device:COMBO`（5 次）
- `attention_mode:COMBO`（5 次）

## 输出

- `controlnet:WANVIDEOCONTROLNET`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan21_Uni3C_controlnet_fp16.safetensors", "fp16", "disabled", "offload_device", "sageattn"]`（2 次）
- `["Wan21_Uni3C_controlnet_fp16.safetensors", "bf16", "disabled", "offload_device", "sageattn"]`（2 次）
- `["Wan21_Uni3C_controlnet_fp16.safetensors", "fp16", "disabled", "offload_device", "sdpa"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
