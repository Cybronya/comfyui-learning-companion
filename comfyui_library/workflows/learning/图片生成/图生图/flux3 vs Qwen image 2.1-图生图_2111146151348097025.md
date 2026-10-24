---
key: 图片生成/图生图/flux3 vs Qwen image 2.1-图生图_2111146151348097025.json
name: flux3 vs Qwen image 2.1-图生图_2111146151348097025
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux3 vs Qwen image 2.1-图生图_2111146151348097025.json
hash: 3b4027a12eb5563c
coverage: 0.735849
learned_at: 2026-10-23 11:36:43
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, SaveImage, ReferenceMultiLatent, MarkdownNote, ConditioningZeroOut, CreateBoundingBoxes, PreviewAny, MarkdownNote, EmptyFlux2LatentImage, ResolutionSelector, LayerUtility: PurgeVRAM, JjkText, JjkText, JjkText, Note Plus (mtb), Label (rgthree), LoadImage, LoadImage, LoadImage, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, AddLabel, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: PurgeVRAM, VAEDecode, KSampler, TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, JjkText, JjkText, JjkText, EmptyLatentImage, LoadImage, LoadImage, Fast Groups Muter (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, JjkText, JjkText, JjkText]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 144777429357800, "steps": 25, "width": 1024}
---

# 图片生成/图生图/flux3 vs Qwen image 2.1-图生图_2111146151348097025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux3 vs Qwen image 2.1-图生图_2111146151348097025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceMultiLatent`
- `MarkdownNote`
- `ConditioningZeroOut`
- `CreateBoundingBoxes`
- `PreviewAny`
- `MarkdownNote`
- `EmptyFlux2LatentImage`
- `ResolutionSelector`
- `LayerUtility: PurgeVRAM`
- `JjkText`
- `JjkText`
- `JjkText`
- `Note Plus (mtb)`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `AddLabel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `JjkText`
- `JjkText`
- `JjkText`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `JjkText`
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `144777429357800`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（39/53）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`ReferenceMultiLatent`、`ConditioningZeroOut`、`CreateBoundingBoxes`、`EmptyFlux2LatentImage`、`ResolutionSelector`、`LayerUtility: PurgeVRAM`、`Note Plus (mtb)`、`Label (rgthree)`、`LoadImage`、`AddLabel`、`ImageConcatMulti`、`TextEncodeQwenImage21`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
