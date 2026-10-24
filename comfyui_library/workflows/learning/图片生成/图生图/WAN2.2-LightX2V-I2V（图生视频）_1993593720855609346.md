---
key: 图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json
name: WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json
hash: f608067ef93e0f75
coverage: 0.861111
learned_at: 2026-10-23 11:27:28
nodes: [CLIPTextEncode, VAELoader, Note, CLIPLoader, UNETLoader, Note, VAEDecode, Note, INTConstant, Int, Int, wanBlockSwap, ModelPatchTorchSettings, wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, KSamplerAdvanced, easy cleanGpuUsed, RIFE VFI, KSamplerAdvanced, WanImageToVideo, LoadImage, Note, INTConstant, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `Int`
- `Int`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `LoadImage`
- `Note`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`INTConstant`、`Int`、`wanBlockSwap`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`RIFE VFI`、`WanImageToVideo`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
