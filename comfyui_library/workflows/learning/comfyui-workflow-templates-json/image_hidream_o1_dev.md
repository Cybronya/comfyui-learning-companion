---
key: comfyui-workflow-templates-json/image_hidream_o1_dev.json
name: image_hidream_o1_dev
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_hidream_o1_dev.json
hash: d86591629af87e30
official: true
coverage: 0.689655
learned_at: 2026-10-15 22:24:54
nodes: [SamplerCustom, BasicScheduler, CheckpointLoaderSimple, ModelNoiseScale, HiDreamO1ReferenceImages, CLIPTextEncode, VAEDecode, SamplerLCM, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, GetImageSize, PrimitiveBoolean, fa7296b5-c974-4466-bfe3-a1f05f43b880, ComfySwitchNode, PrimitiveBoolean, CLIPTextEncode, MarkdownNote, ImageScaleToTotalPixels, MarkdownNote, LoadImage, ComfyMathExpression, ComfyMathExpression, PreviewAny, EmptyHiDreamO1LatentImage, EmptyHiDreamO1LatentImage, MarkdownNote, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "hidream_o1_image_dev_fp8_scaled.safetensors"}
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

覆盖率 **69%**（20/29）

**有卡**：`SamplerCustom`、`BasicScheduler`、`CheckpointLoaderSimple`、`ModelNoiseScale`、`HiDreamO1ReferenceImages`、`CLIPTextEncode`、`VAEDecode`、`SamplerLCM`、`GetImageSize`、`PrimitiveBoolean`、`fa7296b5-c974-4466-bfe3-a1f05f43b880`、`ImageScaleToTotalPixels`、`LoadImage`、`ComfyMathExpression`、`EmptyHiDreamO1LatentImage`、`SaveImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SamplerCustom、SamplerLCM、EmptyHiDreamO1LatentImage、GetImageSize
