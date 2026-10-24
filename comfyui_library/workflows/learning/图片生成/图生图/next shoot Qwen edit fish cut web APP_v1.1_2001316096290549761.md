---
key: 图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json
name: next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json
hash: bfee617266a51895
coverage: 1
learned_at: 2026-10-23 11:41:08
nodes: [CFGNorm, ModelSamplingAuraFlow, VAELoader, ImageScaleToTotalPixels, VAEDecode, TextEncodeQwenImageEditPlus, SaveImage, CR Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, KSampler, TextEncodeQwenImageEditPlus, UNETLoader, CR Text, LoadImage, EmptyLatentImage, 图像缩放V2_孤海, CR Text, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 101694691924967, "steps": 8, "width": 1344}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.1_2001316096290549761.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `CR Text`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `图像缩放V2_孤海`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `101694691924967`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1344`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`CLIPLoader`、`KSampler`、`UNETLoader`、`CR Text`、`LoadImage`、`EmptyLatentImage`、`图像缩放V2_孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
