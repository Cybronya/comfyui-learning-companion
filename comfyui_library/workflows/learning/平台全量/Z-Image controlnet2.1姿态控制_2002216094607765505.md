---
key: 平台全量/Z-Image controlnet2.1姿态控制_2002216094607765505.json
name: Z-Image controlnet2.1姿态控制_2002216094607765505
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-Image controlnet2.1姿态控制_2002216094607765505.json
hash: 1339a4f38fea3073
coverage: 0.909091
learned_at: 2026-11-14 01:08:07
nodes: [KSampler, EmptyLatentImage, GetImage, ConditioningZeroOut, PreviewImage, workflow>Z-image, CLIPTextEncode, LoadImage, workflow>Controlnet, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "dpmpp_sde", "scheduler": "beta", "seed": 351714325728882, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Z-Image controlnet2.1姿态控制_2002216094607765505.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-Image controlnet2.1姿态控制_2002216094607765505.json`

## 结构

**生成流程**：Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `GetImage`
- `ConditioningZeroOut`
- `PreviewImage`
- `workflow>Z-image`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `workflow>Controlnet`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `351714325728882`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`KSampler`、`EmptyLatentImage`、`GetImage`、`ConditioningZeroOut`、`workflow>Z-image`、`CLIPTextEncode`、`LoadImage`、`workflow>Controlnet`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、workflow>controlnet、workflow>Controlnet

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
