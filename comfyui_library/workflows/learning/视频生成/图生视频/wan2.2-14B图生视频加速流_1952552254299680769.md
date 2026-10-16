---
key: 视频生成/图生视频/wan2.2-14B图生视频加速流_1952552254299680769.json
name: wan2.2-14B图生视频加速流_1952552254299680769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952552254299680769.json
hash: 887c32ef02b5d5a8
coverage: 0.891892
learned_at: 2026-10-15 22:31:02
nodes: [DF_Integer, CLIPTextEncode, easy cleanGpuUsed, RH_Captioner, Note, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CLIPLoader, LoadImage, VAEDecode, easy showAnything, CLIPVisionEncode, CLIPVisionLoader, KSamplerAdvanced, KSamplerAdvanced, easy showAnything, CLIPTextEncode, VAELoader, easy int, SimpleMath+, VHS_VideoCombine, PrimitiveBoolean, Textbox, CR Text Replace, Textbox, Textbox, easy ifElse]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-14B图生视频加速流_1952552254299680769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952552254299680769.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `DF_Integer`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `RH_Captioner`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LoadImage`
- `VAEDecode` ★核心
- `easy showAnything`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `easy int`
- `SimpleMath+`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `Textbox`
- `CR Text Replace`
- `Textbox`
- `Textbox`
- `easy ifElse`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`DF_Integer`、`CLIPTextEncode`、`easy cleanGpuUsed`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`KSamplerAdvanced`、`VAELoader`、`easy int`、`SimpleMath+`、`VHS_VideoCombine`、`PrimitiveBoolean`、`Textbox`、`CR Text Replace`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
