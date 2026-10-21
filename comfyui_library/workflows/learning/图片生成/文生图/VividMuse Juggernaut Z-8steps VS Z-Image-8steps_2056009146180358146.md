---
key: 图片生成/文生图/VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146.json
name: VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146.json
hash: 8a0a125e2760a8f0
coverage: 0.833333
learned_at: 2026-10-21 02:55:17
nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, VAELoader, KSampler, UNETLoader, EmptyLatentImage, KSampler, PreviewImage, Fast Groups Bypasser (rgthree), VAEDecode, VAEDecode, LayerUtility: ImageReel, SaveImage, PreviewImage, LayerUtility: ImageReelComposit, PreviewImage, SaveImage, easy promptList, PrimitiveStringMultiline, easy promptList, SaveImage, Seed (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2304, "sampler_name": "lcm", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 0, "steps": 8, "width": 1728}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Juggernaut Z-8steps VS Z-Image-8steps_2056009146180358146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `SaveImage`
- `easy promptList`
- `PrimitiveStringMultiline`
- `easy promptList`
- `SaveImage`
- `Seed (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`
- `width` = `1728`
- `height` = `2304`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`LayerUtility: ImageReel`、`SaveImage`、`LayerUtility: ImageReelComposit`、`easy promptList`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
