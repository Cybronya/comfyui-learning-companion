---
key: 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json
name: WAN2.2图生视频终极版_2083953699881316354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json
hash: 7e10d8976f5c7441
coverage: 0.53012
learned_at: 2026-10-16 19:17:21
nodes: [ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, INTConstant, PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, Note, INTConstant, Int, KSamplerAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Int, Reroute, Reroute, Reroute, Reroute, CompressImages, CreateVideo, Reroute, Reroute, Reroute, PreviewImage, Reroute, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, Reroute, VAELoader, Reroute, Reroute, Note, Note, Note, ModelSamplingSD3, ModelSamplingSD3, Note, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Reroute, Reroute, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, Reroute, WanImageToVideo, Note, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, VAEDecode, easy cleanGpuUsed, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, CR Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `INTConstant`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Note`
- `INTConstant`
- `Int`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CompressImages`
- `CreateVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Reroute`
- `WanImageToVideo`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CR Text`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **53%**（44/83）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`INTConstant`、`CLIPLoader`、`Int`、`KSamplerAdvanced`、`CompressImages`、`CreateVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`UNETLoader`、`WanImageToVideo`、`VAEDecode`、`easy cleanGpuUsed`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
