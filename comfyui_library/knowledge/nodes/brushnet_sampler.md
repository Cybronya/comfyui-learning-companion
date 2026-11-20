# brushnet_sampler

## 节点类型

`brushnet_sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `brushnet:BRUSHNET`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `prompt:STRING`（1 次）
- `n_prompt:STRING`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 2, 1.2, 0, 1, false, 0, 290531740028698, "randomize", "UniPCMultistepScheduler", "caption", "captionlowres,NSFW,log`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
