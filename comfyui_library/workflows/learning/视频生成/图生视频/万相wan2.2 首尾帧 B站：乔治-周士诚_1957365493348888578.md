---
key: 视频生成/图生视频/万相wan2.2 首尾帧 B站：乔治-周士诚_1957365493348888578.json
name: 万相wan2.2 首尾帧 B站：乔治-周士诚_1957365493348888578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957365493348888578.json
hash: baf2917885e8cb47
coverage: 0.96
learned_at: 2026-10-15 22:31:16
nodes: [VAEDecode, CLIPTextEncode, CLIPTextEncode, WanVideoNAG, WanFirstLastFrameToVideo, ImageScale, VAELoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScale, easy int, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, LoadImage, TextInput_, TextInput_, QZ_ResolutionPreset]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/万相wan2.2 首尾帧 B站：乔治-周士诚_1957365493348888578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957365493348888578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `WanFirstLastFrameToVideo`
- `ImageScale`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScale`
- `easy int`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `TextInput_`
- `TextInput_`
- `QZ_ResolutionPreset`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`WanVideoNAG`、`WanFirstLastFrameToVideo`、`ImageScale`、`VAELoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`easy int`、`VHS_VideoCombine`、`LoadImage`、`TextInput_`、`QZ_ResolutionPreset`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
