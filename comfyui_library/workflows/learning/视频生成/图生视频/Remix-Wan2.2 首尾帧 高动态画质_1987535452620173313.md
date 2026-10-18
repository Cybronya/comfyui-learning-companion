---
key: 视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json
name: Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json
hash: ed7da5451bdfff12
coverage: 0.826923
learned_at: 2026-10-15 22:32:59
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, GetNode, GetNode, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, JWInteger, RIFE VFI, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, ModelSamplingSD3, SetNode, wanBlockSwap, wanBlockSwap, SetNode, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, Note, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, easy textSwitch, easy showAnything, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, JWInteger, Note, VAEDecode, LoadImage, MathExpression|pysssss, VHS_VideoCombine, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, ImageConcatMulti, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987535452620173313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `wanBlockSwap`
- `wanBlockSwap`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy textSwitch`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `JWInteger`
- `Note`
- `VAEDecode` ★核心
- `LoadImage`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageConcatMulti`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_NODE`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`JWInteger`、`RIFE VFI`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`wanBlockSwap`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`easy textSwitch`、`VAEDecode`、`LoadImage`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`KSamplerAdvanced`、`LayerUtility: PurgeVRAM V2`、`RH_LLMAPI_NODE`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
