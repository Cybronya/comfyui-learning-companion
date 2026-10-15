---
key: 图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json
name: Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json
hash: 299bb3ba68a3297c
coverage: 0.826087
learned_at: 2026-10-15 22:27:27
nodes: [SaveImage, CLIPLoader, UNETLoader, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, SaveImage, ImageConcatMulti, PreviewImage, VAEDecode, KSampler, ControlNetLoader, EmptySD3LatentImage, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LoraLoaderModelOnly, AIO_Preprocessor, SetUnionControlNetType, LoadImage, ControlNetApplySD3, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.5, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 52738987569456, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_instantX_Controlnet_Union工作流1.0_1974331826225459201.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `52738987569456`
- `steps` = `8`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.75`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`SaveImage`、`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`ImageConcatMulti`、`VAEDecode`、`KSampler`、`ControlNetLoader`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`SetUnionControlNetType`、`LoadImage`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
