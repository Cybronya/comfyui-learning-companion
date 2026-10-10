# MiniMaxH3ChainSegmentSave

## 节点类型

`MiniMaxH3ChainSegmentSave`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `state:H3_CHAIN_STATE`（1 次）
- `images:IMAGE`（1 次）
- `sampled_latent:LATENT`（1 次）
- `audio:AUDIO`（1 次）
- `images_with_overlap:IMAGE`（1 次）
- `denoised_latent:LATENT`（1 次）

## 输出

- `segment:H3_CHAIN_SEGMENT`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
