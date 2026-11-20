---
key: 图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json
name: Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json
hash: e81e8107ffb3010e
coverage: 0.916667
learned_at: 2026-11-02 19:12:57
nodes: [LoadImage, UNETLoader, LoraLoaderModelOnly, easy cleanGpuUsed, CLIPLoader, VAELoader, VAEDecode, KSampler, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, ImageBlur]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1075728970595720, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `ImageBlur`

## 关键参数

- `seed` = `1075728970595720`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`ImageBlur`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
