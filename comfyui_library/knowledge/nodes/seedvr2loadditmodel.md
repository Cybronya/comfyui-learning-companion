# SeedVR2LoadDiTModel

## 节点类型

`SeedVR2LoadDiTModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 67 个 workflow 中。

## 输入

- `cache_model:MODEL`（73 次）
- `torch_compile_args:SEEDVR2_TORCH_COMPILE`（73 次）
- `model:COMBO`（73 次）
- `device:COMBO`（73 次）
- `blocks_to_swap:INT`（73 次）
- `swap_io_components:BOOLEAN`（73 次）
- `offload_device:COMBO`（73 次）
- `attention_mode:COMBO`（73 次）

## 输出

- `dit:SEEDVR2_DIT`（73 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_ema_3b_fp8_e4m3fn.safetensors", "cuda:0", 32, true, "cpu", "sdpa"]`（15 次）
- `["seedvr2_ema_7b-Q4_K_M.gguf", "cuda:0", 36, false, "cpu", "sdpa"]`（8 次）
- `["seedvr2_ema_7b-Q8_K_M.gguf", "cuda:0", 15, false, "cpu", "sageattn_3"]`（6 次）
- `["seedvr2_ema_7b-Q4_K_M.gguf", "cuda:0", 0, false, "none", false]`（6 次）
- `["seedvr2_ema_7b-Q8_0.gguf", "cuda:0", 32, true, "cpu", "sdpa"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
