---
key: 图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json
name: SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json
hash: 59cb8789f41dbdf7
coverage: 0.533333
learned_at: 2026-10-23 11:23:27
nodes: [CheckpointLoaderSimple, DeepTranslatorTextNode, CLIPTextEncode, SAM3_Detect, LoadImage, DrawMaskOnImage, SaveImage, Note, Note, Note, Note, Note, Note, Note, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SAM-3.1图像语义分割提取遮罩+全节点注释_2052975663912628226.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（15 个）：
- `CheckpointLoaderSimple` ★核心
- `DeepTranslatorTextNode`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `LoadImage`
- `DrawMaskOnImage`
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **53%**（8/15）

**有卡**：`CheckpointLoaderSimple`、`DeepTranslatorTextNode`、`CLIPTextEncode`、`SAM3_Detect`、`LoadImage`、`DrawMaskOnImage`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、DrawMaskOnImage、SAM3_Detect、DeepTranslatorTextNode、sd15-t2i-basic
