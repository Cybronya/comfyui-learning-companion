# AniCrafterPreText

## 节点类型

`AniCrafterPreText`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `text_emb:AniCrafter_TEXT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["umt5-xxl-enc-bf16.safetensors", false, true, "human in a scene", "细节模糊不清，字幕，作品，画作，画面，静止，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手`（1 次）
- `["umt5-xxl-enc-bf16.safetensors", false, true, "character in a scene", "细节模糊不清，字幕，作品，画作，画面，静止，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
