---
key: 图片生成/图生图/三参考图生图｜Qwen-Eidt-2511+SeedVR2.5角色一致性分镜出图_2092132709794664449.json
name: 三参考图生图｜Qwen-Eidt-2511+SeedVR2.5角色一致性分镜出图_2092132709794664449
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三参考图生图｜Qwen-Eidt-2511+SeedVR2.5角色一致性分镜出图_2092132709794664449.json
hash: cddc886fc8c7ecd5
coverage: 0.86
learned_at: 2026-10-23 12:01:45
nodes: [LoadImage, CLIPLoader, UNETLoader, LoraLoaderModelOnly, FluxKontextMultiReferenceLatentMethod, EmptyLatentImage, CR Text, LoadImage, LoadImage, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, TextEncodeQwenImageEditPlus, ImageConcatMulti, VAELoader, KSampler, WujiCleaner, VAEDecode, WujiUpscaler, ImageConcanate, SaveImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/三参考图生图｜Qwen-Eidt-2511+SeedVR2.5角色一致性分镜出图_2092132709794664449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三参考图生图｜Qwen-Eidt-2511+SeedVR2.5角色一致性分镜出图_2092132709794664449.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `EmptyLatentImage` ★核心
- `CR Text`
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `ImageConcatMulti`
- `VAELoader`
- `KSampler` ★核心
- `WujiCleaner`
- `VAEDecode` ★核心
- `WujiUpscaler`
- `ImageConcanate`
- `SaveImage`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **86%**（43/50）

**有卡**：`LoadImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`FluxKontextMultiReferenceLatentMethod`、`EmptyLatentImage`、`CR Text`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`ImageConcatMulti`、`VAELoader`、`KSampler`、`WujiCleaner`、`VAEDecode`、`WujiUpscaler`、`ImageConcanate`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
