---
key: 图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json
name: Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json
hash: 016f1bb0d2dab63b
coverage: 0.688172
learned_at: 2026-10-10 20:58:57
nodes: [EmptyLatentImage, PrimitiveBoolean, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, BatchImagesNode, ImageScaleToTotalPixels, EmptyLatentImage, ResolutionSelector, ResolutionSelector, GetNode, VAEDecode, GetNode, GetNode, ComfySwitchNode, GetNode, Seed (rgthree), GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, QwenImage21Cache, SetNode, SetNode, PrimitiveStringMultiline, CLIPLoader, SetNode, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, VAEDecode, Image Comparer (rgthree), SaveImage, KSampler, TextEncodeQwenImage21, TextEncodeQwenImage21, SaveImage, Seed (rgthree), KSampler, UNETLoader, easy showAnything, easy showAnything, PrimitiveStringMultiline, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, GetNode, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json`

## 结构

**节点**（93 个）：
- `EmptyLatentImage`
- `PrimitiveBoolean`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `EmptyLatentImage`
- `ResolutionSelector`
- `ResolutionSelector`
- `GetNode`
- `VAEDecode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `Seed (rgthree)`
- `KSampler`
- `UNETLoader`
- `easy showAnything`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **69%**（64/93）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`ResolutionSelector`、`GetNode`、`VAEDecode`、`ComfySwitchNode`、`Seed (rgthree)`、`SetNode`、`VAELoader`、`QwenImage21Cache`、`PrimitiveStringMultiline`、`CLIPLoader`、`LoraLoaderModelOnly`、`Fast Groups Bypasser (rgthree)`、`Image Comparer (rgthree)`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`easy showAnything`、`TextGenerateLTX2Prompt`

**缺卡**（2）：`Seed (rgthree)`、`Seed (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
