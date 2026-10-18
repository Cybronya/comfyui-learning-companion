---
key: 视频生成/图生视频/Wan2.2 Remix V3 图生视频 + 补帧_2055185537719390209.json
name: Wan2.2 Remix V3 图生视频 + 补帧_2055185537719390209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix V3 图生视频 + 补帧_2055185537719390209.json
hash: 08ad74d936b6a231
coverage: 1
learned_at: 2026-10-15 22:37:56
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, SimpleMath+, INTConstant, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CR Text, INTConstant, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix V3 图生视频 + 补帧_2055185537719390209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055185537719390209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `INTConstant`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `INTConstant`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`SimpleMath+`、`INTConstant`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`UNETLoader`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
