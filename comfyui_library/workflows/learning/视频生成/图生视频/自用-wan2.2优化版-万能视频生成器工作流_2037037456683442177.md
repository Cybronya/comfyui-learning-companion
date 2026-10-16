---
key: 视频生成/图生视频/自用-wan2.2优化版-万能视频生成器工作流_2037037456683442177.json
name: 自用-wan2.2优化版-万能视频生成器工作流_2037037456683442177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037037456683442177.json
hash: e7e545392d3e6d1e
coverage: 0.432432
learned_at: 2026-10-15 22:35:54
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, INTConstant, INTConstant, Int, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Int, Note, CLIPTextEncode, LoraLoaderModelOnly, Reroute, FL_RIFE, PreviewImage, RH_LLMAPI_Pro_Node, PreviewAny, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/自用-wan2.2优化版-万能视频生成器工作流_2037037456683442177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037037456683442177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
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
- `CLIPLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
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
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `Int`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Note`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `FL_RIFE`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **43%**（32/74）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`FL_RIFE`、`RH_LLMAPI_Pro_Node`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
