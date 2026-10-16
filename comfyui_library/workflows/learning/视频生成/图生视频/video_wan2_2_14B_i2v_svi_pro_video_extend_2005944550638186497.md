---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_video_extend_2005944550638186497.json
name: video_wan2_2_14B_i2v_svi_pro_video_extend_2005944550638186497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005944550638186497.json
hash: 6b3dbc64855575a7
coverage: 0.527273
learned_at: 2026-10-15 22:33:59
nodes: [PathchSageAttentionKJ, CFGZeroStar, SetNode, CLIPLoader, GetNode, ModelSamplingSD3, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, WanVideoNAG, CLIPTextEncode, VAELoader, ModelSamplingSD3, GetNode, CLIPVisionLoader, UNETLoader, UNETLoader, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, INTConstant, INTConstant, GetNode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, VAEEncode, VAEEncode, SetNode, SetNode, SetNode, ImageBatchExtendWithOverlap, WanImageToVideoSVIPro]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_video_extend_2005944550638186497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005944550638186497.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `GetNode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `WanImageToVideoSVIPro`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **53%**（29/55）

**有卡**：`PathchSageAttentionKJ`、`CFGZeroStar`、`CLIPLoader`、`ModelSamplingSD3`、`WanVideoNAG`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`UNETLoader`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`INTConstant`、`KSamplerAdvanced`、`VAEDecode`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`VAEEncode`、`ImageBatchExtendWithOverlap`、`WanImageToVideoSVIPro`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar
