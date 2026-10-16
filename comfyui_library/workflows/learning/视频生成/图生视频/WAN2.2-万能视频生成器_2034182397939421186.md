---
key: 视频生成/图生视频/WAN2.2-万能视频生成器_2034182397939421186.json
name: WAN2.2-万能视频生成器_2034182397939421186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034182397939421186.json
hash: 21ed2355bfbeb890
coverage: 0.642857
learned_at: 2026-10-15 22:35:43
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, LoadImage, LoraLoaderModelOnly, INTConstant, INTConstant, UNETLoader, Fast Groups Bypasser (rgthree), Note, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, Reroute, VHS_VideoCombine, FL_RIFE, INTConstant, Reroute, MathExpression|pysssss, RH_LLMAPI_Pro_Node, ShowText|pysssss, VHS_VideoCombine, Reroute, GetImageRangeFromBatch, VHS_LoadVideo, PreviewImage, INTConstant, CR Text, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2-万能视频生成器_2034182397939421186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034182397939421186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Reroute`
- `VHS_VideoCombine`
- `FL_RIFE`
- `INTConstant`
- `Reroute`
- `MathExpression|pysssss`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `Reroute`
- `GetImageRangeFromBatch`
- `VHS_LoadVideo`
- `PreviewImage`
- `INTConstant`
- `CR Text`
- `INTConstant`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **64%**（36/56）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoadImage`、`LoraLoaderModelOnly`、`INTConstant`、`UNETLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`FL_RIFE`、`MathExpression|pysssss`、`RH_LLMAPI_Pro_Node`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
