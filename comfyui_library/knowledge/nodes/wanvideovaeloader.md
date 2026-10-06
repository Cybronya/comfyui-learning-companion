# WanVideoVAELoader

## 节点类型

`WanVideoVAELoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（1 次）
- `model_name:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `use_cpu_cache:BOOLEAN`（1 次）
- `verbose:BOOLEAN`（1 次）

## 输出

- `vae:WANVAE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan2_1_VAE_bf16.safetensors", "bf16"]`（2 次）
- `["wan2.1/Wan2_1_VAE_bf16.safetensors", "bf16"]`（1 次）
- `["Wan2_1_VAE_bf16.safetensors", "bf16", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
