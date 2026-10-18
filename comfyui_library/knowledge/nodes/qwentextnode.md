# QwenTextNode

## 节点类型

`QwenTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `user_prompt:STRING`（1 次）
- `api_token:STRING`（1 次）
- `system_prompt:STRING`（1 次）
- `model:STRING`（1 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `stream:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个40岁左右的现代女性声音。语速稍快，干练利落，节奏紧凑。音色清亮有质感，中气十足，完全没有虚弱感。语气笃定、自信、从容，像一位思维敏捷的职场高管在进行高效沟通。既没有播音腔的刻意，也绝不咬牙切齿，而是带有一种“看透本质”的清醒感和说`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
