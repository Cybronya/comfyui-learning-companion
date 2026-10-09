# PromptGenerateAPI

## 节点类型

`PromptGenerateAPI`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `chat_type:BOOLEAN`（1 次）
- `api_key:STRING`（1 次）
- `description:STRING`（1 次）
- `question:STRING`（1 次）
- `context_size:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["DeepSeek", true, "sk-a39cdeb88b8f475aa8c6fab031b52e7f", "将所提的问题从以下几个方面进行扩展\n1：主体 2：场景 3：风格 4：镜头 5：时长15秒。扩展成符合sora2视频生成`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
