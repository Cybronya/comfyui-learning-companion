# SongBloomGenerate

## 节点类型

`SongBloomGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SONGBLOOM_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `lyrics:STRING`（1 次）
- `cfg_coef:FLOAT`（1 次）
- `temperature:FLOAT`（1 次）
- `steps:INT`（1 次）
- `dit_cfg_type:COMBO`（1 次）
- `use_sampling:BOOLEAN`（1 次）
- `top_k:INT`（1 次）
- `max_duration:FLOAT`（1 次）

## 输出

- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello world, this is a test song", 1.5, 0.9, 36, "h", true, 100, 200, 50701922, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
