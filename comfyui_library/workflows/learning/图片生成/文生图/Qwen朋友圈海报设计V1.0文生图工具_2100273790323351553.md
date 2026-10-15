---
key: 图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json
name: Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json
hash: b17315fddf50057c
coverage: 0.883721
learned_at: 2026-10-10 20:59:10
nodes: [ModelSamplingAuraFlow, UpscaleModelLoader, UltimateSDUpscale, PreviewImage, CLIPTextEncode, VAEDecode, CLIPTextEncode, EmptySD3LatentImage, VAELoader, UNETLoader, CLIPLoader, LoraLoader, SaveImage, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "lora_name": "Qwen-Image 3D IP XIAOXIAOloRA.safetensors", "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "strength_clip": 0.8000000000000002, "strength_model": 0.8000000000000002, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json`

## 结构

**节点**（43 个）：
- `ModelSamplingAuraFlow`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `PreviewImage`
- `CLIPTextEncode`
- `VAEDecode`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `VAELoader`
- `UNETLoader`
- `CLIPLoader`
- `LoraLoader`
- `SaveImage`
- `KSampler`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、lora

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `lora_name` = `Qwen-Image 3D IP XIAOXIAOloRA.safetensors`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `strength_clip` = `0.8000000000000002`
- `strength_model` = `0.8000000000000002`
- `width` = `80`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`ModelSamplingAuraFlow`、`UpscaleModelLoader`、`UltimateSDUpscale`、`PreviewImage`、`CLIPTextEncode`、`VAEDecode`、`EmptySD3LatentImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`SaveImage`、`KSampler`、`孤海注释`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
