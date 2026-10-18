---
key: 视频生成/图生视频/Wan2.2+Remix+V3+图生视频-最新版_2065249355430449154.json
name: Wan2.2+Remix+V3+图生视频-最新版_2065249355430449154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Remix+V3+图生视频-最新版_2065249355430449154.json
hash: 6edde19c71fa21ac
coverage: 1
learned_at: 2026-10-15 22:39:37
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, INTConstant, INTConstant, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, Wan22PromptSelector, LoadImage, CR Text, VAELoader, Text Concatenate]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+Remix+V3+图生视频-最新版_2065249355430449154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065249355430449154.json`

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
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `LoadImage`
- `CR Text`
- `VAELoader`
- `Text Concatenate`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`INTConstant`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`UNETLoader`、`VHS_VideoCombine`、`Wan22PromptSelector`、`LoadImage`、`CR Text`、`VAELoader`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
