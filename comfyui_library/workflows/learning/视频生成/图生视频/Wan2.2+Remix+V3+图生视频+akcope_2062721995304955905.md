---
key: 视频生成/图生视频/Wan2.2+Remix+V3+图生视频+akcope_2062721995304955905.json
name: Wan2.2+Remix+V3+图生视频+akcope_2062721995304955905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Remix+V3+图生视频+akcope_2062721995304955905.json
hash: f3f2e46131f2e781
coverage: 1
learned_at: 2026-10-15 22:39:07
nodes: [ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, CLIPLoader, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, CLIPTextEncode, INTConstant, ImageScaleBy, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, easy cleanGpuUsed, Text Concatenate, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, RIFE VFI, INTConstant, SimpleMath+, WanImageToVideo, VHS_VideoCombine, VHS_VideoCombine, Wan22PromptSelector, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+Remix+V3+图生视频+akcope_2062721995304955905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062721995304955905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `Text Concatenate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RIFE VFI`
- `INTConstant`
- `SimpleMath+`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`ModelSamplingSD3`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`CLIPTextEncode`、`INTConstant`、`ImageScaleBy`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`Text Concatenate`、`LoraLoaderModelOnly`、`RIFE VFI`、`SimpleMath+`、`WanImageToVideo`、`VHS_VideoCombine`、`Wan22PromptSelector`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
