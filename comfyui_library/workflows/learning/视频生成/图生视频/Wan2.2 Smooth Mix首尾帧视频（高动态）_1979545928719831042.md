---
key: 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json
name: Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979545928719831042.json
hash: f77d726a21d67f33
coverage: 0.773585
learned_at: 2026-10-15 22:32:24
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, UNETLoader, UNETLoader, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, LoadImage, CR Text, RH_LLMAPI_NODE, ImageConcanate, CLIPVisionEncode, CLIPVisionLoader, WanFirstLastFrameToVideo, CLIPVisionEncode, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, SetNode, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, VHS_VideoCombine, ImpactSwitch, GetNode, Note, easy showAnything, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1979545928719831042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979545928719831042.json`

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
- `CR Text`
- `RH_LLMAPI_NODE`
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
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
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
- `GetNode`
- `Note`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（41/53）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`UNETLoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`SeedVR2GGUF`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`CLIPVisionEncode`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
