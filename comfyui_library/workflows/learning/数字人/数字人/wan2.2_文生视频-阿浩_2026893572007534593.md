---
key: 数字人/数字人/wan2.2_文生视频-阿浩_2026893572007534593.json
name: wan2.2_文生视频-阿浩_2026893572007534593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2_文生视频-阿浩_2026893572007534593.json
hash: 4f157a3912d2d7cb
coverage: 0.87234
learned_at: 2026-10-26 01:59:27
nodes: [ImpactInt, ImpactInt, PathchSageAttentionKJ, Seed (rgthree), VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, GetNode, VHS_VideoCombine, RIFE VFI, easy clearCacheAll, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy clearCacheAll, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, wanBlockSwap, CR Prompt Text, EmptyHunyuanLatentVideo, MathExpression|pysssss, CR Text Replace, Qwen3_VQA, easy cleanGpuUsed, easy cleanGpuUsed, easy showAnything, SetNode, CLIPTextEncode, Note, WanMoeKSampler, LoraLoaderModelOnly, ImpactInt, ImpactInt, VAELoader, VAEDecode, wanBlockSwap, PathchSageAttentionKJ, CLIPLoader, UNETLoader, UNETLoader, Label (rgthree), CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "fixed"}
---

# 数字人/数字人/wan2.2_文生视频-阿浩_2026893572007534593.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2_文生视频-阿浩_2026893572007534593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（47 个）：
- `ImpactInt`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy clearCacheAll`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy clearCacheAll`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `CR Prompt Text`
- `EmptyHunyuanLatentVideo`
- `MathExpression|pysssss`
- `CR Text Replace`
- `Qwen3_VQA`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy showAnything`
- `SetNode`
- `CLIPTextEncode` ★核心
- `Note`
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `ImpactInt`
- `VAELoader`
- `VAEDecode` ★核心
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Label (rgthree)`
- `CR Prompt Text`

## 关键参数

- `seed` = `0.875`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`ImpactInt`、`PathchSageAttentionKJ`、`Seed (rgthree)`、`VHS_VideoCombine`、`CLIPTextEncode`、`RIFE VFI`、`easy clearCacheAll`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`wanBlockSwap`、`CR Prompt Text`、`EmptyHunyuanLatentVideo`、`MathExpression|pysssss`、`CR Text Replace`、`Qwen3_VQA`、`easy cleanGpuUsed`、`WanMoeKSampler`、`VAELoader`、`VAEDecode`、`CLIPLoader`、`UNETLoader`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
