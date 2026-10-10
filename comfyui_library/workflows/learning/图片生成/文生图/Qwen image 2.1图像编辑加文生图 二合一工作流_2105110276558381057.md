---
key: Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json
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

# Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `EmptyLatentImage` ★核心
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
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `GetNode`
- `VAEDecode` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `Seed (rgthree)`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `PrimitiveStringMultiline`
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

覆盖率 **69%**（64/93）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`ResolutionSelector`、`VAEDecode`、`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`TextGenerateLTX2Prompt`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
