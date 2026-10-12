# UniversalAPINode

## 节点类型

`UniversalAPINode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 图像1:IMAGE`（5 次）
- `🖼️ 图像2:IMAGE`（5 次）
- `🖼️ 图像3:IMAGE`（5 次）
- `🖼️ 图像4:IMAGE`（5 次）
- `🎬 视频:IMAGE`（5 次）
- `🎵 音频:AUDIO`（5 次）
- `🎯 系统角色:STRING`（5 次）
- `💬 用户输入:STRING`（5 次）
- `🤖 模型名称:STRING`（5 次）
- `🌐 API地址:STRING`（5 次）

## 输出

- `AI回复:STRING`（5 次）
- `response:STRING`（5 次）
- `raw_json:STRING`（5 次）
- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你是一个专业的AI助手", "帮我详细描述这个图片，输出中文提示词，仅输出提示词，不要带任何解释性文字", "gemini-3-pro-preview-thinking-*", "https://ai.t8star.cn/v1/chat`（2 次）
- `["一、 角色与目标 (Role & Objective)\n角色: 你是一位精通电影摄影、视觉艺术和导演技巧的AI助手。你的核心任务是为先进的文生视频模型 Wan 2.2 撰写专业、详尽、富有想象力的提示词。\n目标: 根据用户提供的核心`（1 次）
- `["你是一个专业的AI助手", "帮我详细描述这个图片，输出中文提示词，仅输出提示词，不要带任何解释性文字", "gemini-3-pro-preview", "https://generativelanguage.googleapis.c`（1 次）
- `["一、 角色与目标 (Role & Objective)\n角色: 你是一位精通电影摄影、视觉艺术和导演技巧的AI助手。你的核心任务是为先进的文生视频模型 Wan 2.2 撰写专业、详尽、富有想象力的提示词。\n目标: 根据用户提供的核心`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
