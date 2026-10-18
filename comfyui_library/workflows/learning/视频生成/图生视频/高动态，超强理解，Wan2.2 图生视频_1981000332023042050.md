---
key: 视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json
name: 高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json
hash: 3cea7e1ed3270d5c
coverage: 0.851064
learned_at: 2026-10-15 22:32:36
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, RIFE VFI, VAEDecode, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, WanImageToVideo, CLIPTextEncode, MathExpression|pysssss, CLIPVisionEncode, CLIPVisionLoader, CLIPTextEncode, JWInteger, LoadImage, easy showAnything, Note, CR Text Input Switch, CR Text, VHS_VideoCombine, RH_LLMAPI_NODE, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, JWInteger, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, wanBlockSwap, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981000332023042050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `RIFE VFI`
- `VAEDecode` ★核心
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LoadImage`
- `easy showAnything`
- `Note`
- `CR Text Input Switch`
- `CR Text`
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（40/47）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`RIFE VFI`、`VAEDecode`、`SeedVR2GGUF`、`VHS_VideoCombine`、`WanImageToVideo`、`CLIPTextEncode`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPVisionLoader`、`JWInteger`、`LoadImage`、`CR Text Input Switch`、`CR Text`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`wanBlockSwap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
