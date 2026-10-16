---
key: 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json
name: Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1984504641570357250.json
hash: 98bcdc2891879569
coverage: 0.857143
learned_at: 2026-10-15 22:32:48
nodes: [easy cleanGpuUsed, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAEDecode, SetNode, KSamplerAdvanced, GetNode, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, VAELoader, ImageResize+, Note, Note, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, LoadImage, Qwen3_VQA, MultiplePathsInput, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, WanFirstLastFrameToVideo, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix Wan2.2-首尾帧 官方版_RH网_1984504641570357250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984504641570357250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ImageResize+`
- `Note`
- `Note`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `LoadImage`
- `Qwen3_VQA`
- `MultiplePathsInput`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `Text Multiline`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`easy cleanGpuUsed`、`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAEDecode`、`KSamplerAdvanced`、`CLIPTextEncode`、`VAELoader`、`ImageResize+`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LoadImage`、`Qwen3_VQA`、`MultiplePathsInput`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
