---
key: 视频生成/文生视频/wan2.1文生视频T2V、视频重绘V2V——ComfyUI官方节点工作流_1937543806487302146.json
name: wan2.1文生视频T2V、视频重绘V2V——ComfyUI官方节点工作流_1937543806487302146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1937543806487302146.json
hash: 1a0a0c7b34466eff
coverage: 0.758621
learned_at: 2026-10-15 22:43:29
nodes: [LayerUtility: PurgeVRAM V2, Note, ImageSmartSharpen+, GIMMVFI_interpolate, VHS_VideoCombine, LoraLoaderModelOnly, Anything Everywhere3, TorchCompileModel, VAEEncodeTiled, PathchSageAttentionKJ, LoraLoaderModelOnly, WanVideoEnhanceAVideoKJ, ModelSamplingSD3, SkipLayerGuidanceWanVideo, easy clearCacheAll, CFGZeroStarAndInit, Text Multiline, CLIPTextEncode, LoraLoaderModelOnly, VAEDecode, Note, Reroute, Reroute, Reroute, WanVideoTeaCacheKJ, LoraLoaderModelOnly, Reroute, UNetTemporalAttentionMultiply, Reroute, Note, Text Multiline, VAEEncode, CLIPLoader, VAELoader, UpscaleModelLoader, ImageUpscaleWithModel, DownloadAndLoadGIMMVFIModel, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Concatenate, CLIPTextEncode, VHS_VideoCombine, Any Switch (rgthree), Text Multiline, VAEDecodeTiled, LoraLoaderModelOnly, Note, Note, UNETLoader, Text Multiline, Text Multiline, ShowText|pysssss, Any Switch (rgthree), ImageResizeKJ, VHS_LoadVideo, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 708183091574575, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.1文生视频T2V、视频重绘V2V——ComfyUI官方节点工作流_1937543806487302146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1937543806487302146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `ImageSmartSharpen+`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `TorchCompileModel`
- `VAEEncodeTiled` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `WanVideoEnhanceAVideoKJ`
- `ModelSamplingSD3`
- `SkipLayerGuidanceWanVideo`
- `easy clearCacheAll`
- `CFGZeroStarAndInit`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoTeaCacheKJ`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `UNetTemporalAttentionMultiply`
- `Reroute`
- `Note`
- `Text Multiline`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `DownloadAndLoadGIMMVFIModel`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `Text Multiline`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `UNETLoader` ★核心
- `Text Multiline`
- `Text Multiline`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `708183091574575`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（44/58）

**有卡**：`LayerUtility: PurgeVRAM V2`、`ImageSmartSharpen+`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`TorchCompileModel`、`VAEEncodeTiled`、`PathchSageAttentionKJ`、`WanVideoEnhanceAVideoKJ`、`ModelSamplingSD3`、`SkipLayerGuidanceWanVideo`、`easy clearCacheAll`、`CFGZeroStarAndInit`、`Text Multiline`、`CLIPTextEncode`、`VAEDecode`、`WanVideoTeaCacheKJ`、`UNetTemporalAttentionMultiply`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`DownloadAndLoadGIMMVFIModel`、`Text Concatenate`、`VAEDecodeTiled`、`UNETLoader`、`ImageResizeKJ`、`VHS_LoadVideo`、`EmptyHunyuanLatentVideo`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
