---
key: 图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json
name: Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json
hash: f8ec11fa75314b05
coverage: 1
learned_at: 2026-10-10 20:58:58
nodes: [VAEDecode, CLIPTextEncode, VAELoader, SaveImage, ModelSamplingAuraFlow, EmptyLatentImage, UNETLoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1248, "sampler_name": "euler", "scheduler": "simple", "seed": 527660888760163, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json`

## 结构

**节点**（11 个）：
- `VAEDecode`
- `CLIPTextEncode`
- `VAELoader`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `EmptyLatentImage`
- `UNETLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1248`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `527660888760163`
- `steps` = `4`
- `width` = `1024`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`SaveImage`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
