---
key: 视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json
name: Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979808803409530882.json
hash: 6d25f479f4c667f8
coverage: 0.957265
learned_at: 2026-10-15 22:32:26
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, Text Multiline, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text Multiline, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, KSamplerAdvanced, SimpleMath+, PrimitiveInt, INTConstant, VAEDecode, VHS_VideoCombine, Note, Reroute, Text Concatenate, Reroute, INTConstant, INTConstant, INTConstant, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, LoadImage, Text Multiline, Note, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2多版本模型对比工作流（I2V图生视频）_1979808803409530882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979808803409530882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（117 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `PrimitiveInt`
- `INTConstant`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Note`
- `Reroute`
- `Text Concatenate`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Text Multiline`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（112/117）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`LoadImage`、`Text Multiline`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanImageToVideo`、`SimpleMath+`、`INTConstant`、`VAEDecode`、`VHS_VideoCombine`、`Text Concatenate`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
