---
key: 视频生成/图生视频/wan2.2-fmlf多帧长视频-gen全能视频Si_1988112429857021954.json
name: wan2.2-fmlf多帧长视频-gen全能视频Si_1988112429857021954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-fmlf多帧长视频-gen全能视频Si_1988112429857021954.json
hash: 0ea8cc396a91813a
coverage: 1
learned_at: 2026-10-15 22:33:01
nodes: [KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, WanMultiFrameRefToVideo, INTConstant, ModelSamplingSD3, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, INTConstant, VAEDecode, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, ImageSharpen, VHS_VideoCombine, CLIPTextEncode, ImageBatchMulti]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-fmlf多帧长视频-gen全能视频Si_1988112429857021954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988112429857021954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `WanMultiFrameRefToVideo`
- `INTConstant`
- `ModelSamplingSD3`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `ImageSharpen`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ImageBatchMulti`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`WanMultiFrameRefToVideo`、`INTConstant`、`ModelSamplingSD3`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageSharpen`、`VHS_VideoCombine`、`ImageBatchMulti`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
