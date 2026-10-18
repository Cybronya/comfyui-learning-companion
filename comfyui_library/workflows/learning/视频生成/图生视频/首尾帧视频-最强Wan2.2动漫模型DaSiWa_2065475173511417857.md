---
key: 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json
name: 首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json
hash: faf8e746fb01cd27
coverage: 0.777778
learned_at: 2026-10-15 22:39:41
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, RIFE VFI, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, GetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, SeedVR2GGUF, LoadImage, CR Text, RH_LLMAPI_NODE, ImageConcanate, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPVisionEncode, LoadImage, VHS_VideoCombine, VAEDecode, ImageConcanate, ImageConcanate, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, GetNode, UNETLoader, UNETLoader, CLIPVisionLoader, MathExpression|pysssss, SetNode, KSamplerAdvanced, Fast Groups Bypasser (rgthree), ImpactSwitch, Note, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, KSamplerAdvanced, JWInteger, JWInteger, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065475173511417857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
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
- `GetNode`
- `GetNode`
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
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `MathExpression|pysssss`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`
- `Note`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `JWInteger`
- `JWInteger`
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`RIFE VFI`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SeedVR2GGUF`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPVisionLoader`、`MathExpression|pysssss`、`KSamplerAdvanced`、`JWInteger`、`Int`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
