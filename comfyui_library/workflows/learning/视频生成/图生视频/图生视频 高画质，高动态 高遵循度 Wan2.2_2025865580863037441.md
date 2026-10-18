---
key: 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json
name: 图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json
hash: 6070c33287d4eb36
coverage: 0.846154
learned_at: 2026-10-15 22:35:13
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, GetNode, GetNode, SeedVR2GGUF, VHS_VideoCombine, JWInteger, CLIPTextEncode, CLIPVisionLoader, CLIPTextEncode, JWInteger, WanImageToVideo, MathExpression|pysssss, CLIPVisionEncode, CLIPLoader, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, Note, CombinationText, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CR Text Input Switch (4 way), easy showAnything, Note, SetNode, SetNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, AILab_QwenVL, easy cleanGpuUsed, RH_LLMAPI_NODE, easy cleanGpuUsed, VAELoader, VHS_VideoCombine, Fast Groups Bypasser (rgthree), RIFE VFI, CompressImages, VHS_VideoCombine, VAEDecode, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025865580863037441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（52 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `GetNode`
- `GetNode`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `CombinationText`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CR Text Input Switch (4 way)`
- `easy showAnything`
- `Note`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `AILab_QwenVL`
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `VAELoader`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `RIFE VFI`
- `CompressImages`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（44/52）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`JWInteger`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanImageToVideo`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CombinationText`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CR Text Input Switch (4 way)`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`AILab_QwenVL`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`、`VAELoader`、`RIFE VFI`、`CompressImages`、`VAEDecode`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
