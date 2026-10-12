# StableAvatar_LoadModel

## 节点类型

`StableAvatar_LoadModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `transformer:COMBO`（1 次）
- `vae:COMBO`（1 次）
- `lora:COMBO`（1 次）
- `enable_teacache:BOOLEAN`（1 次）
- `use_mmgp:COMBO`（1 次）
- `GPU_memory_mode:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）

## 输出

- `model:MODEL_PIPE_SA`（1 次）
- `info:MODEL_INFO_SA`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["transformer3d-rec-vec.pt", "Wan2.1_VAE.pth", "None", false, "HighRAM_LowVRAM", "None", "bfloat16"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
