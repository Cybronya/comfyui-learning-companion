---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_final_2006035355308400642.json
name: video_wan2_2_14B_i2v_svi_pro_auto_extend2_final_2006035355308400642.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2006035355308400642.json
hash: 4daeee6c0bffdc94
coverage: 0.567568
learned_at: 2026-10-15 22:34:00
nodes: [PathchSageAttentionKJ, CFGZeroStar, SetNode, CLIPLoader, ModelSamplingSD3, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, WanVideoNAG, CLIPTextEncode, ImageResizeKJv2, VAELoader, SetNode, SetNode, GetImageRangeFromBatch, ModelSamplingSD3, GetNode, CLIPVisionLoader, KSamplerAdvanced, SetNode, UNETLoader, SetNode, SetNode, SetNode, UNETLoader, SetNode, GetNode, GetNode, GetNode, VAEEncode, LoadImage, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, ModelSamplingSD3, VHS_VideoCombine, GetNode, INTConstant, INTConstant, ModelSamplingSD3, VAEDecode, VAEDecode, VHS_VideoCombine, GetNode, GetNode, GetNode, CLIPTextEncode, VHS_VideoCombine, easy forLoopEnd, VAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoNAG, WanImageToVideoSVIPro, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewAny, easy forLoopStart, easy promptLine, WanImageToVideoSVIPro, ImageBatchExtendWithOverlap]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_final_2006035355308400642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006035355308400642.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（74 个）：
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `SetNode`
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
- `ImageResizeKJv2`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `easy forLoopStart`
- `easy promptLine`
- `WanImageToVideoSVIPro`
- `ImageBatchExtendWithOverlap`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（42/74）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStar`、`CLIPLoader`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`ImageResizeKJv2`、`VAELoader`、`GetImageRangeFromBatch`、`CLIPVisionLoader`、`KSamplerAdvanced`、`UNETLoader`、`VAEEncode`、`LoadImage`、`VHS_VideoCombine`、`INTConstant`、`VAEDecode`、`easy forLoopEnd`、`LoraLoaderModelOnly`、`WanImageToVideoSVIPro`、`easy forLoopStart`、`easy promptLine`、`ImageBatchExtendWithOverlap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
