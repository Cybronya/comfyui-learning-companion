# FL_SongGen_AutoStyle

## 节点类型

`FL_SongGen_AutoStyle`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SONGGEN_MODEL`（1 次）
- `lyrics:STRING`（1 次）
- `auto_style:COMBO`（1 次）
- `duration:FLOAT`（1 次）
- `temperature:FLOAT`（1 次）
- `cfg_coef:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `gen_type:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `mixed_audio:AUDIO`（1 次）
- `vocal_audio:AUDIO`（1 次）
- `bgm_audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[intro-short] ; [verse] Hello world.This is a test ; [chorus] Singing along.Making music ; [outro-short]", "Pop", 60, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
