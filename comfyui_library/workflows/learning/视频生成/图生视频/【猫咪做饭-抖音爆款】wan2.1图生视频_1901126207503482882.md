---
key: 视频生成/图生视频/【猫咪做饭-抖音爆款】wan2.1图生视频_1901126207503482882.json
name: 【猫咪做饭-抖音爆款】wan2.1图生视频_1901126207503482882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901126207503482882.json
hash: e0ba0563023bdf1b
coverage: 0.973684
learned_at: 2026-10-15 22:29:23
nodes: [LoadWanVideoClipTextEncoder, WanVideoDecode, LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoVAELoader, WanVideoTorchCompileSettings, Note, WanVideoImageClipEncode, Int, Int, ImageResizeAdvanced, WanVideoModelLoader, CR SDXL Aspect Ratio, CLIPTextEncode, DifferentialDiffusion, LoraLoader, LoraLoader, UNETLoader, CLIPTextEncode, LoadImage, VAEDecode, SaveImage, WanVideoTextEncode, VAELoader, DualCLIPLoader, KSampler, KSampler, LatentUpscaleBy, WanVideoLoraSelect, Note Plus (mtb), VHS_VideoCombine, UpscaleModelLoader, RIFE VFI, ImageUpscaleWithModel, WanVideoSampler, WanVideoTeaCache, LoadWanVideoT5TextEncoder]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.6, "lora_name": "F.1蓝白英短猫_v1.0.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 377022722009739, "steps": 25, "strength_clip": 1, "strength_model": 0.9}
---

# 视频生成/图生视频/【猫咪做饭-抖音爆款】wan2.1图生视频_1901126207503482882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901126207503482882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoImageClipEncode`
- `Int`
- `Int`
- `ImageResizeAdvanced`
- `WanVideoModelLoader`
- `CR SDXL Aspect Ratio`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `WanVideoTextEncode`
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `KSampler` ★核心
- `LatentUpscaleBy`
- `WanVideoLoraSelect`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `RIFE VFI`
- `ImageUpscaleWithModel`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `F.1蓝白英短猫_v1.0.safetensors`
- `strength_model` = `0.9`
- `strength_clip` = `1`
- `seed` = `377022722009739`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoImageClipEncode`、`Int`、`ImageResizeAdvanced`、`WanVideoModelLoader`、`CR SDXL Aspect Ratio`、`CLIPTextEncode`、`DifferentialDiffusion`、`LoraLoader`、`UNETLoader`、`LoadImage`、`VAEDecode`、`SaveImage`、`WanVideoTextEncode`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`LatentUpscaleBy`、`WanVideoLoraSelect`、`Note Plus (mtb)`、`VHS_VideoCombine`、`UpscaleModelLoader`、`RIFE VFI`、`ImageUpscaleWithModel`、`WanVideoSampler`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、WanVideoSampler、LatentUpscaleBy
