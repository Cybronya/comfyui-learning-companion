---
key: 视频生成/图生视频/wan2.2_首尾帧_1993648600257413122.json
name: wan2.2_首尾帧_1993648600257413122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_首尾帧_1993648600257413122.json
hash: 95fbe0c8e6f734b2
coverage: 0.9
learned_at: 2026-10-15 22:33:19
nodes: [ImpactInt, ImpactInt, PathchSageAttentionKJ, PathchSageAttentionKJ, Seed (rgthree), VHS_VideoCombine, wanBlockSwap, wanBlockSwap, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, easy clearCacheAll, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), easy clearCacheAll, WanMoeKSampler, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, WanFirstLastFrameToVideo, MathExpression|pysssss, CLIPTextEncode, GetNode, CLIPTextEncode, easy imageSize, Note, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImpactInt, ImpactInt, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), VAEDecode, ImageLoader, MultiplePathsInput, easy clearCacheAll, SetNode, ImageLoader, ShowAnything|Mie, Qwen3_VQA, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_首尾帧_1993648600257413122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993648600257413122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
- `ImpactInt`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy clearCacheAll`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `easy clearCacheAll`
- `WanMoeKSampler` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanFirstLastFrameToVideo`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `ImageLoader`
- `MultiplePathsInput`
- `easy clearCacheAll`
- `SetNode`
- `ImageLoader`
- `ShowAnything|Mie`
- `Qwen3_VQA`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`ImpactInt`、`PathchSageAttentionKJ`、`Seed (rgthree)`、`VHS_VideoCombine`、`wanBlockSwap`、`RIFE VFI`、`easy clearCacheAll`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`WanMoeKSampler`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`MathExpression|pysssss`、`CLIPTextEncode`、`easy imageSize`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageLoader`、`MultiplePathsInput`、`ShowAnything|Mie`、`Qwen3_VQA`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
