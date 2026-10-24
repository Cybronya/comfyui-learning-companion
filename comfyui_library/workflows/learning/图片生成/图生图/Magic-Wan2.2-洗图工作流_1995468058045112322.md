---
key: 图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json
name: Magic-Wan2.2-洗图工作流_1995468058045112322
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json
hash: 7a47aae5907f9c17
coverage: 1
learned_at: 2026-10-23 11:09:16
nodes: [VAEDecode, CLIPLoader, VAELoader, SaveImage, UNETLoader, LoraLoaderModelOnly, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, CLIPTextEncode, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 1045648862493228, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1045648862493228`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
