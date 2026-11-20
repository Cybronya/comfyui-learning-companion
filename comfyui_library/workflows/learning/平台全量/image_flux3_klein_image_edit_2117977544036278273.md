---
key: 平台全量/image_flux3_klein_image_edit_2117977544036278273.json
name: image_flux3_klein_image_edit_2117977544036278273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/image_flux3_klein_image_edit_2117977544036278273.json
hash: 204239b64650cf12
coverage: 0.533333
learned_at: 2026-11-14 01:12:41
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, SaveImage, MarkdownNote, ReferenceMultiLatent, MarkdownNote, PreviewAny, MarkdownNote, EmptyFlux2LatentImage, CLIPLoader, TextGenerate, PrimitiveStringMultiline, Flux3LayoutPrompt, BatchImagesNode, ComfySwitchNode, PreviewAny, LoadImage, CreateBoundingBoxes, CLIPTextEncode, UNETLoader, LoadImage, LoadImage, ResolutionSelector, SetNode, SetNode, GetNode, GetNode, PrimitiveBoolean, SetNode, GetNode, ComfySwitchNode, PrimitiveInt, SetNode, GetNode, CR Prompt Text, CR Prompt Text, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 227455791406022, "steps": 50}
---

# 平台全量/image_flux3_klein_image_edit_2117977544036278273.json

> 来源文件 `comfyui_library/workflows/平台全量/image_flux3_klein_image_edit_2117977544036278273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `ReferenceMultiLatent`
- `MarkdownNote`
- `PreviewAny`
- `MarkdownNote`
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `Flux3LayoutPrompt`
- `BatchImagesNode`
- `ComfySwitchNode`
- `PreviewAny`
- `LoadImage`
- `CreateBoundingBoxes`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `227455791406022`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **53%**（24/45）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`ReferenceMultiLatent`、`EmptyFlux2LatentImage`、`TextGenerate`、`Flux3LayoutPrompt`、`BatchImagesNode`、`LoadImage`、`CreateBoundingBoxes`、`UNETLoader`、`ResolutionSelector`、`PrimitiveBoolean`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ResolutionSelector、LoadImage
