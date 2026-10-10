# Comfly_vidu_text2video

## 节点类型

`Comfly_vidu_text2video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `style:COMBO`（1 次）
- `duration:INT`（1 次）
- `seed:INT`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `movement_amplitude:COMBO`（1 次）
- `bgm:BOOLEAN`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `task_id:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "viduq2", "", "general", 5, 25158839, "randomize", "16:9", "720p", "auto", false, false, false, 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
