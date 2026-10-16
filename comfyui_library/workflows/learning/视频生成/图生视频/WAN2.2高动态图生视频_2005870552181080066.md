---
key: 视频生成/图生视频/WAN2.2高动态图生视频_2005870552181080066.json
name: WAN2.2高动态图生视频_2005870552181080066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005870552181080066.json
hash: c8f2be576899f1cc
coverage: 0.414286
learned_at: 2026-10-15 22:33:59
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, Note, Reroute, wanBlockSwap, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, Int, Note, wanBlockSwap, VHS_VideoCombine, CLIPLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, RIFE VFI, VHS_VideoCombine, Int, UNETLoader, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2高动态图生视频_2005870552181080066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005870552181080066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

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
- `Note`
- `Note`
- `Reroute`
- `wanBlockSwap`
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
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageResizeKJv2`
- `RIFE VFI`
- `VHS_VideoCombine`
- `Int`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **41%**（29/70）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`wanBlockSwap`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`RIFE VFI`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
