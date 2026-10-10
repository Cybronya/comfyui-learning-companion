# ADE_AnimateDiffLoaderWithContext

## 节点类型

`ADE_AnimateDiffLoaderWithContext`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `context_options:CONTEXT_OPTIONS`（1 次）
- `motion_lora:MOTION_LORA`（1 次）
- `ad_settings:AD_SETTINGS`（1 次）
- `sample_settings:SAMPLE_SETTINGS`（1 次）
- `ad_keyframes:AD_KEYFRAMES`（1 次）
- `model_name:COMBO`（1 次）
- `beta_schedule:COMBO`（1 次）
- `motion_scale:FLOAT`（1 次）
- `apply_v2_models_properly:BOOLEAN`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["AnimateLCM/sd15_t2v_beta.ckpt", "autoselect", 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
