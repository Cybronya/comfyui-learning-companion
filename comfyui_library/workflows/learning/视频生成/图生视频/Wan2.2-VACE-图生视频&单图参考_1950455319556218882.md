---
key: 视频生成/图生视频/Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json
name: Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json
hash: 902b4fd3addedd56
coverage: 1
learned_at: 2026-10-15 22:30:55
nodes: [CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, VHS_VideoCombine, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, String Literal, String Literal, easy seed, LoadImage, KSamplerAdvanced, WanVaceToVideo, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-VACE-图生视频&单图参考_1950455319556218882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950455319556218882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（63 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_VideoCombine`
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
- `INTConstant`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
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
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `String Literal`
- `String Literal`
- `easy seed`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `WanVaceToVideo`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（63/63）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`ImageResizeKJ`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`TrimVideoLatent`、`VHS_VideoCombine`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAELoader`、`UnetLoaderGGUF`、`String Literal`、`easy seed`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CFGZeroStarAndInit
