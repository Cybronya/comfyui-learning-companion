---
key: 视频生成/图生视频/万相wan2.2 图生视频 B站：乔治-周士诚_1957316699274014721.json
name: 万相wan2.2 图生视频 B站：乔治-周士诚_1957316699274014721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957316699274014721.json
hash: c0d0edb3cf92f6e8
coverage: 0.956522
learned_at: 2026-10-15 22:31:16
nodes: [CLIPTextEncode, VAEDecode, WanVideoNAG, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline, WanImageToVideo, easy int, CLIPLoader, VAELoader, LoadImage, ImageScale, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, UNETLoader, UNETLoader, TextInput_, TextInput_, QZ_ResolutionPreset]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/万相wan2.2 图生视频 B站：乔治-周士诚_1957316699274014721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957316699274014721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `WanImageToVideo`
- `easy int`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ImageScale`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
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

覆盖率 **96%**（22/23）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`WanVideoNAG`、`ModelSamplingSD3`、`KSamplerAdvanced`、`WanImageToVideo`、`easy int`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ImageScale`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`UNETLoader`、`TextInput_`、`QZ_ResolutionPreset`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
