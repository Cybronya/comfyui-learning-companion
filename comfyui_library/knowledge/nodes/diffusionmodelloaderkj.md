# DiffusionModelLoaderKJ

## 节点类型

`DiffusionModelLoaderKJ`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `extra_state_dict:STRING`（2 次）
- `model_name:COMBO`（2 次）
- `weight_dtype:COMBO`（2 次）
- `compute_dtype:COMBO`（2 次）
- `patch_cublaslinear:BOOLEAN`（2 次）
- `sage_attention:COMBO`（2 次）
- `enable_fp16_accumulation:BOOLEAN`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors", "default", "default", false, "auto", true]`（1 次）
- `["minimax_h3_fl2va_pruned_int8_convrot.safetensors", "default", "default", false, "auto", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
