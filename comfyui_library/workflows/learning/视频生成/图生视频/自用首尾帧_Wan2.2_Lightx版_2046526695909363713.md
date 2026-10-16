---
key: 视频生成/图生视频/自用首尾帧_Wan2.2_Lightx版_2046526695909363713.json
name: 自用首尾帧_Wan2.2_Lightx版_2046526695909363713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046526695909363713.json
hash: 5a95005821d7ce41
coverage: 0.90625
learned_at: 2026-10-15 22:36:59
nodes: [CLIPTextEncode, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, RIFE VFI, Int, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, VAELoader, Note, SaveImage, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, UnetLoaderGGUF, UnetLoaderGGUF, Note, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Note, VHS_VideoCombine, VHS_VideoCombine, ImageScale, ImageScale, WanFirstLastFrameToVideo, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/自用首尾帧_Wan2.2_Lightx版_2046526695909363713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046526695909363713.json`

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
