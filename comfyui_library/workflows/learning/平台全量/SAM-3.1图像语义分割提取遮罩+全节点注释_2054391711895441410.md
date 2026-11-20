---
key: 平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json
name: SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json
hash: 926e915ee1d4f35e
coverage: 0.6
learned_at: 2026-11-14 00:55:00
nodes: [Note, CheckpointLoaderSimple, CLIPTextEncode, Note, DeepTranslatorTextNode, PreviewAny, DrawMaskOnImage, SaveImage, Note, Note, LoadImage, JjkText, SAM3_Detect, MaskToImage, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json

> 来源文件 `comfyui_library/workflows/平台全量/SAM-3.1图像语义分割提取遮罩+全节点注释_2054391711895441410.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（15 个）：
- `Note`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `DeepTranslatorTextNode`
- `PreviewAny`
- `DrawMaskOnImage`
- `SaveImage`
- `Note`
- `Note`
- `LoadImage`
- `JjkText`
- `SAM3_Detect`
- `MaskToImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **60%**（9/15）

**有卡**：`CheckpointLoaderSimple`、`CLIPTextEncode`、`DeepTranslatorTextNode`、`DrawMaskOnImage`、`SaveImage`、`LoadImage`、`SAM3_Detect`、`MaskToImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、DeepTranslatorTextNode、DrawMaskOnImage、MaskToImage、SAM3_Detect
