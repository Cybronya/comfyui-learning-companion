---
key: 视频生成/图生视频/AA--批量自动图生视频+wan2.2自动图生视频+FlashVSR视频放大_1999756057926922241.json
name: AA--批量自动图生视频+wan2.2自动图生视频+FlashVSR视频放大_1999756057926922241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AA--批量自动图生视频+wan2.2自动图生视频+FlashVSR视频放大_1999756057926922241.json
hash: f2ab229a29d8bd71
coverage: 0.765957
learned_at: 2026-10-15 22:33:38
nodes: [UNETLoader, ModelSamplingSD3, ModelSamplingSD3, VAELoader, CLIPLoader, PathchSageAttentionKJ, UNETLoader, easy forLoopEnd, easy showAnything, PathchSageAttentionKJ, Note, VHS_LoadVideo, FlashVSRNode, VHS_VideoInfo, VHS_VideoCombine, Note, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, Note, Note, easy imageCount, LayerUtility: PurgeVRAM, CLIPTextEncode, VAEDecode, Note, Note, Note, easy forLoopStart, KSamplerAdvanced, KSamplerAdvanced, Qwen3_VQA, VHS_VideoCombine, RHUploadZip, easy float, ImageScaleBy, RHBatchImages:, Bjornulf_ShowInt, Bjornulf_ShowInt, RHExtractImage, PreviewImage, CLIPTextEncode, WanImageToVideo, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/AA--批量自动图生视频+wan2.2自动图生视频+FlashVSR视频放大_1999756057926922241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999756057926922241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `easy forLoopEnd`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `Note`
- `VHS_LoadVideo`
- `FlashVSRNode`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `Note`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `Note`
- `Note`
- `easy imageCount`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Note`
- `Note`
- `Note`
- `easy forLoopStart`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Qwen3_VQA`
- `VHS_VideoCombine`
- `RHUploadZip`
- `easy float`
- `ImageScaleBy`
- `RHBatchImages:`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `RHExtractImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`easy forLoopEnd`、`VHS_LoadVideo`、`FlashVSRNode`、`VHS_VideoInfo`、`VHS_VideoCombine`、`JWInteger`、`LayerUtility: PurgeVRAM`、`LoraLoaderModelOnly`、`easy imageCount`、`CLIPTextEncode`、`VAEDecode`、`easy forLoopStart`、`KSamplerAdvanced`、`Qwen3_VQA`、`RHUploadZip`、`easy float`、`ImageScaleBy`、`RHBatchImages:`、`Bjornulf_ShowInt`、`RHExtractImage`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Bjornulf_ShowInt
