# Comfly_suno_upload_extend

## 节点类型

`Comfly_suno_upload_extend`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip_id:STRING`（2 次）
- `prompt:STRING`（2 次）
- `tags:STRING`（2 次）
- `title:STRING`（2 次）
- `continue_at:INT`（2 次）
- `version:COMBO`（2 次）
- `api_key:STRING`（2 次）
- `seed:INT`（2 次）

## 输出

- `audio1:AUDIO`（2 次）
- `audio2:AUDIO`（2 次）
- `audio_url1:STRING`（2 次）
- `audio_url2:STRING`（2 次）
- `task_id:STRING`（2 次）
- `response:STRING`（2 次）
- `clip_id1:STRING`（2 次）
- `clip_id2:STRING`（2 次）
- `duration:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "", 28, "v5", "", 587850454, "randomize"]`（1 次）
- `["", "", "", 28, "v5", "", 1292671510, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
