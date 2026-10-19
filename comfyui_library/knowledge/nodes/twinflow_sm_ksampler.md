# TwinFlow_SM_KSampler

## 节点类型

`TwinFlow_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:TwinFlow_SM_Model`（3 次）
- `positive:CONDITIONING`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `steps:COMBO`（3 次）
- `seed:INT`（3 次）
- `block_num:INT`（3 次）
- `force_offload:COMBO`（3 次）

## 输出

- `latents:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[768, 1024, 2, 1004818603, "randomize", 0, "all"]`（1 次）
- `[768, 1024, 2, 1128247136, "randomize", 0, "none"]`（1 次）
- `[2048, 2048, 2, 328646780, "randomize", 0, "clip"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
