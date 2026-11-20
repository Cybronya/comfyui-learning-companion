---
key: 平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json
name: Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json
hash: 88dfdf2db360a18e
coverage: 0.789474
learned_at: 2026-11-14 00:51:44
nodes: [ImageConcanate, ImageConcanate, KSampler, SaveImage, VAEDecode, SetNode, easy showAnything, RH_LLMAPI_NODE, CheckpointLoaderSimple, GetNode, EmptyLatentImage, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxResolutionNode, Note, LoadImage, LoadImage, Text Multiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v3.safetensors", "denoise": 1, "height": 512, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 1003996827011356, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ImageConcanate`
- `ImageConcanate`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SetNode`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxResolutionNode`
- `Note`
- `LoadImage`
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `1003996827011356`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-v3.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`ImageConcanate`、`KSampler`、`SaveImage`、`VAEDecode`、`RH_LLMAPI_NODE`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`FluxResolutionNode`、`LoadImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、FluxResolutionNode、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
