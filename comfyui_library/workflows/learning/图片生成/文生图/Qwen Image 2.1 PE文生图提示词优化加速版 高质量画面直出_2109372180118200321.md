---
key: 图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json
name: Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json
hash: 08ec2fdfcbddc4c5
coverage: 0.8125
learned_at: 2026-10-21 02:54:04
nodes: [SaveImage, QwenImage21_T2IPromptRewrite, easy showAnything, easy showAnything, PreviewImage, SaveImageAdvanced, VAEDecode, KSampler, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, PrimitiveStringMultiline, CLIPLoader, UNETLoader, RH_QwenImagePromptEnhancer, ComfySwitchNode, PrimitiveBoolean, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE文生图提示词优化加速版 高质量画面直出_2109372180118200321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `SaveImage`
- `QwenImage21_T2IPromptRewrite`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RH_QwenImagePromptEnhancer`
- `ComfySwitchNode`
- `PrimitiveBoolean`
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

覆盖率 **81%**（39/48）

**有卡**：`SaveImage`、`QwenImage21_T2IPromptRewrite`、`SaveImageAdvanced`、`VAEDecode`、`KSampler`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`UNETLoader`、`RH_QwenImagePromptEnhancer`、`PrimitiveBoolean`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
