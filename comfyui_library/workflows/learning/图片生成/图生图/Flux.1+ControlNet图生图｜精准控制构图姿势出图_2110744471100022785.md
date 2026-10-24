---
key: 图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json
name: Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json
hash: 0634a8614e0ee243
coverage: 0.9375
learned_at: 2026-10-23 10:58:41
nodes: [AIO_Preprocessor, VAEDecode, LoadImage, LoadImage, EmptySD3LatentImage, FluxGuidance, VAELoader, KSampler, UNETLoader, DualCLIPLoader, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, SaveImage, AIO_Preprocessor, LoraLoaderModelOnly, ControlNetApplyAdvanced, ControlNetApplyAdvanced, SetUnionControlNetType, ControlNetLoader, SetUnionControlNetType, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "controlnet_strength": 0.6000000000000001, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1+ControlNet图生图｜精准控制构图姿势出图_2110744471100022785.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `AIO_Preprocessor`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `LoraLoaderModelOnly` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `孤海注释`
- `孤海注释`
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

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（60/64）

**有卡**：`AIO_Preprocessor`、`VAEDecode`、`LoadImage`、`EmptySD3LatentImage`、`FluxGuidance`、`VAELoader`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`、`ControlNetApplyAdvanced`、`SetUnionControlNetType`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
