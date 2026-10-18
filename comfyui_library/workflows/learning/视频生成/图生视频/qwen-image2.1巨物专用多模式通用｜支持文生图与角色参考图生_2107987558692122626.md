---
key: 视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json
name: qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json
hash: a845670fdd01bd71
coverage: 0.890625
learned_at: 2026-10-17 22:19:17
nodes: [CLIPLoader, VAEDecode, UNETLoader, VAELoader, LoraLoaderModelOnly, SaveImage, PreviewImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, PrimitiveStringMultiline, EmptyLatentImage, TextEncodeQwenImage21, KSampler, ConditioningKrea2Rebalance, WujiUpscaler2, LoadImage, Fast Groups Bypasser (rgthree), RH_Screenwriter, WujiImagePrompt, easy showAnything, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **89%**（57/64）

**有卡**：`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ConditioningKrea2Rebalance`、`WujiUpscaler2`、`LoadImage`、`RH_Screenwriter`、`WujiImagePrompt`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
