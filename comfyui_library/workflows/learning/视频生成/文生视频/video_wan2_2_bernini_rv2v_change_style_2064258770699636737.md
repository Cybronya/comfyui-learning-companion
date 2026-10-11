---
key: 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json
name: video_wan2_2_bernini_rv2v_change_style_2064258770699636737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json
hash: 715e3f85f6ca898d
coverage: 0.45614
learned_at: 2026-10-11 20:21:32
nodes: [CFGZeroStar, SetNode, CLIPLoader, GetNode, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, VAELoader, CLIPVisionLoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, KSamplerAdvanced, WanVideoNAG, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BerniniConditioning, SetNode, SetNode, SetNode, SetNode, BatchImagesNode, VHS_VideoCombine, INTConstant, MarkdownNote, LoadImage, VHS_LoadVideo, INTConstant, INTConstant, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `CFGZeroStar`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BerniniConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BatchImagesNode`
- `VHS_VideoCombine`
- `INTConstant`
- `MarkdownNote`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **46%**（26/57）

**有卡**：`CFGZeroStar`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionLoader`、`ModelSamplingSD3`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ImageResizeKJv2`、`BerniniConditioning`、`BatchImagesNode`、`VHS_VideoCombine`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
