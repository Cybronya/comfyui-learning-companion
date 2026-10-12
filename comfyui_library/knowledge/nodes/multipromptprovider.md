# MultiPromptProvider

## 节点类型

`MultiPromptProvider`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `prompts:STRING`（2 次）

## 输出

- `conditionings:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a chimpanzee walks in the jungle |\na chimpanzee stops and eats a snack |\na chimpanzee lays on the ground"]`（1 次）
- `["ultra-realistic cinematic scene of a smiling snowboarder racing down a steep mountain slope with a massive avalanche t`（1 次）
- `["a chinese woman put the book on the desk |\na chinese woman stand up |\na chinese woman face to the camera and smile"]`（1 次）
- `["A Chinese woman drew her sword|\nzoom out|\nA Chinese woman points a sword at the camera"]`（1 次）
- `[""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
