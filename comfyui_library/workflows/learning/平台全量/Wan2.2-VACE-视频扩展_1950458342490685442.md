---
key: 平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json
name: Wan2.2-VACE-视频扩展_1950458342490685442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json
hash: ca2e0abe5ef4c997
coverage: 1
learned_at: 2026-11-14 01:06:04
nodes: [CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, easy seed, MaskToImage, INTConstant, String Literal, INTConstant, ImagePadKJ, GetImageSize+, ImageResizeKJ, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, JWImageExtractFromBatch]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `easy seed`
- `MaskToImage`
- `INTConstant`
- `String Literal`
- `INTConstant`
- `ImagePadKJ`
- `GetImageSize+`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `JWImageExtractFromBatch`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAELoader`、`UnetLoaderGGUF`、`easy seed`、`MaskToImage`、`INTConstant`、`String Literal`、`ImagePadKJ`、`GetImageSize+`、`ImageResizeKJ`、`VHS_VideoCombine`、`VHS_LoadVideo`、`JWImageExtractFromBatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、CFGZeroStarAndInit、easy seed、KSamplerAdvanced
