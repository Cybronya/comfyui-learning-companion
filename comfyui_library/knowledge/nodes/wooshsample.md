# WooshSample

## 节点类型

`WooshSample`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `gen_model:WOOSH_GEN_MODEL`（1 次）
- `text_conditioning:WOOSH_TEXT_COND`（1 次）
- `video:WOOSH_VIDEO`（1 次）
- `prompt:STRING`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `seed:INT`（1 次）
- `latent_frames:INT`（1 次）
- `force_offload:BOOLEAN`（1 次）

## 输出

- `video_frames:IMAGE`（1 次）
- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 50, 4.5, 2186694101, "randomize", 501, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
