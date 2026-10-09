---
key: 图片生成/文生图/Qwen Image + Wan2.2 真实感 + 高清放大_1953397505272807426.json
name: Qwen Image + Wan2.2 真实感 + 高清放大_1953397505272807426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image + Wan2.2 真实感 + 高清放大_1953397505272807426.json
hash: 6d203aa7a358b05f
coverage: 0.866667
learned_at: 2026-10-07 23:11:58
nodes: [CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoader, KSampler, LoraLoader, UNETLoader, VAEEncode, CLIPLoader, VAELoader, ModelSamplingAuraFlow, CLIPTextEncode, EmptySD3LatentImage, CLIPTextEncode, Reroute, CLIPTextEncode, SaveImage, Image Comparer (rgthree), VAEDecode, CLIPLoader, VAELoader, LoraLoader, UNETLoader, ImageUpscaleWithModel, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcanateOfUtils, ImageFromBatch, ImageFromBatch, ImageFromBatch, Image Tiled, ImageConcanateOfUtils, KSampler, VAEDecode, ImageConcanateOfUtils, ImageFromBatch, ImageFromBatch, PreviewImage, ImageScaleToTotalPixels, Reroute, SaveImage, UpscaleModelLoader, CR Text]
patterns: [lora]
missing: [CR Text, Image Tiled]
parameters: {"cfg": 3.5, "denoise": 1, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 808692421766096, "steps": 20, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image + Wan2.2 真实感 + 高清放大_1953397505272807426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1953397505272807426.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoader` ★核心
- `KSampler` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `ImageUpscaleWithModel`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageFromBatch`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Reroute`
- `SaveImage`
- `UpscaleModelLoader`
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `808692421766096`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CFGZeroStarAndInit`、`LoraLoader`、`KSampler`、`UNETLoader`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`SaveImage`、`VAEDecode`、`ImageUpscaleWithModel`、`ImageFromBatch`、`ImageConcanateOfUtils`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`

**缺卡**（2）：`CR Text`、`Image Tiled`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit、VAEEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识
