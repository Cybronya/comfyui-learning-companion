---
key: 视频生成/图生视频/wan2.2_图生视频_1993607152562536450.json
name: wan2.2_图生视频_1993607152562536450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2_图生视频_1993607152562536450.json
hash: ebe598bbd8922a6b
coverage: 0.86
learned_at: 2026-10-15 22:33:19
nodes: [MultiplePathsInput, ImpactInt, ImpactInt, WanImageToVideo, PathchSageAttentionKJ, PathchSageAttentionKJ, Seed (rgthree), CR Prompt Text, CR Prompt Text, VHS_VideoCombine, wanBlockSwap, easy clearCacheAll, VHS_VideoCombine, CLIPTextEncode, GetNode, CLIPTextEncode, SetNode, easy showAnything, ImageResizeKJv2, PreviewImage, CR Text Concatenate, easy clearCacheAll, VHS_VideoCombine, easy clearCacheAll, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MathExpression|pysssss, easy clearCacheAll, WanMoeKSampler, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, Note, ImageLoader, ImpactInt, ImpactInt, Qwen3_VQA, UNETLoader, UNETLoader, CLIPLoader, VAELoader, wanBlockSwap, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2_图生视频_1993607152562536450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993607152562536450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `MultiplePathsInput`
- `ImpactInt`
- `ImpactInt`
- `WanImageToVideo`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `CR Prompt Text`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `easy showAnything`
- `ImageResizeKJv2`
- `PreviewImage`
- `CR Text Concatenate`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MathExpression|pysssss`
- `easy clearCacheAll`
- `WanMoeKSampler` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `ImageLoader`
- `ImpactInt`
- `ImpactInt`
- `Qwen3_VQA`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `wanBlockSwap`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RIFE VFI`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **86%**（43/50）

**有卡**：`MultiplePathsInput`、`ImpactInt`、`WanImageToVideo`、`PathchSageAttentionKJ`、`Seed (rgthree)`、`CR Prompt Text`、`VHS_VideoCombine`、`wanBlockSwap`、`easy clearCacheAll`、`CLIPTextEncode`、`ImageResizeKJv2`、`CR Text Concatenate`、`SeedVR2VideoUpscaler`、`MathExpression|pysssss`、`WanMoeKSampler`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`ImageLoader`、`Qwen3_VQA`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEDecode`、`LoraLoaderModelOnly`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
