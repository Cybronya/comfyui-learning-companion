---
key: Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json
name: Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json
hash: 7bd92ac58e2b947e
coverage: 0.702128
learned_at: 2026-10-10 20:58:53
nodes: [VAEDecode, easy showAnything, SaveImage, JjkText, PreviewImage, VAEDecode, SaveImage, ComfySwitchNode, GetNode, ResolutionSelector, UNETLoader, SetNode, SetNode, CLIPLoader, VAELoader, CLIPLoader, Anything Everywhere3, AIO_Preprocessor, KSampler, LoadImage, BatchImagesNode, QwenImage21Cache, GetNode, PreviewAny, EmptyLatentImage, Image Comparer (rgthree), KSampler, GetNode, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, ShowText|pysssss, LoadImage, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, FastGroupsBypassSwitch, KSampler, TextGenerateLTX2Prompt, ResolutionSelector, CR Text, SaveImage, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, easy showAnything, easy sleep, PreviewImage, CLIPLoader, TextEncodeQwenImage21, TextGenerateLTX2Prompt, PreviewAny, LoadImage, LoadImage, CR Prompt Text, CR Text Concatenate, Qwen3VL_Advanced, DWPreprocessor, DepthAnythingPreprocessor, ImageBlend, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text Concatenate, easy sleep, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `VAEDecode` ★核心
- `easy showAnything`
- `SaveImage`
- `JjkText`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ComfySwitchNode`
- `GetNode`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `LoadImage`
- `BatchImagesNode`
- `QwenImage21Cache`
- `GetNode`
- `PreviewAny`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `FastGroupsBypassSwitch`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `CR Text`
- `SaveImage`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `easy sleep`
- `PreviewImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Qwen3VL_Advanced`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `ImageBlend`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

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

覆盖率 **70%**（66/94）

**有卡**：`VAEDecode`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`AIO_Preprocessor`、`KSampler`、`LoadImage`、`BatchImagesNode`、`QwenImage21Cache`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`FastGroupsBypassSwitch`、`Qwen3VL_Advanced`、`DWPreprocessor`、`DepthAnythingPreprocessor`、`ImageBlend`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（4）：`CR Text`、`CR Text Concatenate`、`easy sleep`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
