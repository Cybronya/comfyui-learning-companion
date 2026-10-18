---
key: 视频生成/图生视频/wan2.2万能视频生成_2032814460473188353.json
name: wan2.2万能视频生成_2032814460473188353.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2万能视频生成_2032814460473188353.json
hash: e64b53607ae55676
coverage: 0.438356
learned_at: 2026-10-15 22:35:37
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, INTConstant, INTConstant, Int, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Int, CLIPTextEncode, LoraLoaderModelOnly, Reroute, FL_RIFE, PreviewImage, PreviewAny, LoadImage, Note, Note, CR Text, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2万能视频生成_2032814460473188353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032814460473188353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

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
- `Reroute`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
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
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `FL_RIFE`
- `PreviewImage`
- `PreviewAny`
- `LoadImage`
- `Note`
- `Note`
- `CR Text`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **44%**（32/73）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`FL_RIFE`、`LoadImage`、`CR Text`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
