---
key: 图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json
name: seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json
hash: 0fdcd184d14d65e7
coverage: 1
learned_at: 2026-10-23 11:45:16
nodes: [KSamplerSelect, RH_Captioner, RandomNoise, BasicGuider, VAEEncode, LineArtPreprocessor, ImageResizeKJ, ImageInvert, ImageUpscaleWithModel, ImageResizeKJ, VAELoader, SamplerCustomAdvanced, VAEDecode, easy cleanGpuUsed, Image Levels Adjustment, easy imageRemBg, BasicScheduler, SaveImage, LoadImage, Checkpoint Loader (Simple), UpscaleModelLoader, CLIPTextEncode, DualCLIPLoader]
patterns: []
missing: []
---

# 图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/seedance2.5真人过审，转线稿，站位图，适用于即梦_2088403416916774913.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `RH_Captioner`
- `RandomNoise`
- `BasicGuider`
- `VAEEncode` ★核心
- `LineArtPreprocessor`
- `ImageResizeKJ`
- `ImageInvert`
- `ImageUpscaleWithModel`
- `ImageResizeKJ`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Levels Adjustment`
- `easy imageRemBg`
- `BasicScheduler`
- `SaveImage`
- `LoadImage`
- `Checkpoint Loader (Simple)`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`KSamplerSelect`、`RH_Captioner`、`RandomNoise`、`BasicGuider`、`VAEEncode`、`LineArtPreprocessor`、`ImageResizeKJ`、`ImageInvert`、`ImageUpscaleWithModel`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`Image Levels Adjustment`、`easy imageRemBg`、`BasicScheduler`、`SaveImage`、`LoadImage`、`Checkpoint Loader (Simple)`、`UpscaleModelLoader`、`CLIPTextEncode`、`DualCLIPLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEEncode、DualCLIPLoader
