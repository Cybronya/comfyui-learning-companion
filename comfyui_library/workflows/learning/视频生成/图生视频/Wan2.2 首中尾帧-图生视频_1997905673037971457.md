---
key: 视频生成/图生视频/Wan2.2 首中尾帧-图生视频_1997905673037971457.json
name: Wan2.2 首中尾帧-图生视频_1997905673037971457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997905673037971457.json
hash: 9d888aceb407f988
coverage: 1
learned_at: 2026-10-15 22:33:30
nodes: [UNETLoader, CLIPLoader, LoraLoaderModelOnly, WanFirstMiddleLastFrameToVideo, UNETLoader, CLIPTextEncode, ModelSamplingSD3, ImageScaleBy, ImageScaleBy, ImageConcatMulti, ImageScaleBy, VAELoader, LoraLoaderModelOnly, INTConstant, INTConstant, ImageConcanate, VAEDecode, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 首中尾帧-图生视频_1997905673037971457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997905673037971457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `ImageScaleBy`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `ImageConcanate`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`WanFirstMiddleLastFrameToVideo`、`CLIPTextEncode`、`ModelSamplingSD3`、`ImageScaleBy`、`ImageConcatMulti`、`VAELoader`、`INTConstant`、`ImageConcanate`、`VAEDecode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
