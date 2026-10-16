---
key: 视频生成/图生视频/Wan2.2- Lightx2v 1030首、中、尾帧视频_1988980574498992130.json
name: Wan2.2- Lightx2v 1030首、中、尾帧视频_1988980574498992130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988980574498992130.json
hash: a87feb7436981f66
coverage: 1
learned_at: 2026-10-15 22:33:05
nodes: [ModelSamplingSD3, ModelSamplingSD3, ImageResizeKJv2, ImageResizeKJv2, INTConstant, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageResizeKJv2, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, SimpleMath+, VHS_VideoCombine, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ColorMatch_UTK]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2- Lightx2v 1030首、中、尾帧视频_1988980574498992130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988980574498992130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SimpleMath+`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ColorMatch_UTK`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`ModelSamplingSD3`、`ImageResizeKJv2`、`INTConstant`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LoadImage`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SimpleMath+`、`VHS_VideoCombine`、`WanFirstMiddleLastFrameToVideo`、`KSamplerAdvanced`、`VAEDecode`、`ColorMatch_UTK`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
