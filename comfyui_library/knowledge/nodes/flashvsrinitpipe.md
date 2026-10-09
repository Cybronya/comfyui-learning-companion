# FlashVSRInitPipe

## 节点类型

`FlashVSRInitPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:COMBO`（5 次）
- `mode:COMBO`（5 次）
- `alt_vae:COMBO`（5 次）
- `force_offload:BOOLEAN`（5 次）
- `precision:COMBO`（5 次）
- `device:COMBO`（5 次）
- `attention_mode:COMBO`（5 次）

## 输出

- `pipe:PIPE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["FlashVSR-v1.1", "tiny", "none", true, "bf16", "cuda", "block_sparse_attention"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
