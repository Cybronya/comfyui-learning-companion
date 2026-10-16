---
key: 视频生成/图生视频/首尾帧 Wan2.2-I2V 4步加速Lora首尾帧【Q8量化版】_1956638598607900673.json
name: 首尾帧 Wan2.2-I2V 4步加速Lora首尾帧【Q8量化版】_1956638598607900673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956638598607900673.json
hash: 237f8a4220cb15fc
coverage: 0.909091
learned_at: 2026-10-15 22:31:14
nodes: [WanVideoNAG, ModelSamplingSD3, RIFE VFI, Int, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, UnetLoaderGGUF, Power Lora Loader (rgthree), Power Lora Loader (rgthree), VHS_VideoCombine, Note, Note, PreViewVideo, CreateVideo, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, LoadImage, LoadImage, ImageScale, WanFirstLastFrameToVideo, ImageScale, PreviewImage, VAEDecode, UnetLoaderGGUF, CLIPLoader, VAELoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/首尾帧 Wan2.2-I2V 4步加速Lora首尾帧【Q8量化版】_1956638598607900673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956638598607900673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `WanVideoNAG`
- `ModelSamplingSD3`
- `RIFE VFI`
- `Int`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `UnetLoaderGGUF` ★核心
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `PreViewVideo`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `ImageScale`
- `WanFirstLastFrameToVideo`
- `ImageScale`
- `PreviewImage`
- `VAEDecode` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`WanVideoNAG`、`ModelSamplingSD3`、`RIFE VFI`、`Int`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`Power Lora Loader (rgthree)`、`VHS_VideoCombine`、`PreViewVideo`、`CreateVideo`、`CLIPTextEncode`、`LoadImage`、`ImageScale`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Power Lora Loader (rgthree)、PreViewVideo
