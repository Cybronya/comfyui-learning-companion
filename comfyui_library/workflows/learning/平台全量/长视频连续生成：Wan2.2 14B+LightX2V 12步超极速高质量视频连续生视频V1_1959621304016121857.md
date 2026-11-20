---
key: 平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json
name: 长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json
hash: 12a717828bb1f543
coverage: 0.911765
learned_at: 2026-11-14 02:49:29
nodes: [CLIPTextEncode, VAELoader, Note, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, CLIPLoader, ModelSamplingSD3, PathchSageAttentionKJ, easy mathInt, PreviewImage, VAEDecode, UNETLoader, VHS_MergeImages, VHS_SelectImages, SomethingToString, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, CLIPTextEncode, WanImageToVideo, Image Size to Number, VHS_VideoCombine, JWInteger, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json

> 来源文件 `comfyui_library/workflows/平台全量/长视频连续生成：Wan2.2 14B+LightX2V 12步超极速高质量视频连续生视频V1_1959621304016121857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy mathInt`
- `PreviewImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VHS_MergeImages`
- `VHS_SelectImages`
- `SomethingToString`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `Image Size to Number`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPLoader`、`easy mathInt`、`VAEDecode`、`UNETLoader`、`VHS_MergeImages`、`VHS_SelectImages`、`SomethingToString`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`WanImageToVideo`、`Image Size to Number`、`JWInteger`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、Image Size to Number
