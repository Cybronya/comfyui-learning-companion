---
key: 图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json
name: Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json
hash: d98161b19ceee245
coverage: 0.916667
learned_at: 2026-10-10 20:59:10
nodes: [KSampler, ControlNetApplyAdvanced, DWPreprocessor, PreviewImage, SetShakkerLabsUnionControlNetType, UNETLoader, DualCLIPLoader, LoraLoader, VAEDecode, ControlNetLoader, StyleModelLoader, EmptyLatentImage, CLIPVisionEncode, CLIPVisionLoader, VAELoader, CLIPTextEncode, RH_Captioner, LoraLoader, CLIPTextEncodeFlux, ShowText|pysssss, SaveImage, LoadImage, LoadImage, StyleModelApply]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1019313570362968, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
---

# 图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json`

## 结构

**节点**（24 个）：
- `KSampler`
- `ControlNetApplyAdvanced`
- `DWPreprocessor`
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoader`
- `VAEDecode`
- `ControlNetLoader`
- `StyleModelLoader`
- `EmptyLatentImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPTextEncode`
- `RH_Captioner`
- `LoraLoader`
- `CLIPTextEncodeFlux`
- `ShowText|pysssss`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `StyleModelApply`

**识别到的模式**：text_to_image、lora

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `denoise` = `1`
- `height` = `1536`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1019313570362968`
- `steps` = `20`
- `strength_clip` = `1`
- `strength_model` = `0.8`
- `width` = `1024`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`KSampler`、`ControlNetApplyAdvanced`、`DWPreprocessor`、`PreviewImage`、`SetShakkerLabsUnionControlNetType`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`VAEDecode`、`ControlNetLoader`、`StyleModelLoader`、`EmptyLatentImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPTextEncode`、`RH_Captioner`、`CLIPTextEncodeFlux`、`ShowText|pysssss`、`SaveImage`、`LoadImage`
