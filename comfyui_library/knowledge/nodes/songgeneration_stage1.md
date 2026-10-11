# SongGeneration_Stage1

## 节点类型

`SongGeneration_Stage1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `vae:COMBO`（1 次）
- `seperate_model:COMBO`（1 次）
- `prompt_pt:COMBO`（1 次）
- `auto_prompt_audio_type:COMBO`（1 次）
- `model_1rvq:COMBO`（1 次）
- `demucs_pt:COMBO`（1 次）
- `lyric:STRING`（1 次）

## 输出

- `cond:SongGeneration_Cond`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["autoencoder_music_1320k.ckpt", "model_2.safetensors", "new_auto_prompt.pt", "Jazz", "none", "none", "[verse]\n在那雪山之上.有`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
