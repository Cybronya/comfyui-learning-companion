---
key: 图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json
name: qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json
hash: fdea878126371540
coverage: 0.794118
learned_at: 2026-10-07 02:23:11
nodes: [VAELoader, CLIPLoader, TextGenerateLTX2Prompt, TextEncodeQwenImage21, KSampler, easy setNode, VAEDecode, ShowText|pysssss, EmptyLatentImage, ComfySwitchNode, CLIPLoader, CLIPLoader, SetNode, SetNode, GetNode, ResolutionSelector, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, UNETLoader, PreviewImage, Image Comparer (rgthree), QwenImage21Cache, Anything Everywhere3, LoraLoaderModelOnly, CR Prompt Text, SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage]
patterns: [text_to_image]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResolutionSelector`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（54/68）

**有卡**：`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoadImage`

**缺卡**（4）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy setNode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
