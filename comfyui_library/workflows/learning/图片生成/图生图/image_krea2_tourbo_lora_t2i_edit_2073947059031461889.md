---
key: 图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json
name: image_krea2_tourbo_lora_t2i_edit_2073947059031461889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json
hash: 5dfa7461cf2cc471
coverage: 0.6875
learned_at: 2026-10-23 11:37:52
nodes: [MarkdownNote, MarkdownNote, StringConcatenate, ComfySwitchNode, StringConcatenate, TextGenerate, ComfySwitchNode, MarkdownNote, PreviewAny, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, SaveImage, SAMLoader, UltralyticsDetectorProvider, FaceDetailer, PrimitiveStringMultiline, PrimitiveBoolean, UNETLoader, PrimitiveBoolean, VAELoader, VAEEncode, PrimitiveStringMultiline, VAEDecode, PreviewImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.7500000000000001, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 457637799974048, "steps": 8, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `MarkdownNote`
- `MarkdownNote`
- `StringConcatenate`
- `ComfySwitchNode`
- `StringConcatenate`
- `TextGenerate`
- `ComfySwitchNode`
- `MarkdownNote`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `FaceDetailer`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `VAELoader`
- `VAEEncode` ★核心
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `457637799974048`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7500000000000001`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`StringConcatenate`、`TextGenerate`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`SaveImage`、`SAMLoader`、`UltralyticsDetectorProvider`、`FaceDetailer`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`VAEEncode`、`VAEDecode`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
