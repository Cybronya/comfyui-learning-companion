---
key: 视频生成/图生视频/Wan2.2 Remix V3 图生视频_2064270207278993409.json
name: Wan2.2 Remix V3 图生视频_2064270207278993409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064270207278993409.json
hash: 36ce10c52996eeb0
coverage: 1
learned_at: 2026-10-15 22:39:23
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPLoader, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, SimpleMath+, INTConstant, ImageScaleBy, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VHS_VideoCombine, RIFE VFI, easy cleanGpuUsed, VHS_VideoCombine, Wan22PromptSelector, Text Concatenate, INTConstant, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix V3 图生视频_2064270207278993409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064270207278993409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
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
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `INTConstant`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `Text Concatenate`
- `INTConstant`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`SimpleMath+`、`INTConstant`、`ImageScaleBy`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`RIFE VFI`、`easy cleanGpuUsed`、`Wan22PromptSelector`、`Text Concatenate`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
