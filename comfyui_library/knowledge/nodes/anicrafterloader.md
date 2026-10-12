# AniCrafterLoader

## 节点类型

`AniCrafterLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `model:MODEL_AniCrafter`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors", "Wan2.1_VAE.pth", "none", "none", 1, 1, 1, "LowRAM_LowVRAM"]`（1 次）
- `["Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors", "Wan2.1_VAE.pth", "Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
