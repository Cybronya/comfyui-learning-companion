---
key: 图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json
name: WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json
hash: 0476692583263eb8
coverage: 1
learned_at: 2026-10-23 11:27:30
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, SaveImage, KSampler, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEEncode, easy float]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 571926027203342, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `easy float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `571926027203342`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`KSampler`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`easy float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
