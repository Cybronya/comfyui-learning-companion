---
key: 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json
name: video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json
hash: c9c6fd0110bffc2a
coverage: 0.428571
learned_at: 2026-10-15 22:34:01
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, CLIPTextEncode, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Note, easy int, Int, easy int, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, LoraLoaderModelOnly, Reroute, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006247037502758914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `CLIPLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `easy int`
- `Int`
- `easy int`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **43%**（30/70）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`Int`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
