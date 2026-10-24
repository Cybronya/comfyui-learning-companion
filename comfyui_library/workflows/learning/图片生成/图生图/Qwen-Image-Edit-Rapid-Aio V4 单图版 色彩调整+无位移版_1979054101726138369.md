---
key: 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json
name: Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json
hash: 1e3200aeca087ba2
coverage: 0.928571
learned_at: 2026-10-23 11:17:00
nodes: [CR Text, SaveImage, LoadImage, LoadImage, CheckpointLoaderSimple, KSampler, CR Text Concatenate, VAEDecode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus_lrzjason, Image Comparer (rgthree), ColorMatch, LoadImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v4.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 528992163119291, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CR Text`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `CR Text Concatenate`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `Image Comparer (rgthree)`
- `ColorMatch`
- `LoadImage`
- `CR Text`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-v4.safetensors`
- `seed` = `528992163119291`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CR Text`、`SaveImage`、`LoadImage`、`CheckpointLoaderSimple`、`KSampler`、`CR Text Concatenate`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEditPlus_lrzjason`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEditPlus、TextEncodeQwenImageEditPlus_lrzjason、SaveImage、ColorMatch

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
