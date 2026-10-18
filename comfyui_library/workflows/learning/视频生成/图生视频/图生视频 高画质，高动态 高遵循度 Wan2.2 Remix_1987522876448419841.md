---
key: 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json
name: 图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json
hash: 27383dfb7c7add70
coverage: 0.843137
learned_at: 2026-10-15 22:32:58
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, GetNode, GetNode, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, JWInteger, RIFE VFI, CLIPTextEncode, CLIPVisionLoader, CLIPTextEncode, JWInteger, WanImageToVideo, MathExpression|pysssss, CLIPVisionEncode, CLIPLoader, VAELoader, LoadImage, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VAEDecode, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, Note, CombinationText, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CR Text Input Switch (4 way), easy showAnything, Note, SetNode, SetNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, CR Text, AILab_QwenVL, easy cleanGpuUsed, RH_LLMAPI_NODE, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987522876448419841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `GetNode`
- `GetNode`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `WanImageToVideo`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
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
- `CR Text`
- `AILab_QwenVL`
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`JWInteger`、`RIFE VFI`、`CLIPTextEncode`、`CLIPVisionLoader`、`WanImageToVideo`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CombinationText`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CR Text Input Switch (4 way)`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CR Text`、`AILab_QwenVL`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
