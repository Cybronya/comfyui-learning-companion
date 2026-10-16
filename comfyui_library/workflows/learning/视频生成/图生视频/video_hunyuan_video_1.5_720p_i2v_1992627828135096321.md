---
key: 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v_1992627828135096321.json
name: video_hunyuan_video_1.5_720p_i2v_1992627828135096321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992627828135096321.json
hash: 50675c20319ee760
coverage: 0.5
learned_at: 2026-10-15 22:33:16
nodes: [GetNode, VAEDecodeTiled, MarkdownNote, MarkdownNote, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, PreviewAny, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, HunyuanVideo15LatentUpscaleWithModel, VHS_VideoCombine, GetNode, SetNode, ModelSamplingSD3, KSampler, VAEDecode, SetNode, SetNode, SetNode, SetNode, SetNode, Note, AILab_QwenVL, UNETLoader, PathchSageAttentionKJ, DualCLIPLoader, VAELoader, LoadImage, ImageResizeKJv2, CLIPVisionLoader, CLIPVisionEncode, HunyuanVideo15ImageToVideo, UNETLoader, LatentUpscaleModelLoader, ModelSamplingSD3, HunyuanVideo15SuperResolution, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v_1992627828135096321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992627828135096321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
- `GetNode`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `HunyuanVideo15LatentUpscaleWithModel`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `AILab_QwenVL`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `HunyuanVideo15ImageToVideo`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `ModelSamplingSD3`
- `HunyuanVideo15SuperResolution`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（25/50）

**有卡**：`VAEDecodeTiled`、`CLIPTextEncode`、`HunyuanVideo15LatentUpscaleWithModel`、`VHS_VideoCombine`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`AILab_QwenVL`、`UNETLoader`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`ImageResizeKJv2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`HunyuanVideo15ImageToVideo`、`LatentUpscaleModelLoader`、`HunyuanVideo15SuperResolution`、`KSamplerAdvanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced、VAEDecodeTiled
