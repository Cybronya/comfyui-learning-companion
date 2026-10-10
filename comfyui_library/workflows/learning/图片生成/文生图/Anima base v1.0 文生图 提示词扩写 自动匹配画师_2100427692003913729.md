---
key: Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json
name: Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json
hash: 02edf25262f0133c
coverage: 0.689655
learned_at: 2026-10-10 21:26:13
nodes: [CLIPLoader, VAELoader, SaveImage, llama_cpp_parameters, UNETLoader, Note, SaveImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEDecode, KSampler, llama_cpp_instruct_adv, CLIPTextEncode, PreviewAny, llama_cpp_model_loader, Note, EmptyLatentImage, Note, LoraLoaderModelOnly, CLIPTextEncode, Seed_, KSampler, LayerUtility: ImageReelComposit, SaveImage, Note, LayerUtility: ImageReel, CR Text, MarkdownNote]
patterns: [text_to_image]
missing: [CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 888, "steps": 12, "width": 1536}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识]
---

# Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `llama_cpp_parameters`
- `UNETLoader` ★核心
- `Note`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `llama_cpp_model_loader`
- `Note`
- `EmptyLatentImage` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed_`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Note`
- `LayerUtility: ImageReel`
- `CR Text`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `888`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`CLIPLoader`、`VAELoader`、`SaveImage`、`llama_cpp_parameters`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`Seed_`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
