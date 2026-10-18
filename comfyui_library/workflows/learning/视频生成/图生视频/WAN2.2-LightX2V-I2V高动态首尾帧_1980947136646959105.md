---
key: 视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json
name: WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json
hash: aea5555aa76a5e8a
coverage: 0.789474
learned_at: 2026-10-15 22:32:35
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, RIFE VFI, GetNode, KSamplerAdvanced, KSamplerAdvanced, SeedVR2GGUF, LoadImage, CR Text, ImageConcanate, CLIPVisionEncode, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, VHS_VideoCombine, ImpactSwitch, UNETLoader, CLIPLoader, ModelPatchTorchSettings, wanBlockSwap, ModelSamplingSD3, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, VAELoader, LoraLoaderModelOnly, UNETLoader, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE, Note, ModelSamplingSD3, easy showAnything, VHS_VideoCombine, GetNode, GetNode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-LightX2V-I2V高动态首尾帧_1980947136646959105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980947136646959105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `RIFE VFI`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SeedVR2GGUF`
- `LoadImage`
- `CR Text`
- `ImageConcanate`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`
- `Note`
- `ModelSamplingSD3`
- `easy showAnything`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **79%**（45/57）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`、`SeedVR2GGUF`、`LoadImage`、`CR Text`、`ImageConcanate`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPTextEncode`、`ImageResizeKJ`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`UNETLoader`、`CLIPLoader`、`ModelPatchTorchSettings`、`wanBlockSwap`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
