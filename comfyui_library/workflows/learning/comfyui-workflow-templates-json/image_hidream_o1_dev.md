---
key: comfyui-workflow-templates-json/image_hidream_o1_dev.json
name: image_hidream_o1_dev
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_hidream_o1_dev.json
hash: d86591629af87e30
official: true
coverage: 0.655172
learned_at: 2026-10-07 21:35:44
nodes: [SamplerCustom, BasicScheduler, CheckpointLoaderSimple, ModelNoiseScale, HiDreamO1ReferenceImages, CLIPTextEncode, VAEDecode, SamplerLCM, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, GetImageSize, PrimitiveBoolean, fa7296b5-c974-4466-bfe3-a1f05f43b880, ComfySwitchNode, PrimitiveBoolean, CLIPTextEncode, MarkdownNote, ImageScaleToTotalPixels, MarkdownNote, LoadImage, ComfyMathExpression, ComfyMathExpression, PreviewAny, EmptyHiDreamO1LatentImage, EmptyHiDreamO1LatentImage, MarkdownNote, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: [fa7296b5-c974-4466-bfe3-a1f05f43b880]
parameters: {"checkpoint": "hidream_o1_image_dev_fp8_scaled.safetensors"}
discoveries: [次要节点 `fa7296b5-c974-4466-bfe3-a1f05f43b880` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_hidream_o1_dev.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_hidream_o1_dev.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `SamplerCustom` ★核心
- `BasicScheduler`
- `CheckpointLoaderSimple` ★核心
- `ModelNoiseScale`
- `HiDreamO1ReferenceImages`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SamplerLCM` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetImageSize`
- `PrimitiveBoolean`
- `fa7296b5-c974-4466-bfe3-a1f05f43b880`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `LoadImage`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `EmptyHiDreamO1LatentImage`
- `EmptyHiDreamO1LatentImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `SaveImage`

## 关键参数

- `checkpoint` = `hidream_o1_image_dev_fp8_scaled.safetensors`

## 知识

覆盖率 **66%**（19/29）

**有卡**：`SamplerCustom`、`BasicScheduler`、`CheckpointLoaderSimple`、`ModelNoiseScale`、`HiDreamO1ReferenceImages`、`CLIPTextEncode`、`VAEDecode`、`SamplerLCM`、`GetImageSize`、`PrimitiveBoolean`、`ImageScaleToTotalPixels`、`LoadImage`、`ComfyMathExpression`、`EmptyHiDreamO1LatentImage`、`SaveImage`

**缺卡**（1）：`fa7296b5-c974-4466-bfe3-a1f05f43b880`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SamplerCustom、SamplerLCM、EmptyHiDreamO1LatentImage、GetImageSize

## 学习发现

- 次要节点 `fa7296b5-c974-4466-bfe3-a1f05f43b880` 知识库中没有该节点类型的任何知识
