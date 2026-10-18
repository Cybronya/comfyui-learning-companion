---
key: 视频生成/图生视频/wan2.2_2013893086845341698.json
name: wan2.2_2013893086845341698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_2013893086845341698.json
hash: 5de4a73fcd425aa7
coverage: 0.634615
learned_at: 2026-10-15 22:34:33
nodes: [PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, Reroute, wanBlockSwap, CLIPLoader, VAELoader, Reroute, Reroute, Reroute, wanBlockSwap, easy promptReplace, CLIPTextEncode, CLIPTextEncode, ImpactInt, INTConstant, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, VHS_VideoCombine, INTConstant, INTConstant, Reroute, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Reroute, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, VHS_VideoCombine, UNETLoader, UNETLoader, CR Text, Note, WanImageToVideo, KSamplerAdvanced, RIFE VFI, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2_2013893086845341698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013893086845341698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `wanBlockSwap`
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `wanBlockSwap`
- `easy promptReplace`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `INTConstant`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `Note`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **63%**（33/52）

**有卡**：`PathchSageAttentionKJ`、`ImageResizeKJv2`、`wanBlockSwap`、`CLIPLoader`、`VAELoader`、`easy promptReplace`、`CLIPTextEncode`、`ImpactInt`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`VHS_VideoCombine`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`CR Text`、`WanImageToVideo`、`RIFE VFI`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
