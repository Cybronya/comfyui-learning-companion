---
key: 图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json
name: Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json
hash: c91c481d77e6b31e
coverage: 0.797468
learned_at: 2026-10-07 02:27:59
nodes: [VAELoader, SetNode, EmptyLatentImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy imageSize, GetNode, Any Switch (rgthree), Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, ComfySwitchNode, GetNode, ImageScaleBy, CLIPLoader, ResolutionSelector, TextEncodeQwenImage21, UNETLoader, VAEDecode, SaveImage, QwenImage21Cache, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, VAEDecode, ImageConcatMulti, SaveImage, SaveImage, LoraLoaderModelOnly, KSampler, KSampler, Fast Groups Bypasser (rgthree), SaveImage, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [ImageResize+, ImageResize+, easy imageSize, easy imageSize]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图图生视频高清工作流合集V2，多场景覆盖方案_2103548965714223106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `VAELoader`
- `SetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **80%**（63/79）

**有卡**：`VAELoader`、`EmptyLatentImage`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（4）：`ImageResize+`、`ImageResize+`、`easy imageSize`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
