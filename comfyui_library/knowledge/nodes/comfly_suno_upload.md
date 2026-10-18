# Comfly_suno_upload

## 节点类型

`Comfly_suno_upload`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio:AUDIO`（5 次）
- `api_key:STRING`（5 次）
- `upload_filename:STRING`（5 次）
- `seed:INT`（5 次）

## 输出

- `clip_id:STRING`（5 次）
- `title:STRING`（5 次）
- `tags:STRING`（5 次）
- `lyrics:STRING`（5 次）
- `response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "audio.mp3", 522994153, "randomize"]`（1 次）
- `["", "audio.mp3", 946630656, "randomize"]`（1 次）
- `["", "audio.mp3", 2014117041, "randomize"]`（1 次）
- `["", "audio.mp3", 1979769733, "randomize"]`（1 次）
- `["", "audio.mp3", 1813618906, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
