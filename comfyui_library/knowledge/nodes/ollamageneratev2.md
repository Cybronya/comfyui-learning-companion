# OllamaGenerateV2

## 节点类型

`OllamaGenerateV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `connectivity:OLLAMA_CONNECTIVITY`（1 次）
- `options:OLLAMA_OPTIONS`（1 次）
- `images:IMAGE`（1 次）
- `context:OLLAMA_CONTEXT`（1 次）
- `meta:OLLAMA_META`（1 次）
- `system:STRING`（1 次）
- `prompt:STRING`（1 次）
- `think:BOOLEAN`（1 次）
- `keep_context:BOOLEAN`（1 次）
- `format:COMBO`（1 次）

## 输出

- `result:STRING`（1 次）
- `thinking:STRING`（1 次）
- `context:OLLAMA_CONTEXT`（1 次）
- `meta:OLLAMA_META`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你是专业文案顶级创作者，现在给你一张图片，请写出专业的分镜图，剧情中新场景都和老场景有关联，人物的情感变化，动作变化，场景变化，风格变化等有内在逻辑，不突兀，并符合文案要求，同时参考提供的图片，重点保证角色特征的一致性不变，尤其是脸部的`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
