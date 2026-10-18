---
key: 视频生成/图生视频/wan2.2官方图生视频，自动润色提示词_1950052256939950082.json
name: wan2.2官方图生视频，自动润色提示词_1950052256939950082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2官方图生视频，自动润色提示词_1950052256939950082.json
hash: 03853d0c78450320
coverage: 0.903226
learned_at: 2026-10-15 22:30:52
nodes: [DF_Integer, easy showAnything, easy ifElse, TextBox, LayerUtility: PurgeVRAM, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, SimpleMath+, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, CLIPVisionLoader, easy cleanGpuUsed, easy showAnything, CR Text Replace, RH_Captioner, VAELoader, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, TextBox, ModelSamplingSD3, KSamplerAdvanced, UNETLoader, UNETLoader, TextBox, easy int, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2官方图生视频，自动润色提示词_1950052256939950082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950052256939950082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（31 个）：
- `DF_Integer`
- `easy showAnything`
- `easy ifElse`
- `TextBox`
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `SimpleMath+`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextBox`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `TextBox`
- `easy int`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`DF_Integer`、`TextBox`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`SimpleMath+`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`VAELoader`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`easy int`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
