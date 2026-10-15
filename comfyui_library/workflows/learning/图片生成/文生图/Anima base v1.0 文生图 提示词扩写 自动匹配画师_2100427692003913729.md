---
key: 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json
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

# 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json`

## 结构

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `llama_cpp_parameters`
- `UNETLoader`
- `Note`
- `SaveImage`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `VAEDecode`
- `KSampler`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode`
- `PreviewAny`
- `llama_cpp_model_loader`
- `Note`
- `EmptyLatentImage`
- `Note`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Seed_`
- `KSampler`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Note`
- `LayerUtility: ImageReel`
- `CR Text`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `seed` = `888`
- `steps` = `12`
- `width` = `1536`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`CLIPLoader`、`VAELoader`、`SaveImage`、`llama_cpp_parameters`、`UNETLoader`、`Note`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`llama_cpp_instruct_adv`、`PreviewAny`、`llama_cpp_model_loader`、`EmptyLatentImage`、`LoraLoaderModelOnly`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
