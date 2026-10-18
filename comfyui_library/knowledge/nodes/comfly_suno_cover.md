# Comfly_suno_cover

## 节点类型

`Comfly_suno_cover`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `cover_clip_id:STRING`（3 次）
- `prompt:STRING`（3 次）
- `title:STRING`（3 次）
- `tags:STRING`（3 次）
- `version:COMBO`（3 次）
- `make_instrumental:BOOLEAN`（3 次）
- `api_key:STRING`（3 次）
- `negative_tags:STRING`（3 次）
- `seed:INT`（3 次）

## 输出

- `audio1:AUDIO`（3 次）
- `audio2:AUDIO`（3 次）
- `audio_url1:STRING`（3 次）
- `audio_url2:STRING`（3 次）
- `task_id:STRING`（3 次）
- `response:STRING`（3 次）
- `clip_id1:STRING`（3 次）
- `clip_id2:STRING`（3 次）
- `image_url1:STRING`（3 次）
- `image_url2:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "I will give you all", "抒情，温柔", "v5", false, "", "", 1865210865, "randomize"]`（1 次）
- `["", "", "", "v5", false, "", "", 1195344582, "randomize"]`（1 次）
- `["", "I will give you all", "抒情，温柔", "v5", false, "", "", 716218781, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
