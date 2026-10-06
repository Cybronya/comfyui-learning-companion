---
key: 图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json
name: Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json
hash: e524efb7e34d1979
coverage: 0.740741
learned_at: 2026-10-06 21:47:15
nodes: [ResolutionSelector, EmptyLatentImage, AIO_Preprocessor, GetImageSize, PreviewImage, PreviewImage, ImageScaleBy, ImageResizeKJv2, LoadImage, LoadImage, ImageResizeKJv2, SaveImage, SeedNode, KSampler, VAEDecode, CLIPLoader, Textbox, Textbox, TextEncodeQwenImage21, UNETLoader, ResizeImageMaskNode, VAELoader, QwenImage21UnionLoader, QwenImage21Cache, QwenImage21UnionApply, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [AIO_Preprocessor, ImageScaleBy, QwenImage21UnionApply, QwenImage21UnionLoader, Textbox, Textbox, GetImageSize, ImageResizeKJv2, ImageResizeKJv2, ResizeImageMaskNode, SeedNode, solarL_SaveImagesToZip, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `AIO_Preprocessor` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21UnionApply` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21UnionLoader` 知识库中没有该节点类型的任何知识, 次要节点 `Textbox` 知识库中没有该节点类型的任何知识, 次要节点 `Textbox` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ResizeImageMaskNode` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `SeedNode` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（81 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`
- `GetImageSize`
- `PreviewImage`
- `PreviewImage`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `SeedNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `Textbox`
- `Textbox`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `ResizeImageMaskNode`
- `VAELoader`
- `QwenImage21UnionLoader`
- `QwenImage21Cache`
- `QwenImage21UnionApply`
- `ComfySwitchNode`
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

覆盖率 **74%**（60/81）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`LoadImage`、`SaveImage`、`KSampler`、`VAEDecode`、`CLIPLoader`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（13）：`AIO_Preprocessor`、`ImageScaleBy`、`QwenImage21UnionApply`、`QwenImage21UnionLoader`、`Textbox`、`Textbox`、`GetImageSize`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`SeedNode`、`solarL_SaveImagesToZip`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `AIO_Preprocessor` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleBy` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21UnionApply` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21UnionLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `Textbox` 知识库中没有该节点类型的任何知识
- 次要节点 `Textbox` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ResizeImageMaskNode` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `SeedNode` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
