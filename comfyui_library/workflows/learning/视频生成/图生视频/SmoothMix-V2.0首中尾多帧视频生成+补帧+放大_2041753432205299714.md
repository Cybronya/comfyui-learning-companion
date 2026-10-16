---
key: 视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2041753432205299714.json
name: SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2041753432205299714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041753432205299714.json
hash: be4cdb80e35237d7
coverage: 1
learned_at: 2026-10-15 22:36:21
nodes: [CLIPLoader, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, KSamplerAdvanced, ModelSamplingSD3, VAELoader, INTConstant, INTConstant, INTConstant, CLIPTextEncode, SimpleMath+, RIFE VFI, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, easy cleanGpuUsed, ImageScaleBy, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/SmoothMix-V2.0首中尾多帧视频生成+补帧+放大_2041753432205299714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041753432205299714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImageResizeKJv2`、`KSamplerAdvanced`、`VAELoader`、`INTConstant`、`SimpleMath+`、`RIFE VFI`、`VHS_VideoCombine`、`WanFirstMiddleLastFrameToVideo`、`easy cleanGpuUsed`、`ImageScaleBy`、`VAEDecode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
