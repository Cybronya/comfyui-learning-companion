---
key: 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json
name: Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json
hash: 635094ed1293ca0d
coverage: 0.773333
learned_at: 2026-10-10 20:58:54
nodes: [easy setNode, VAEDecode, EmptyLatentImage, Seed (rgthree), KSampler, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, CLIPLoader, CLIPLoader, CLIPLoader, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, CR Prompt Text, LayerUtility: TextJoin, CR Prompt Text, SaveImage, ResolutionSelector, TextEncodeQwenImage21, TextGenerateLTX2Prompt, easy showAnything, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [LayerUtility: TextJoin, easy setNode, CR Prompt Text, CR Prompt Text, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1短剧资产系列场景篇｜环境场景道具批量生成｜分镜更省事_2102620341595103233.json`

## 结构

**节点**（75 个）：
- `easy setNode`
- `VAEDecode`
- `EmptyLatentImage`
- `Seed (rgthree)`
- `KSampler`
- `UNETLoader`
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: TextJoin`
- `CR Prompt Text`
- `SaveImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **77%**（58/75）

**有卡**：`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`Anything Everywhere3`、`SetNode`、`GetNode`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`PreviewImage`、`Image Comparer (rgthree)`、`INTConstant`、`SaveImage`、`CR Prompt Text`、`LayerUtility: TextJoin`、`ResolutionSelector`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`easy showAnything`、`Fast Groups Bypasser (rgthree)`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

**缺卡**（5）：`LayerUtility: TextJoin`、`easy setNode`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
