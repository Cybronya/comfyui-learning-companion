---
key: 图片生成/文生图/wan2.1超真实文生图 特写皮肤细节拉满_1949347197003997185.json
name: wan2.1超真实文生图 特写皮肤细节拉满_1949347197003997185
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1超真实文生图 特写皮肤细节拉满_1949347197003997185.json
hash: d4e8390db7a7bae9
coverage: 0.666667
learned_at: 2026-10-10 20:59:27
nodes: [CLIPTextEncode, CLIPTextEncode, UNETLoader, VAELoader, VAEDecode, SaveImage, MarkdownNote, CLIPLoader, MarkdownNote, MarkdownNote, MarkdownNote, KSampler, ttN concat, MarkdownNote, LoraLoader, LoraLoader, LoraLoader, easy showAnything, Image_Resize, LoadImage, EmptyHunyuanLatentVideo, LoadImage, VAEEncode, LayerUtility: ZhipuGLM4V]
patterns: [image_to_image, lora]
missing: [LayerUtility: ZhipuGLM4V, ttN concat]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1234567890, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `LayerUtility: ZhipuGLM4V` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1超真实文生图 特写皮肤细节拉满_1949347197003997185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1超真实文生图 特写皮肤细节拉满_1949347197003997185.json`

## 结构

**节点**（24 个）：
- `CLIPTextEncode`
- `CLIPTextEncode`
- `UNETLoader`
- `VAELoader`
- `VAEDecode`
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler`
- `ttN concat`
- `MarkdownNote`
- `LoraLoader`
- `LoraLoader`
- `LoraLoader`
- `easy showAnything`
- `Image_Resize`
- `LoadImage`
- `EmptyHunyuanLatentVideo`
- `LoadImage`
- `VAEEncode`
- `LayerUtility: ZhipuGLM4V`

**识别到的模式**：image_to_image、lora

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `1234567890`
- `steps` = `8`
- `strength_clip` = `1.0000000000000002`
- `strength_model` = `1.0000000000000002`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`MarkdownNote`、`CLIPLoader`、`KSampler`、`ttN concat`、`LoraLoader`

**缺卡**（2）：`LayerUtility: ZhipuGLM4V`、`ttN concat`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ZhipuGLM4V` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
