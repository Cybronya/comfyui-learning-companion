---
key: 平台全量/Wan2.2 Remix 图生视频_1987154917611778049.json
name: Wan2.2 Remix 图生视频_1987154917611778049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Remix 图生视频_1987154917611778049.json
hash: 0ba76e011a54e104
coverage: 1
learned_at: 2026-11-14 01:05:31
nodes: [CLIPLoader, INTConstant, VAELoader, INTConstant, INTConstant, SimpleMath+, LoadImage, ImageResizeKJv2, CR Text, Wan22PromptSelector, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, Text Concatenate, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, WanImageToVideo, CLIPVisionEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 平台全量/Wan2.2 Remix 图生视频_1987154917611778049.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Remix 图生视频_1987154917611778049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `CLIPLoader`
- `INTConstant`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `LoadImage`
- `ImageResizeKJv2`
- `CR Text`
- `Wan22PromptSelector`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Text Concatenate`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CLIPLoader`、`INTConstant`、`VAELoader`、`SimpleMath+`、`LoadImage`、`ImageResizeKJv2`、`CR Text`、`Wan22PromptSelector`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPVisionLoader`、`ModelSamplingSD3`、`UNETLoader`、`Text Concatenate`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`WanImageToVideo`、`CLIPVisionEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
