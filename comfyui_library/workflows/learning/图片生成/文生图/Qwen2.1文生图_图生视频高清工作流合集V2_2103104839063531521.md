---
key: 图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json
name: Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_图生视频高清工作流合集V2_2103104839063531521.json
hash: e24b8a4102684f54
coverage: 0.703704
learned_at: 2026-10-10 20:59:06
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

**节点**（54 个）：
- `Label (rgthree)`
- `VAELoader`
- `Note`
- `SetNode`
- `EmptyLatentImage`
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
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `KSampler`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LoraLoaderModelOnly`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `999`
- `steps` = `4`
- `width` = `1024`

## 知识

覆盖率 **70%**（38/54）

**有卡**：`Label (rgthree)`、`VAELoader`、`Note`、`SetNode`、`EmptyLatentImage`、`MarkdownNote`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageSize`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`GetNode`、`Any Switch (rgthree)`、`Image Comparer (rgthree)`、`LoadImage`、`ComfySwitchNode`、`CLIPLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`

**缺卡**（6）：`Label (rgthree)`、`Label (rgthree)`、`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`

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
