---
key: 视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json
name: Wan2.2-remix+VQA 首尾帧_1988124359338389506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json
hash: 1f51f47d2ee55a31
coverage: 0.891304
learned_at: 2026-10-15 22:33:01
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, CLIPLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, WanFirstLastFrameToVideo, ModelPatchTorchSettings, KSamplerAdvanced, ModelPatchTorchSettings, SetNode, SetNode, LayerUtility: PurgeVRAM V2, VAEDecode, VHS_VideoCombine, SeedVR2GGUF, Qwen3_VQA_Plus, easy textSwitch, CLIPTextEncode, CLIPTextEncode, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, MathExpression|pysssss, easy showAnything, PreviewImage, Fast Groups Bypasser (rgthree), CR Text, LoadImage, LoadImage, CLIPVisionLoader, VAELoader, CLIPVisionEncode, CLIPVisionEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988124359338389506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanFirstLastFrameToVideo`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SeedVR2GGUF`
- `Qwen3_VQA_Plus`
- `easy textSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `MathExpression|pysssss`
- `easy showAnything`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`VHS_VideoCombine`、`RIFE VFI`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`WanFirstLastFrameToVideo`、`ModelPatchTorchSettings`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`SeedVR2GGUF`、`Qwen3_VQA_Plus`、`easy textSwitch`、`CLIPTextEncode`、`JWInteger`、`MathExpression|pysssss`、`CR Text`、`LoadImage`、`CLIPVisionLoader`、`VAELoader`、`CLIPVisionEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
