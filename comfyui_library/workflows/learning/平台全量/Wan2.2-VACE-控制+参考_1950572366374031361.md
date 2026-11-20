---
key: 平台全量/Wan2.2-VACE-控制+参考_1950572366374031361.json
name: Wan2.2-VACE-控制+参考_1950572366374031361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-VACE-控制+参考_1950572366374031361.json
hash: 5831bfa2addea093
coverage: 1
learned_at: 2026-11-14 01:06:04
nodes: [INTConstant, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, easy seed, VHS_LoadVideo, easy int, INTConstant, CLIPTextEncode, AIO_Preprocessor, GetImageSizeAndCount, ImageResizeKJ, String Literal, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2-VACE-控制+参考_1950572366374031361.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-VACE-控制+参考_1950572366374031361.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `INTConstant`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
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
- `VHS_LoadVideo`
- `easy int`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `String Literal`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`INTConstant`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAELoader`、`UnetLoaderGGUF`、`easy seed`、`VHS_LoadVideo`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`ImageResizeKJ`、`String Literal`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、CFGZeroStarAndInit、easy seed
