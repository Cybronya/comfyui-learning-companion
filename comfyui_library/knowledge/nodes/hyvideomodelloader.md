# HyVideoModelLoader

## 节点类型

`HyVideoModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `compile_args:COMPILEARGS`（1 次）
- `block_swap_args:BLOCKSWAPARGS`（1 次）
- `lora:HYVIDLORA`（1 次）
- `model:COMBO`（1 次）
- `base_precision:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `load_device:COMBO`（1 次）
- `attention_mode:COMBO`（1 次）
- `auto_cpu_offload:BOOLEAN`（1 次）
- `upcast_rope:BOOLEAN`（1 次）

## 输出

- `model:HYVIDEOMODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hunyuan_video_720_cfgdistill_bf16.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn_varlen", false, true`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
