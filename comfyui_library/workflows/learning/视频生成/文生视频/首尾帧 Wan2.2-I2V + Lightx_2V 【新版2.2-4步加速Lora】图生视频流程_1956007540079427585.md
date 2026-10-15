---
key: 视频生成/文生视频/首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585.json
name: 首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585.json
hash: 2372f3c78a80f9b3
coverage: 0.90625
learned_at: 2026-10-15 22:49:06
nodes: [CLIPTextEncode, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, RIFE VFI, Int, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, VAELoader, Note, SaveImage, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, UnetLoaderGGUF, UnetLoaderGGUF, Note, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Note, VHS_VideoCombine, VHS_VideoCombine, ImageScale, ImageScale, WanFirstLastFrameToVideo, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `RIFE VFI`
- `Int`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageScale`
- `ImageScale`
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`CLIPTextEncode`、`WanVideoNAG`、`ModelSamplingSD3`、`RIFE VFI`、`Int`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`SaveImage`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`Power Lora Loader (rgthree)`、`VHS_VideoCombine`、`ImageScale`、`WanFirstLastFrameToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Power Lora Loader (rgthree)、SaveImage
