# workflow>抽卡优化控制

## 节点类型

`workflow>抽卡优化控制`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）
- `CLIPTextEncode 2 clip:CLIP`（1 次）
- `text:STRING`（1 次）
- `CLIPTextEncode text:STRING`（1 次）
- `start:FLOAT`（1 次）
- `end:FLOAT`（1 次）
- `CLIPTextEncode 2 text:STRING`（1 次）
- `ConditioningSetTimestepRange start:FLOAT`（1 次）
- `ConditioningSetTimestepRange end:FLOAT`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `ConditioningCombine 条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合 杂乱的背景，三条`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
