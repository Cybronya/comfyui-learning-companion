---
key: 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json
name: video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json
hash: 8a05a6c55d7a52ce
coverage: 0.43662
learned_at: 2026-10-15 22:33:35
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, Reroute, wanBlockSwap, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, CLIPTextEncode, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy int, PrimitiveStringMultiline, Note, Int, VHS_VideoCombine, easy int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999107369680371713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（71 个）：
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
- `wanBlockSwap`
- `Reroute`
- `wanBlockSwap`
- `Reroute`
- `UNETLoader` ★核心
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
- `LoadImage`
- `easy int`
- `PrimitiveStringMultiline`
- `Note`
- `Int`
- `VHS_VideoCombine`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（31/71）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy int`、`Int`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
