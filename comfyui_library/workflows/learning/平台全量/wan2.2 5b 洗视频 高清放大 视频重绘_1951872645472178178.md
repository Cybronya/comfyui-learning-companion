---
key: 平台全量/wan2.2 5b 洗视频 高清放大 视频重绘_1951872645472178178.json
name: wan2.2 5b 洗视频 高清放大 视频重绘_1951872645472178178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 5b 洗视频 高清放大 视频重绘_1951872645472178178.json
hash: 49b3ff3dcad48b06
coverage: 0.947368
learned_at: 2026-11-14 01:19:15
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, GetNode, VAEEncode, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LayerUtility: ImageScaleRestore V2, VHS_LoadVideo, Int, VAEDecodeTiled, LayerUtility: PurgeVRAM, VAEDecode, LayerUtility: PurgeVRAM, KSampler, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 777, "steps": 12}
---

# 平台全量/wan2.2 5b 洗视频 高清放大 视频重绘_1951872645472178178.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 5b 洗视频 高清放大 视频重绘_1951872645472178178.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `GetNode`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleRestore V2`
- `VHS_LoadVideo`
- `Int`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `777`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleRestore V2`、`VHS_LoadVideo`、`Int`、`VAEDecodeTiled`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`KSampler`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、VAEDecodeTiled
