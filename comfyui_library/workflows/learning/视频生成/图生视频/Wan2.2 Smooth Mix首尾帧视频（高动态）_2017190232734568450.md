---
key: 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json
name: Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017190232734568450.json
hash: fa091100bc09115a
coverage: 0.773585
learned_at: 2026-10-15 22:34:45
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, LoadImage, CLIPVisionEncode, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, ImageResizeKJ, MathExpression|pysssss, JWInteger, VHS_VideoCombine, ImpactSwitch, GetNode, Fast Groups Bypasser (rgthree), Note, CLIPTextEncode, JWInteger, RH_LLMAPI_NODE, CLIPTextEncode, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy showAnything, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_2017190232734568450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017190232734568450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（53 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `SeedVR2GGUF`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `JWInteger`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy showAnything`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（41/53）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`UNETLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`SeedVR2GGUF`、`LoadImage`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VAEDecode`、`ImageConcanate`、`CLIPLoader`、`VAELoader`、`ImageResizeKJ`、`MathExpression|pysssss`、`JWInteger`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
