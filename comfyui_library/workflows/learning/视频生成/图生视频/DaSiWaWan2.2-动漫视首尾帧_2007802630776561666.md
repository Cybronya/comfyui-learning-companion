---
key: 视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json
name: DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007802630776561666.json
hash: e4b5eacf6c456214
coverage: 1
learned_at: 2026-10-15 22:34:05
nodes: [INTConstant, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, UNETLoader, UNETLoader, LoadImage, KSamplerAdvanced, VAEDecode, LoadImage, KSamplerAdvanced, VHS_VideoCombine, INTConstant, INTConstant, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, VAELoader, ModelPatchTorchSettings, ModelPatchTorchSettings, WanFirstLastFrameToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007802630776561666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `INTConstant`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAELoader`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `WanFirstLastFrameToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`INTConstant`、`PathchSageAttentionKJ`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`SimpleMath+`、`ImageResizeKJv2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAELoader`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`ModelSamplingSD3`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
