---
key: 视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json
name: 嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988086364040310785.json
hash: a661a9106ce23747
coverage: 0.833333
learned_at: 2026-10-15 22:33:01
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, RIFE VFI, GetNode, SeedVR2GGUF, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, GetNode, JWInteger, GetNode, GetNode, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, UNETLoader, PathchSageAttentionKJ, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, wanBlockSwap, VAELoader, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, MathExpression|pysssss, CLIPLoader, SetNode, SetNode, CR Text, RH_LLMAPI_NODE, Note, ImageConcanate, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, ImageScaleToTotalPixels, ImageBatchMulti, ImageConcatMulti, easy showAnything, WanMultiFrameRefToVideo, JWInteger, VAEDecode, VHS_VideoCombine, ImageConcatMulti, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, ImageResizeKJ, WanFirstMiddleLastFrameToVideo, VHS_VideoCombine, ImpactSwitch, WanMultiFrameRefToVideo, WanMultiFrameRefToVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988086364040310785.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（72 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `RIFE VFI`
- `GetNode`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
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
- `MathExpression|pysssss`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `CR Text`
- `RH_LLMAPI_NODE`
- `Note`
- `ImageConcanate`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `easy showAnything`
- `WanMultiFrameRefToVideo`
- `JWInteger`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanFirstMiddleLastFrameToVideo`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `WanMultiFrameRefToVideo`
- `WanMultiFrameRefToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（60/72）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`RIFE VFI`、`SeedVR2GGUF`、`CLIPTextEncode`、`JWInteger`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`wanBlockSwap`、`LoraLoaderModelOnly`、`VAELoader`、`MathExpression|pysssss`、`CLIPLoader`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`LoadImage`、`ImageScaleToTotalPixels`、`ImageBatchMulti`、`ImageConcatMulti`、`WanMultiFrameRefToVideo`、`VAEDecode`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
