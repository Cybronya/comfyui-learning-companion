---
key: 视频生成/图生视频/Wan2.2图生视频加速_1953037159256289282.json
name: Wan2.2图生视频加速_1953037159256289282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953037159256289282.json
hash: 5b2f4582dae61406
coverage: 0.891892
learned_at: 2026-10-15 22:31:03
nodes: [easy ifElse, easy int, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, CR Text Replace, RH_Captioner, VAELoader, PrimitiveBoolean, Note, LayerUtility: ImageScaleByAspectRatio V2, TextBox, WanImageToVideo, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CLIPLoader, TextBox, VAEDecode, VHS_VideoCombine, easy showAnything, CLIPVisionEncode, CLIPVisionLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, easy showAnything, LoadImage, TextBox, DF_Integer]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2图生视频加速_1953037159256289282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953037159256289282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `easy ifElse`
- `easy int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CR Text Replace`
- `RH_Captioner`
- `VAELoader`
- `PrimitiveBoolean`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextBox`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `TextBox`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `LoadImage`
- `TextBox`
- `DF_Integer`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`easy int`、`CLIPTextEncode`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`VAELoader`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextBox`、`WanImageToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`SimpleMath+`、`KSamplerAdvanced`、`LoadImage`、`DF_Integer`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
