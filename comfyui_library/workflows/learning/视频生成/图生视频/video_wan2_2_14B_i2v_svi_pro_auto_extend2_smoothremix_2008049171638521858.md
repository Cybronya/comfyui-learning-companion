---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_smoothremix_2008049171638521858.json
name: video_wan2_2_14B_i2v_svi_pro_auto_extend2_smoothremix_2008049171638521858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2008049171638521858.json
hash: 9baf249206388610
coverage: 0.567568
learned_at: 2026-10-15 22:34:05
nodes: [PathchSageAttentionKJ, CFGZeroStar, CLIPLoader, ModelSamplingSD3, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanVideoNAG, CLIPTextEncode, VAELoader, SetNode, SetNode, GetImageRangeFromBatch, ModelSamplingSD3, GetNode, CLIPVisionLoader, KSamplerAdvanced, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, GetNode, INTConstant, INTConstant, ModelSamplingSD3, VAEDecode, VAEDecode, VHS_VideoCombine, GetNode, GetNode, GetNode, CLIPTextEncode, VHS_VideoCombine, easy forLoopEnd, VAEEncode, WanVideoNAG, WanImageToVideoSVIPro, WanImageToVideoSVIPro, KSamplerAdvanced, KSamplerAdvanced, SetNode, PreviewAny, CLIPTextEncode, ImageResizeKJv2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy promptLine, easy forLoopStart, ImageBatchExtendWithOverlap, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_smoothremix_2008049171638521858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008049171638521858.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（74 个）：
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `CLIPLoader`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `VAEEncode` ★核心
- `WanVideoNAG`
- `WanImageToVideoSVIPro`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy promptLine`
- `easy forLoopStart`
- `ImageBatchExtendWithOverlap`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（42/74）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStar`、`CLIPLoader`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`VAELoader`、`GetImageRangeFromBatch`、`CLIPVisionLoader`、`KSamplerAdvanced`、`VAEEncode`、`VHS_VideoCombine`、`INTConstant`、`VAEDecode`、`easy forLoopEnd`、`WanImageToVideoSVIPro`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`easy promptLine`、`easy forLoopStart`、`ImageBatchExtendWithOverlap`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
