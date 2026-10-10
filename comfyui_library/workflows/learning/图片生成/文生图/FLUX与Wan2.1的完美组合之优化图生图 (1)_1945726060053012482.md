---
key: FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json
name: FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json
hash: 2cb126eb0de02027
coverage: 0.827586
learned_at: 2026-10-10 20:58:32
nodes: [VAEDecode, CLIPTextEncode, EmptySD3LatentImage, KSampler, CLIPTextEncode, FluxGuidance, UNETLoader, DualCLIPLoader, VAELoader, easy cleanGpuUsed, Lora Loader Stack (rgthree), TeaCache, VAELoader, CLIPLoader, CLIPTextEncode, RH_Translator, LayerUtility: ImageReel, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, WanVideoNAG, VAEEncode, ModelSamplingSD3, KSampler, LayerUtility: ImageReelComposit, VAEDecode, PreviewImage, SaveImage]
patterns: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy cleanGpuUsed, Lora Loader Stack (rgthree)]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 666, "steps": 10}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `Lora Loader Stack (rgthree)`
- `TeaCache`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `666`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`FluxGuidance`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`TeaCache`、`CLIPLoader`、`RH_Translator`、`LoraLoaderModelOnly`、`WanVideoNAG`、`VAEEncode`、`ModelSamplingSD3`、`SaveImage`

**缺卡**（4）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy cleanGpuUsed`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
