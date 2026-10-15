---
key: 视频生成/文生视频/Wan2.2-VACE-首尾帧_2072999665202929664.json
name: Wan2.2-VACE-首尾帧_2072999665202929664
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-首尾帧_2072999665202929664.json
hash: 644a09dd6c965cf4
coverage: 1
learned_at: 2026-10-15 22:47:13
nodes: [CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, ImageResizeKJ, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, String Literal, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2-VACE-首尾帧_2072999665202929664.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-首尾帧_2072999665202929664.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
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
- `String Literal`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`ImageResizeKJ`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`String Literal`、`VAELoader`、`UnetLoaderGGUF`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CFGZeroStarAndInit
