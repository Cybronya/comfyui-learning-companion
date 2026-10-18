---
key: 视频生成/图生视频/wan2.2-14B图生视频加速流_1959204229682507777.json
name: wan2.2-14B图生视频加速流_1959204229682507777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-14B图生视频加速流_1959204229682507777.json
hash: 242e78a65ade724a
coverage: 0.891892
learned_at: 2026-10-15 22:31:24
nodes: [DF_Integer, easy ifElse, easy int, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, CR Text Replace, RH_Captioner, VAELoader, PrimitiveBoolean, Note, LayerUtility: ImageScaleByAspectRatio V2, TextBox, WanImageToVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CLIPLoader, TextBox, TextBox, VAEDecode, VHS_VideoCombine, easy showAnything, CLIPVisionEncode, CLIPVisionLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, easy showAnything, UNETLoader, UNETLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-14B图生视频加速流_1959204229682507777.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959204229682507777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `DF_Integer`
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
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `TextBox`
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
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`DF_Integer`、`easy int`、`CLIPTextEncode`、`easy cleanGpuUsed`、`CR Text Replace`、`RH_Captioner`、`VAELoader`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextBox`、`WanImageToVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`VAEDecode`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`SimpleMath+`、`KSamplerAdvanced`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
