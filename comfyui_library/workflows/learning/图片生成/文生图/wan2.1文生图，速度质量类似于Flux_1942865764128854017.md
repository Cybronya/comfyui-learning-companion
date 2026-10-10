---
key: wan2.1文生图，速度质量类似于Flux_1942865764128854017.json
name: wan2.1文生图，速度质量类似于Flux_1942865764128854017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1文生图，速度质量类似于Flux_1942865764128854017.json
hash: 923d1cf7e4ef1705
coverage: 0.613636
learned_at: 2026-10-10 20:59:26
nodes: [PathchSageAttentionKJ, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, SaveImage, easy clearCacheAll, easy cleanGpuUsed, ModelSamplingSD3, VAEDecode, Label (rgthree), MarkdownNote, Label (rgthree), CLIPTextEncode, Label (rgthree), Note, Label (rgthree), Label (rgthree), FastFilmGrain, WanVideoNAG, VAELoader, UNETLoader, CLIPLoader, LoraLoader, SaveImage, easy clearCacheAll, easy cleanGpuUsed, CLIPTextEncode, Note, Label (rgthree), Label (rgthree), FastFilmGrain, VAEDecode, ModelSamplingSD3, WanVideoNAG, DualCLIPLoader, CLIPTextEncode, UNETLoader, VAELoader, KSampler, EmptyLatentImage, Fast Groups Bypasser (rgthree), DeepTranslatorTextNode, Note, Text Multiline]
patterns: [text_to_image, lora]
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Text Multiline, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1088, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 506939822677643, "steps": 20, "strength_clip": 1, "strength_model": 1, "width": 1920}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# wan2.1文生图，速度质量类似于Flux_1942865764128854017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1文生图，速度质量类似于Flux_1942865764128854017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `SaveImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `FastFilmGrain`
- `WanVideoNAG`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `SaveImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `FastFilmGrain`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanVideoNAG`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `DeepTranslatorTextNode`
- `Note`
- `Text Multiline`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `506939822677643`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `1920`
- `height` = `1088`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（27/44）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSampler`、`SaveImage`、`ModelSamplingSD3`、`VAEDecode`、`FastFilmGrain`、`WanVideoNAG`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoader`、`DualCLIPLoader`、`EmptyLatentImage`、`DeepTranslatorTextNode`

**缺卡**（12）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Text Multiline`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
