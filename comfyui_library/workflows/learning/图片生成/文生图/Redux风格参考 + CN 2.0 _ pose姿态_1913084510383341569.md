---
key: 图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json
name: Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json
hash: d98161b19ceee245
coverage: 0.916667
learned_at: 2026-10-07 19:46:12
nodes: [KSampler, ControlNetApplyAdvanced, DWPreprocessor, PreviewImage, SetShakkerLabsUnionControlNetType, UNETLoader, DualCLIPLoader, LoraLoader, VAEDecode, ControlNetLoader, StyleModelLoader, EmptyLatentImage, CLIPVisionEncode, CLIPVisionLoader, VAELoader, CLIPTextEncode, RH_Captioner, LoraLoader, CLIPTextEncodeFlux, ShowText|pysssss, SaveImage, LoadImage, LoadImage, StyleModelApply]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "秋日森林_秋天女孩_V1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1019313570362968, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
---

# 图片生成/文生图/Redux风格参考 + CN 2.0 _ pose姿态_1913084510383341569.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1913084510383341569.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（24 个）：
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `DWPreprocessor`
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `ControlNetLoader`
- `StyleModelLoader`
- `EmptyLatentImage` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `LoraLoader` ★核心
- `CLIPTextEncodeFlux` ★核心
- `ShowText|pysssss`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `StyleModelApply`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `1019313570362968`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `lora_name` = `秋日森林_秋天女孩_V1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`KSampler`、`ControlNetApplyAdvanced`、`DWPreprocessor`、`SetShakkerLabsUnionControlNetType`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`VAEDecode`、`ControlNetLoader`、`StyleModelLoader`、`EmptyLatentImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`VAELoader`、`CLIPTextEncode`、`RH_Captioner`、`CLIPTextEncodeFlux`、`SaveImage`、`LoadImage`、`StyleModelApply`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
