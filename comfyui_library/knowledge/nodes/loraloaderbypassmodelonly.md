# LoraLoaderBypassModelOnly

## 节点类型

`LoraLoaderBypassModelOnly`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model:MODEL`（8 次）
- `lora_name:COMBO`（8 次）
- `strength_model:FLOAT`（8 次）

## 输出

- `MODEL:MODEL`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_turbo_v4_step600_ema_DasiwaREF2VAHybridV1_0_curveproj1025_compat_v001.safetensors", 1]`（5 次）
- `["qwen_image_2.1_viggle_turbo_v0.2.1_r256_comfy-t8.safetensors", 1]`（2 次）
- `["youhuaqwen21_c1-st10000.safetensors", 0.9000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
