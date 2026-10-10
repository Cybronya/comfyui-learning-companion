---
key: 图片生成/图生图/MJ悠船V8.2 美学艺术图像模型 文生图+图生图_2093149914611150850.json
name: MJ悠船V8.2 美学艺术图像模型 文生图+图生图_2093149914611150850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MJ悠船V8.2 美学艺术图像模型 文生图+图生图_2093149914611150850.json
hash: 8855d0b8a297debb
coverage: 0.25
learned_at: 2026-10-10 20:48:04
nodes: [孤海注释, LoadImage, 孤海注释, LoadImage, 孤海注释, 孤海注释, RH_YouchuanTextToImageV82Fast, 孤海注释, PlaySound|pysssss, MarkdownNote, JjkText, 孤海注释, 孤海注释, JjkText, SaveImage, PreviewImage]
patterns: []
missing: [PlaySound|pysssss]
discoveries: [次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/MJ悠船V8.2 美学艺术图像模型 文生图+图生图_2093149914611150850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MJ悠船V8.2 美学艺术图像模型 文生图+图生图_2093149914611150850.json`

## 结构

**生成流程**：Output → Other

**节点**（16 个）：
- `孤海注释`
- `LoadImage`
- `孤海注释`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `RH_YouchuanTextToImageV82Fast`
- `孤海注释`
- `PlaySound|pysssss`
- `MarkdownNote`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `JjkText`
- `SaveImage`
- `PreviewImage`

## 知识

覆盖率 **25%**（4/16）

**有卡**：`LoadImage`、`RH_YouchuanTextToImageV82Fast`、`SaveImage`

**缺卡**（1）：`PlaySound|pysssss`

**用到的条目**：LoadImage、SaveImage、RH_YouchuanTextToImageV82Fast、sd15-t2i-basic、sd15-t2i-lora、Text、CS_Preview_Any、easy_multitrackinfooutput

## 学习发现

- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
