---
key: 视频生成/图生视频/Remix2.1图生视频+首尾帧_2010736776633131010.json
name: Remix2.1图生视频+首尾帧_2010736776633131010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix2.1图生视频+首尾帧_2010736776633131010.json
hash: 7e32c35e71fc86b0
coverage: 0.961538
learned_at: 2026-10-15 22:34:18
nodes: [CLIPVisionEncode, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPVisionLoader, CLIPVisionLoader, VAEDecode, ImageResizeKJv2, ImageResizeKJv2, easy getNode, easy getNode, easy getNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, WanMoeKSampler, easy getNode, easy getNode, CLIPTextEncode, easy getNode, WanImageToVideo, WanMoeKSampler, easy getNode, easy clearCacheAll, VAEDecode, WanFirstLastFrameToVideo, ModelPatchTorchSettings, ModelPatchTorchSettings, easy setNode, easy setNode, easy setNode, easy setNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, ImageResizeKJv2, LoadImage, INTConstant, easy getNode, INTConstant, Qwen3_VQA, easy showAnything, VHS_VideoCombine, UNETLoader, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Remix2.1图生视频+首尾帧_2010736776633131010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010736776633131010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（52 个）：
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanMoeKSampler` ★核心
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `easy getNode`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `LoadImage`
- `INTConstant`
- `easy getNode`
- `INTConstant`
- `Qwen3_VQA`
- `easy showAnything`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **96%**（50/52）

**有卡**：`CLIPVisionEncode`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`VAEDecode`、`ImageResizeKJv2`、`easy getNode`、`CLIPTextEncode`、`WanMoeKSampler`、`WanImageToVideo`、`easy clearCacheAll`、`WanFirstLastFrameToVideo`、`ModelPatchTorchSettings`、`easy setNode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`INTConstant`、`Qwen3_VQA`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
