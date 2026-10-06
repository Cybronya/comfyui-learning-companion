---
key: 图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json
name: Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json
hash: 42a451db807a3f6c
coverage: 0.735849
learned_at: 2026-10-06 21:48:42
nodes: [VAELoader, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, GetNode, VAEDecode, SetNode, KSampler, AnySwitch, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, TextEncodeQwenImage21, LoadImage, LoadImage, SaveImage, LoadImage, ResolutionSelector, Image Comparer (rgthree), LoadImage, Text Multiline, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: [AnySwitch, ImageScaleToTotalPixels, Text Multiline, Text Multiline, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `AnySwitch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图像编辑综合工作流，一站式创作新方案_2106507657149509633.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `VAELoader`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `KSampler` ★核心
- `AnySwitch`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Text Multiline`
- `LoadImage`
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（39/53）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（5）：`AnySwitch`、`ImageScaleToTotalPixels`、`Text Multiline`、`Text Multiline`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `AnySwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
