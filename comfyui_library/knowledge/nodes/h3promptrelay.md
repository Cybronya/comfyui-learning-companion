# H3PromptRelay

## 节点类型

`H3PromptRelay`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `clip:CLIP`（1 次）
- `latent:LATENT`（1 次）
- `global_prompt:STRING`（1 次）
- `local_prompts:STRING`（1 次）
- `segment_lengths:STRING`（1 次）
- `epsilon:FLOAT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["10秒暗黑玄幻法术战斗视频。环境深邃，漫天飘浮着发光的黄色符纸。主角是一位梳着粗黑长辫、背负长剑的少女驱魔师。她身穿带有古文符咒的暗色战袍，右手维持施法结印，指尖凝聚着金光。\n完整动态： 少女眼神冷冽，指尖金光骤然爆发出刺眼的亮度，照`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
