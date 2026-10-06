---
key: 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json
name: qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json
hash: c973afac4aec3849
coverage: 0.725
learned_at: 2026-10-06 21:50:10
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveInt, PreviewAny, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, QwenImage21Cache, ModelAttentionBackend, CLIPLoader, TextGenerate, CLIPLoader, PrimitiveStringMultiline, GetImageSize, Any Switch (rgthree), TextEncodeQwenImage21, ImageResizeKJv2, VAEDecode, Image Comparer (rgthree), LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [BatchImagesNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, ModelAttentionBackend, PrimitiveBoolean, TextGenerate, TextGenerate, GetImageSize, ImageResizeKJv2, PreviewAny, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1多功能官流整合｜文生图图生图一套全搞定_2106233388154839041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（80 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `CLIPLoader`
- `TextGenerate`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **72%**（58/80）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（11）：`BatchImagesNode`、`Fast Groups Bypasser (rgthree)`、`ImageScaleToTotalPixels`、`ModelAttentionBackend`、`PrimitiveBoolean`、`TextGenerate`、`TextGenerate`、`GetImageSize`、`ImageResizeKJv2`、`PreviewAny`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
