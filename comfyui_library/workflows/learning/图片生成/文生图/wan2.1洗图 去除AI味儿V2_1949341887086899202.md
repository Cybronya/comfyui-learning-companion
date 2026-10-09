---
key: 图片生成/文生图/wan2.1洗图 去除AI味儿V2_1949341887086899202.json
name: wan2.1洗图 去除AI味儿V2_1949341887086899202.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1洗图 去除AI味儿V2_1949341887086899202.json
hash: 411e7f05f5252be9
coverage: 0.586207
learned_at: 2026-10-07 22:58:06
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, VAELoader, SaveImage, MarkdownNote, CLIPLoader, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, VAEEncode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: SaveImagePlusV2, Reroute, PreviewImage, PDImageResizeV2, UNETLoader, LoadImage, RH_LLMAPI_NODE, LoraLoader, LoraLoader, VAEDecode, ttN concat, RH_Captioner, easy showAnything, LoraLoader, KSampler]
patterns: [image_to_image, lora]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ttN concat, LayerUtility: SaveImagePlusV2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "beta", "seed": 1234567896, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: SaveImagePlusV2` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1洗图 去除AI味儿V2_1949341887086899202.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1949341887086899202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAELoader`
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VAEEncode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: SaveImagePlusV2`
- `Reroute`
- `PreviewImage`
- `PDImageResizeV2`
- `UNETLoader` ★核心
- `LoadImage`
- `RH_LLMAPI_NODE`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `ttN concat`
- `RH_Captioner`
- `easy showAnything`
- `LoraLoader` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `1234567896`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **59%**（17/29）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAELoader`、`SaveImage`、`CLIPLoader`、`VAEEncode`、`PDImageResizeV2`、`UNETLoader`、`LoadImage`、`RH_LLMAPI_NODE`、`LoraLoader`、`VAEDecode`、`RH_Captioner`、`KSampler`

**缺卡**（4）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ttN concat`、`LayerUtility: SaveImagePlusV2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: SaveImagePlusV2` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
