---
key: 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json
name: Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json
hash: 2275f4e01d92e4de
coverage: 0.830986
learned_at: 2026-10-07 02:17:47
nodes: [CLIPLoader, VAELoader, UNETLoader, EmptyLatentImage, QwenImage21Cache, ComfySwitchNode, Anything Everywhere3, TextEncodeQwenImage21, PreviewAny, KSampler, VAEDecode, Image Comparer (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, TextGenerateLTX2Prompt, BatchImagesNode, CLIPLoader, LoadImage, LoadImage, CLIPLoader, CR Prompt Text, LoadImage, LoadImage, LoadImage, ResolutionSelector, PreviewImage, SaveImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `PreviewAny`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `TextGenerateLTX2Prompt`
- `BatchImagesNode`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
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

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（59/71）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`LoadImage`、`ResolutionSelector`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（3）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
