---
key: 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json
name: video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2000487723846729730.json
hash: 4b756ae8d2cec17e
coverage: 0.465753
learned_at: 2026-10-15 22:33:41
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, wanBlockSwap, Reroute, wanBlockSwap, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, CLIPTextEncode, Note, VHS_VideoCombine, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, Int, easy int, easy int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000487723846729730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（73 个）：
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
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `Int`
- `easy int`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **47%**（34/73）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`WanFirstLastFrameToVideo`、`Int`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
