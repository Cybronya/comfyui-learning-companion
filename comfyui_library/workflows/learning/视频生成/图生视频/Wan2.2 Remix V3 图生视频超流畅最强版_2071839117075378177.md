---
key: 视频生成/图生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2071839117075378177.json
name: Wan2.2 Remix V3 图生视频超流畅最强版_2071839117075378177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071839117075378177.json
hash: bef15b98daf0101f
coverage: 1
learned_at: 2026-10-15 22:40:48
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, Wan22PromptSelector, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, INTConstant, INTConstant, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2071839117075378177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071839117075378177.json`

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
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `Wan22PromptSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
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

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`Wan22PromptSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`INTConstant`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`UNETLoader`、`Text Concatenate`、`VHS_VideoCombine`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
