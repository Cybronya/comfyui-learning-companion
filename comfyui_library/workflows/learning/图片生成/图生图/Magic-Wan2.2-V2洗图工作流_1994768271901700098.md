---
key: 图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json
name: Magic-Wan2.2-V2洗图工作流_1994768271901700098
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json
hash: 0a14a10e712848ea
coverage: 1
learned_at: 2026-10-23 11:09:16
nodes: [VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, VAEEncode, CLIPTextEncode, SaveImage, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.23000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 1016888976448451, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1016888976448451`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.23000000000000004`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`SaveImage`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
