---
key: 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json
name: Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json
hash: 85c4281b9147d845
coverage: 0.772727
learned_at: 2026-10-06 21:49:07
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, SaveImage, CLIPLoader, EmptyLatentImage, TextGenerate, VAEDecode, PreviewImage, ResolutionSelector, PreviewAny, CR Prompt Text, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [TextGenerate, CR Prompt Text, CR Prompt Text, PreviewAny, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextGenerate`
- `VAEDecode` ★核心
- `PreviewImage`
- `ResolutionSelector`
- `PreviewAny`
- `CR Prompt Text`
- `CR Prompt Text`
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

覆盖率 **77%**（34/44）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`EmptyLatentImage`、`VAEDecode`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（5）：`TextGenerate`、`CR Prompt Text`、`CR Prompt Text`、`PreviewAny`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
