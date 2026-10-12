# Qwen_VLM_API

## 节点类型

`Qwen_VLM_API`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model:COMBO`（2 次）
- `api_key:STRING`（2 次）
- `max_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `system_prompt:STRING`（2 次）
- `user_prompt:STRING`（2 次）
- `stream:BOOLEAN`（2 次）

## 输出

- `reasoning_content:STRING`（2 次）
- `answer:STRING`（2 次）
- `tokens_usage:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen2.5-vl-72b-instruct", "", 1024, 0.8, 0.6, "【输入方式】：参考图 + 文本描述  \n【延展目标】：基于上一张图的画面风格、人物外形、光影氛围、镜头语言，生成下一张分镜图，使得剧情延续\`（1 次）
- `["qwen2.5-vl-72b-instruct", "", 1024, 0.8, 0.6, "你是一个能分析图像的AI助手。请仔细观察图像，并根据用户的问题提供详细、准确的描述。", "请描述这张图片。", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
