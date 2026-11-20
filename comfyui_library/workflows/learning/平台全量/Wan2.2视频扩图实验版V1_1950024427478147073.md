---
key: 平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json
name: Wan2.2视频扩图实验版V1_1950024427478147073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json
hash: 8adc3d0ee73eb16d
coverage: 0.8
learned_at: 2026-11-14 01:06:24
nodes: [MarkdownNote, MaskToImage, RepeatImageBatch, ImageToMask, CLIPTextEncode, PathchSageAttentionKJ, UnetLoaderGGUF, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, UnetLoaderGGUF, WanVaceToVideo, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, GetVideoComponents, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, PreviewImage, PreviewImage, JWInteger, JWInteger, Note, Note, PrimitiveNode, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, CLIPLoader, VAELoader, TrimVideoLatent]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2视频扩图实验版V1_1950024427478147073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `MarkdownNote`
- `MaskToImage`
- `RepeatImageBatch`
- `ImageToMask`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `GetVideoComponents`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `PreviewImage`
- `PreviewImage`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `CLIPLoader`
- `VAELoader`
- `TrimVideoLatent`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`MaskToImage`、`RepeatImageBatch`、`ImageToMask`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`WanVaceToVideo`、`ModelSamplingSD3`、`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`JWInteger`、`VHS_VideoCombine`、`KSamplerAdvanced`、`VAEDecode`、`VHS_LoadVideo`、`CLIPLoader`、`VAELoader`、`TrimVideoLatent`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、KSamplerAdvanced、TrimVideoLatent、GetVideoComponents
