---
key: 视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json
name: Wan 2.2-Fun-VACE-图生视频_1967620116848545793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json
hash: 43f967fb55a087b5
coverage: 1
learned_at: 2026-10-10 23:06:09
nodes: [TrimVideoLatent, VAEDecode, CLIPTextEncode, VHS_VideoCombine, WanVaceToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, GetImageSizeAndCount, LoadImage, WanVideoVACEStartToEndFrame, INTConstant, ImageResizeKJv2, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ImageRepeat, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2-Fun-VACE-图生视频_1967620116848545793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `GetImageSizeAndCount`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageRepeat`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanVaceToVideo`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`GetImageSizeAndCount`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`INTConstant`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageRepeat`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
