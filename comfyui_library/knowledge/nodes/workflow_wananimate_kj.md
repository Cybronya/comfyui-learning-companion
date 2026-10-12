# workflow>WanAnimate KJ加载器

## 节点类型

`workflow>WanAnimate KJ加载器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `quantization:COMBO`（3 次）
- `load_device:COMBO`（3 次）
- `attention_mode:COMBO`（3 次）
- `rms_norm_function:COMBO`（3 次）
- `model:COMBO`（3 次）
- `base_precision:COMBO`（3 次）
- `clip:COMBO`（3 次）
- `precision:COMBO`（3 次）
- `:COMBO`（3 次）
- `LoadWanVideoT5TextEncoder quantization:COMBO`（3 次）

## 输出

- `clip:WANTEXTENCODER`（3 次）
- `vae:WANVAE`（3 次）
- `model:WANVIDEOMODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["disabled", "offload_device", "sageattn", "default", "Wan22Animate/Wan2_2-Animate-14B_fp8_scaled_e4m3fn_KJ_v2.safetenso`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
