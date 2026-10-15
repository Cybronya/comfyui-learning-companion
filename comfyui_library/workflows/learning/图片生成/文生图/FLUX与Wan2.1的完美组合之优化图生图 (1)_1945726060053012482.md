---
key: 图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json
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

# 图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX与Wan2.1的完美组合之优化图生图 (1)_1945726060053012482.json`

## 结构

**节点**（29 个）：
- `VAEDecode`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `CLIPTextEncode`
- `FluxGuidance`
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `Lora Loader Stack (rgthree)`
- `TeaCache`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `RH_Translator`
- `LayerUtility: ImageReel`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `WanVideoNAG`
- `VAEEncode`
- `ModelSamplingSD3`
- `KSampler`
- `LayerUtility: ImageReelComposit`
- `VAEDecode`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.20000000000000004`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `666`
- `steps` = `10`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`FluxGuidance`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`easy cleanGpuUsed`、`Lora Loader Stack (rgthree)`、`TeaCache`、`CLIPLoader`、`RH_Translator`、`LayerUtility: ImageReel`、`LoraLoaderModelOnly`、`WanVideoNAG`、`VAEEncode`、`ModelSamplingSD3`

**缺卡**（4）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy cleanGpuUsed`、`Lora Loader Stack (rgthree)`

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
