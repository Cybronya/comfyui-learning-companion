---
key: 视频生成/图生视频/wan2.2首尾帧生视频_2029550515125755905.json
name: wan2.2首尾帧生视频_2029550515125755905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首尾帧生视频_2029550515125755905.json
hash: 55f8bd595151a319
coverage: 0.672131
learned_at: 2026-10-15 22:35:22
nodes: [Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PreviewImage, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAEDecode, easy cleanGpuUsed, PreviewAny, Reroute, RH_LLMAPI_NODE, easy float, easy cleanGpuUsed, Note, SimpleMath+, HunyuanVideoFoley, RH_LLMAPI_Pro_Node, WanFirstLastFrameToVideo, INTConstant, INTConstant, Float, Note, Note, Note, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAELoader, JWInteger, FL_RIFE, LoadImage, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首尾帧生视频_2029550515125755905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029550515125755905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PreviewImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewAny`
- `Reroute`
- `RH_LLMAPI_NODE`
- `easy float`
- `easy cleanGpuUsed`
- `Note`
- `SimpleMath+`
- `HunyuanVideoFoley`
- `RH_LLMAPI_Pro_Node`
- `WanFirstLastFrameToVideo`
- `INTConstant`
- `INTConstant`
- `Float`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `JWInteger`
- `FL_RIFE`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **67%**（41/61）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoraLoaderModelOnly`、`Int`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`、`easy float`、`SimpleMath+`、`HunyuanVideoFoley`、`RH_LLMAPI_Pro_Node`、`WanFirstLastFrameToVideo`、`INTConstant`、`Float`、`VHS_VideoCombine`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`JWInteger`、`FL_RIFE`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
