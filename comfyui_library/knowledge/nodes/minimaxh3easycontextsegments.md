# MiniMaxH3EasyContextSegments

## 节点类型

`MiniMaxH3EasyContextSegments`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `h3_bundle:MINIMAX_H3_BUNDLE`（1 次）
- `media:*`（1 次）
- `mode:COMBO`（1 次）
- `audio_mode:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `resolution:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `seconds:FLOAT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `h3_context:MINIMAX_H3_CONTEXT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["上下文分段", "默认", "参考素材：<Picture 1>（本段唯一参考基准：人物五官、发型、服装与场景均以该图为准）\n主体与场景：一位棕色长发编成两条长麻花辫的年轻女性站在深炭灰色店面外墙前的中景（膝盖以上，无远景，无全景），戴`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
