---
key: 视频生成/图生视频/wan2.2加速首尾帧_1958142838896807937.json
name: wan2.2加速首尾帧_1958142838896807937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958142838896807937.json
hash: 524220601909c5b2
coverage: 0.965517
learned_at: 2026-10-15 22:31:21
nodes: [RH_Translator, VAEDecodeTiled, LoadImage, LoadImage, UpscaleModelLoader, Textbox, CLIPTextEncode, VAELoader, CLIPTextEncode, UNETLoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, ImageUpscaleWithModel, ModelSamplingSD3, CLIPVisionLoader, UNETLoader, CLIPVisionEncode, CLIPVisionEncode, ImageScale, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, WanFirstLastFrameToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoNAG, RIFE VFI, Seed Everywhere]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2加速首尾帧_1958142838896807937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958142838896807937.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `RH_Translator`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LoadImage`
- `UpscaleModelLoader`
- `Textbox`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `ImageUpscaleWithModel`
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `ImageScale`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `RIFE VFI`
- `Seed Everywhere`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`RH_Translator`、`VAEDecodeTiled`、`LoadImage`、`UpscaleModelLoader`、`Textbox`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`ModelSamplingSD3`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageScale`、`KSamplerAdvanced`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`LoraLoaderModelOnly`、`WanVideoNAG`、`RIFE VFI`、`Seed Everywhere`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed Everywhere
