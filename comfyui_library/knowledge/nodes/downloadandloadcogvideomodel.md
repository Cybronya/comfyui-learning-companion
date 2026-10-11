# DownloadAndLoadCogVideoModel

## 节点类型

`DownloadAndLoadCogVideoModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `block_edit:TRANSFORMERBLOCKS`（4 次）
- `lora:COGLORA`（4 次）
- `compile_args:COMPILEARGS`（4 次）
- `model:COMBO`（4 次）
- `precision:COMBO`（4 次）
- `quantization:COMBO`（4 次）
- `enable_sequential_cpu_offload:BOOLEAN`（4 次）
- `attention_mode:COMBO`（4 次）
- `load_device:COMBO`（4 次）

## 输出

- `model:COGVIDEOMODEL`（4 次）
- `vae:VAE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["THUDM/CogVideoX-5b", "bf16", "disabled", false, "sdpa", "main_device"]`（2 次）
- `["kijai/CogVideoX-5b-1.5-T2V", "bf16", "disabled", false, "comfy", "main_device"]`（1 次）
- `["kijai/CogVideoX-5b-1.5-I2V", "bf16", "disabled", false, "comfy", "main_device"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
