---
key: 数字人/数字人/Sam3.1 高质量语义分割工作流_2053001590621130754.json
name: Sam3.1 高质量语义分割工作流_2053001590621130754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Sam3.1 高质量语义分割工作流_2053001590621130754.json
hash: 7b1f6db3e5ff5714
coverage: 0.875
learned_at: 2026-10-26 01:57:14
nodes: [CLIPTextEncode, RunningHub Void Point Editor, CheckpointLoaderSimple, MaskComposite, MaskToImage, ImageCompositeMasked, RunningHub Void Mask Reasoner, SaveVideo, DeepTranslatorTextNode, SAM3_Detect, PointsEditor, easy showAnything, SaveImage, SaveImage, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 数字人/数字人/Sam3.1 高质量语义分割工作流_2053001590621130754.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Sam3.1 高质量语义分割工作流_2053001590621130754.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `RunningHub Void Point Editor`
- `CheckpointLoaderSimple` ★核心
- `MaskComposite`
- `MaskToImage`
- `ImageCompositeMasked`
- `RunningHub Void Mask Reasoner`
- `SaveVideo`
- `DeepTranslatorTextNode`
- `SAM3_Detect`
- `PointsEditor`
- `easy showAnything`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPTextEncode`、`RunningHub Void Point Editor`、`CheckpointLoaderSimple`、`MaskComposite`、`MaskToImage`、`ImageCompositeMasked`、`RunningHub Void Mask Reasoner`、`SaveVideo`、`DeepTranslatorTextNode`、`SAM3_Detect`、`PointsEditor`、`SaveImage`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、SaveVideo、ImageCompositeMasked、MaskToImage、PointsEditor
