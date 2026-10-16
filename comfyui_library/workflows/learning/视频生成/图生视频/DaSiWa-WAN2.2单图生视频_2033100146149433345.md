---
key: 视频生成/图生视频/DaSiWa-WAN2.2单图生视频_2033100146149433345.json
name: DaSiWa-WAN2.2单图生视频_2033100146149433345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033100146149433345.json
hash: 826e97d3290ba86b
coverage: 0.852941
learned_at: 2026-10-15 22:35:38
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, Int, Int, INTConstant, INTConstant, CLIPTextEncode, PainterI2V, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, Reroute, Reroute, PreviewImage, VAEDecode, easy cleanGpuUsed, RIFE VFI, GetImagesFromBatchIndexed, LoadImage, Fast Groups Bypasser (rgthree), CLIPTextEncode, VHS_VideoCombine, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/DaSiWa-WAN2.2单图生视频_2033100146149433345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033100146149433345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Int`
- `Int`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `PainterI2V`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RIFE VFI`
- `GetImagesFromBatchIndexed`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PreviewImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`Int`、`INTConstant`、`CLIPTextEncode`、`PainterI2V`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`RIFE VFI`、`GetImagesFromBatchIndexed`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
