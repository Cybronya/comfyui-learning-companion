---
key: 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json
name: Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json
hash: e24b8a4102684f54
coverage: 0.703704
learned_at: 2026-10-07 02:27:48
nodes: [Label (rgthree), VAELoader, Note, SetNode, EmptyLatentImage, SetNode, MarkdownNote, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, ComfySwitchNode, GetNode, ImageScaleBy, CLIPLoader, ResolutionSelector, Label (rgthree), TextEncodeQwenImage21, UNETLoader, VAEDecode, SaveImage, QwenImage21Cache, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, VAEDecode, ImageConcatMulti, SaveImage, SaveImage, LoraLoaderModelOnly, KSampler, KSampler, Fast Groups Bypasser (rgthree), SaveImage, LoraLoaderModelOnly]
patterns: []
missing: [Label (rgthree), Label (rgthree), ImageResize+, ImageResize+, easy imageSize, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 4, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `Label (rgthree)`
- `VAELoader`
- `Note`
- `SetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `MarkdownNote`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy imageSize`
- `GetNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfySwitchNode`
- `GetNode`
- `ImageScaleBy`
- `CLIPLoader`
- `ResolutionSelector`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（38/54）

**有卡**：`VAELoader`、`EmptyLatentImage`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`KSampler`

**缺卡**（6）：`Label (rgthree)`、`Label (rgthree)`、`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
