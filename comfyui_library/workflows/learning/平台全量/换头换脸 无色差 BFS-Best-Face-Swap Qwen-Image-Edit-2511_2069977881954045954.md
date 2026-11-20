---
key: 平台全量/换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954.json
name: 换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954.json
hash: 94eb6a9dc897e577
coverage: 0.863636
learned_at: 2026-11-14 02:07:32
nodes: [CFGNorm, TextEncodeQwenImageEditPlus, Anything Everywhere3, Note, UNETLoader, VAELoader, CLIPLoader, KSampler, VAEDecode, ImageConcatMulti, ImageConcatMulti, LoraLoader, LoraLoader, TextEncodeQwenImageEditPlus, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio, ModelSamplingAuraFlow, EmptySD3LatentImage, PreviewImage, SaveImage, LoadImage, LoadImage]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Qwen-Image-Edit-2511-Lightning-8steps_V1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 31440, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954.json

> 来源文件 `comfyui_library/workflows/平台全量/换头换脸 无色差 BFS-Best-Face-Swap Qwen-Image-Edit-2511_2069977881954045954.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `Anything Everywhere3`
- `Note`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `31440`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Qwen-Image-Edit-2511-Lightning-8steps_V1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`CFGNorm`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`ImageConcatMulti`、`LoraLoader`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGNorm、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
