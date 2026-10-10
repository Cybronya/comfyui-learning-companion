---
key: 图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json
name: Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json
hash: 01e165b4c08a3c59
coverage: 0.82
learned_at: 2026-10-10 20:48:07
nodes: [CLIPLoader, VAEDecode, UNETLoader, VAELoader, LoraLoaderModelOnly, SaveImage, PreviewImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, PrimitiveStringMultiline, EmptyLatentImage, TextEncodeQwenImage21, KSampler, ConditioningKrea2Rebalance, WujiUpscaler2, LoadImage, Fast Groups Bypasser (rgthree), RH_Screenwriter, WujiImagePrompt, easy showAnything, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [WujiImagePrompt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `WujiImagePrompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ConditioningKrea2Rebalance`
- `WujiUpscaler2`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `RH_Screenwriter`
- `WujiImagePrompt`
- `easy showAnything`
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

覆盖率 **82%**（41/50）

**有卡**：`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ConditioningKrea2Rebalance`、`WujiUpscaler2`、`LoadImage`、`RH_Screenwriter`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`WujiImagePrompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `WujiImagePrompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
