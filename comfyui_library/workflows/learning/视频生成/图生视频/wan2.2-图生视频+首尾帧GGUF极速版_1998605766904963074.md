---
key: 视频生成/图生视频/wan2.2-图生视频+首尾帧GGUF极速版_1998605766904963074.json
name: wan2.2-图生视频+首尾帧GGUF极速版_1998605766904963074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998605766904963074.json
hash: 99e6cb227b2cbc23
coverage: 0.965517
learned_at: 2026-10-15 22:33:32
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPVisionEncode, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ModelPatchTorchSettings, WanImageToVideo, ModelPatchTorchSettings, VAEDecode, ImageResizeKJv2, WanMoeKSampler, WanMoeKSampler, VHS_VideoCombine, ImageResizeKJv2, ModelPatchTorchSettings, PathchSageAttentionKJ, easy clearCacheAll, VAEDecode, easy clearCacheAll, ModelPatchTorchSettings, VHS_VideoCombine, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPTextEncode, RIFE VFI, ImageResizeKJv2, Int, Int, Int, Int, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, RIFE VFI, Qwen3_VQA, easy clearCacheAll, LoraLoaderModelOnly, UnetLoaderGGUF, LoadImage, LoadImage, LoadImage, CLIPTextEncode, UnetLoaderGGUF, CLIPTextEncode, easy showAnything, LoraLoaderModelOnly, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-图生视频+首尾帧GGUF极速版_1998605766904963074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998605766904963074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ModelPatchTorchSettings`
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `WanMoeKSampler` ★核心
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `Int`
- `Int`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `RIFE VFI`
- `Qwen3_VQA`
- `easy clearCacheAll`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **97%**（56/58）

**有卡**：`PathchSageAttentionKJ`、`CLIPVisionEncode`、`CLIPTextEncode`、`CLIPVisionLoader`、`ModelPatchTorchSettings`、`WanImageToVideo`、`VAEDecode`、`ImageResizeKJv2`、`WanMoeKSampler`、`VHS_VideoCombine`、`easy clearCacheAll`、`WanFirstLastFrameToVideo`、`RIFE VFI`、`Int`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`Qwen3_VQA`、`UnetLoaderGGUF`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、WanMoeKSampler、CLIPVisionEncode
