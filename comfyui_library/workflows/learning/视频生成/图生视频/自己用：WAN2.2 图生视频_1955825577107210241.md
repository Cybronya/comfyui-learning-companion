---
key: 视频生成/图生视频/自己用：WAN2.2 图生视频_1955825577107210241.json
name: 自己用：WAN2.2 图生视频_1955825577107210241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/自己用：WAN2.2 图生视频_1955825577107210241.json
hash: f9912c28dfc597bc
coverage: 0.911765
learned_at: 2026-10-15 22:31:10
nodes: [CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, UNETLoader, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CLIPLoader, VAEDecode, SimpleMath+, easy int, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, RHHiddenNodes, VAELoader, DF_Integer, VHS_VideoCombine, PrimitiveBoolean, easy showAnything, RH_Translator, easy showAnything, LoadImage, TextBox]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/自己用：WAN2.2 图生视频_1955825577107210241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955825577107210241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SimpleMath+`
- `easy int`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `RHHiddenNodes`
- `VAELoader`
- `DF_Integer`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `LoadImage`
- `TextBox`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`CLIPTextEncode`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`UNETLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`VAEDecode`、`SimpleMath+`、`easy int`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`RHHiddenNodes`、`VAELoader`、`DF_Integer`、`VHS_VideoCombine`、`PrimitiveBoolean`、`RH_Translator`、`LoadImage`、`TextBox`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
