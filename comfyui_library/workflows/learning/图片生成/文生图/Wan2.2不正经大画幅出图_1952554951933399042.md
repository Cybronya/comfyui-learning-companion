---
key: 图片生成/文生图/Wan2.2不正经大画幅出图_1952554951933399042.json
name: Wan2.2不正经大画幅出图_1952554951933399042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2不正经大画幅出图_1952554951933399042.json
hash: 46d9aee0d9c95d7d
coverage: 0.730769
learned_at: 2026-10-10 20:59:14
nodes: [ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ModelSamplingSD3, CLIPLoader, VAELoader, Prompts Everywhere, ImageFromBatch, ImageConcanateOfUtils, ImageConcanateOfUtils, ImageUpscaleWithModel, Image Tiled, GetNode, SetNode, ImageConcanateOfUtils, SetNode, SetNode, ModelSamplingSD3, Anything Everywhere3, VAEDecode, GetNode, Seed Everywhere, Note, CLIPTextEncode, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, UNETLoader, KSampler, ImageScaleBy, ImageUpscaleWithModel, GetNode, VAEEncode, GetImagesFromBatchIndexed, VAEDecode, EmptyHunyuanLatentVideo, KSampler, PreviewImage, LoraLoaderModelOnly, UpscaleModelLoader, Fast Groups Bypasser (rgthree), LoadImage, UpscaleModelLoader, CLIPTextEncode, SaveImage, SaveImage]
patterns: [image_to_image]
missing: [Image Tiled, Prompts Everywhere, Seed Everywhere]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 202789835509806, "steps": 6}
discoveries: [次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识, 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2不正经大画幅出图_1952554951933399042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2不正经大画幅出图_1952554951933399042.json`

## 结构

**节点**（52 个）：
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `Prompts Everywhere`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `ImageUpscaleWithModel`
- `Image Tiled`
- `GetNode`
- `SetNode`
- `ImageConcanateOfUtils`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `Anything Everywhere3`
- `VAEDecode`
- `GetNode`
- `Seed Everywhere`
- `Note`
- `CLIPTextEncode`
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `UNETLoader`
- `KSampler`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `GetNode`
- `VAEEncode`
- `GetImagesFromBatchIndexed`
- `VAEDecode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `UpscaleModelLoader`
- `CLIPTextEncode`
- `SaveImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `0.10000000000000002`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `202789835509806`
- `steps` = `6`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`ImageFromBatch`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`Prompts Everywhere`、`ImageConcanateOfUtils`、`ImageUpscaleWithModel`、`Image Tiled`、`GetNode`、`SetNode`、`Anything Everywhere3`、`VAEDecode`、`Seed Everywhere`、`Note`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`ImageScaleBy`

**缺卡**（3）：`Image Tiled`、`Prompts Everywhere`、`Seed Everywhere`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识
- 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
