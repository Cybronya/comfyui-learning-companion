---
key: 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json
name: Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json
hash: 64dab648233d556a
coverage: 0.833333
learned_at: 2026-10-15 22:39:58
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, RIFE VFI, SeedVR2GGUF, VHS_VideoCombine, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, VAELoader, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, CLIPLoader, SetNode, SetNode, ImageConcanate, VHS_VideoCombine, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, ImageResizeKJ, JWInteger, Fast Groups Bypasser (rgthree), JWInteger, KSamplerAdvanced, RHHiddenNodes, ImageConcatMulti, ImageScaleToTotalPixels, MathExpression|pysssss, ImageBatchMulti, WanFirstMiddleLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, WanMultiFrameRefToVideo, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CR Text, Note, ImpactSwitch, easy showAnything, CLIPTextEncode, CLIPTextEncode, WanMultiFrameRefToVideo, WanMultiFrameRefToVideo, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067206177418727425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（72 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `RIFE VFI`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `JWInteger`
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `RHHiddenNodes`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `MathExpression|pysssss`
- `ImageBatchMulti`
- `WanFirstMiddleLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `WanMultiFrameRefToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `Note`
- `ImpactSwitch`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanMultiFrameRefToVideo`
- `WanMultiFrameRefToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（60/72）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`RIFE VFI`、`SeedVR2GGUF`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ImageConcanate`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`JWInteger`、`KSamplerAdvanced`、`RHHiddenNodes`、`ImageScaleToTotalPixels`、`MathExpression|pysssss`、`ImageBatchMulti`、`WanFirstMiddleLastFrameToVideo`、`VAEDecode`、`WanMultiFrameRefToVideo`、`CR Text`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
