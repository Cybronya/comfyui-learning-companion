---
key: 视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_change_camera_1993311257635782657.json
name: video_wan2_2_14B_i2v_FFGO_change_camera_1993311257635782657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1993311257635782657.json
hash: 53795b38b8a2bb30
coverage: 0.555556
learned_at: 2026-10-15 22:33:18
nodes: [SetNode, SetNode, CLIPLoader, GetNode, ModelSamplingSD3, GetNode, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, WanVideoNAG, CLIPTextEncode, VAELoader, ModelSamplingSD3, GetNode, KSamplerAdvanced, UNETLoader, ImageStitch, ImageStitch, RMBG, GetImageRangeFromBatch, ImageResizeKJv2, SetNode, PreviewImage, CLIPVisionLoader, SetNode, INTConstant, INTConstant, UNETLoader, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, RMBG, CFGZeroStar, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPVisionEncode, GetNode, GetNode, GetNode, GetNode, PainterI2V, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, KSamplerAdvanced, TrimVideoLatent, CLIPTextEncode, VHS_VideoCombine, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_change_camera_1993311257635782657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993311257635782657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageStitch`
- `ImageStitch`
- `RMBG`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `CLIPVisionLoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `RMBG`
- `CFGZeroStar`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PainterI2V`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `TrimVideoLatent`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（35/63）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`VAEDecode`、`WanVideoNAG`、`CLIPTextEncode`、`VAELoader`、`KSamplerAdvanced`、`UNETLoader`、`ImageStitch`、`RMBG`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`CLIPVisionLoader`、`INTConstant`、`LoraLoaderModelOnly`、`CFGZeroStar`、`PathchSageAttentionKJ`、`CLIPVisionEncode`、`PainterI2V`、`TrimVideoLatent`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
