---
key: 视频生成/图生视频/WAN2.2图生视频_1999730211526766594.json
name: WAN2.2图生视频_1999730211526766594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999730211526766594.json
hash: a5eb44ca31c8dfde
coverage: 0.96875
learned_at: 2026-10-15 22:33:37
nodes: [INTConstant, INTConstant, Int, VHS_VideoCombine, Int, CLIPTextEncode, LoadImage, UNETLoader, UNETLoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, RIFE VFI, wanBlockSwap, VAEDecode, easy cleanGpuUsed, KSamplerAdvanced, CLIPTextEncode, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideo, VAELoader, wanBlockSwap]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2图生视频_1999730211526766594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999730211526766594.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `INTConstant`
- `INTConstant`
- `Int`
- `VHS_VideoCombine`
- `Int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `RIFE VFI`
- `wanBlockSwap`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `VAELoader`
- `wanBlockSwap`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`INTConstant`、`Int`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`wanBlockSwap`、`VAEDecode`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`WanImageToVideo`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
