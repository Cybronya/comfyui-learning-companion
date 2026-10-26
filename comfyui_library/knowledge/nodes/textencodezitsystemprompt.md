# TextEncodeZITSystemPrompt

## 节点类型

`TextEncodeZITSystemPrompt`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `prompt:STRING`（4 次）
- `system_prompt:STRING`（4 次）

## 输出

- `CONDITIONING:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["画面扭曲，物体变形，模糊杂乱，多余碎片，畸形", ""]`（2 次）
- `["游戏我的世界中人物史蒂夫手握着钻石剑在草坪上迎面向我奔跑过来", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
