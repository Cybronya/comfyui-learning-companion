---
key: 图片生成/图生图/Z-image+Wan 2.2 -质感增强洗图_2008574605040029697.json
name: Z-image+Wan 2.2 -质感增强洗图_2008574605040029697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image+Wan 2.2 -质感增强洗图_2008574605040029697.json
hash: 2479fe8b58da42a2
coverage: 0.809524
learned_at: 2026-10-23 11:30:45
nodes: [UNETLoader, CLIPTextEncode, VAELoader, SplitSigmas, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CFGGuider, CLIPLoader, LoraLoaderModelOnly, WanVideoNAG, VAEEncode, RandomNoise, Image Comparer (rgthree), SamplerCustomAdvanced, VAEDecode, DisableNoise, BasicScheduler, easy cleanGpuUsed, CLIPTextEncode, easy showAnything, CheckpointLoaderSimple, VAEEncode, CLIPTextEncode, ConditioningZeroOut, DyPE_FLUX, PreviewImage, Reroute, PrimitiveInt, SeedVR2, LoraLoaderModelOnly, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, ResizeShortestToNode, Image Comparer (rgthree), Reroute, ImageLoader, Image Comparer (rgthree), KSampler, Qwen3_VQA, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 0.4000000000000001, "sampler_name": "dpmpp_2m_sde", "scheduler": "sgm_uniform", "seed": 148676371464194, "steps": 10}
---

# 图片生成/图生图/Z-image+Wan 2.2 -质感增强洗图_2008574605040029697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image+Wan 2.2 -质感增强洗图_2008574605040029697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（42 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `WanVideoNAG`
- `VAEEncode` ★核心
- `RandomNoise`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `DisableNoise`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `DyPE_FLUX`
- `PreviewImage`
- `Reroute`
- `PrimitiveInt`
- `SeedVR2`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ResizeShortestToNode`
- `Image Comparer (rgthree)`
- `Reroute`
- `ImageLoader`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `Qwen3_VQA`
- `SaveImage`

## 关键参数

- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`
- `seed` = `148676371464194`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`SplitSigmas`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`LoraLoaderModelOnly`、`WanVideoNAG`、`VAEEncode`、`RandomNoise`、`VAEDecode`、`DisableNoise`、`BasicScheduler`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`ConditioningZeroOut`、`DyPE_FLUX`、`SeedVR2`、`ResizeShortestToNode`、`ImageLoader`、`KSampler`、`Qwen3_VQA`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
