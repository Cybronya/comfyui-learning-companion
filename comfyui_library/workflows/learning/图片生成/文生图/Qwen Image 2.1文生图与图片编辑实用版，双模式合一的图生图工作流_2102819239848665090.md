---
key: 图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json
name: Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json
hash: 230042b9d6b90a9c
coverage: 0.845528
learned_at: 2026-10-10 20:58:53
nodes: [VAELoader, KSampler, CLIPLoader, VAELoader, KSampler, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, CLIPLoader, EmptyLatentImage, VAEDecode, VAEDecode, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, AddLabel, SaveImage, Seed (rgthree), ModelSamplingAuraFlow, UNETLoader, TextEncodeQwenImage21, AddLabel, BatchImagesNode, CLIPTextEncode, ImagesConcanateToGrid, AddLabel, ResolutionSelector, SaveImage, SaveImage, UNETLoader, CLIPLoader, easy promptList, TextGenerateLTX2Prompt, AILab_QwenVL, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, PrimitiveStringMultiline, SaveImage, LoadImage, PreviewAny, CLIPLoader, UNETLoader, KSampler, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, GetImageSize, EmptyLatentImage, VAEDecode, SaveImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, CLIPLoader, SaveImage, PrimitiveStringMultiline, easy anythingIndexSwitch, PreviewAny, ComfySwitchNode, PreviewAny, LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, TextEncodeQwenImage21, GetImageSize, EmptyLatentImage, QwenImage21Cache, KSampler, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, PrimitiveStringMultiline, BatchImagesNode, ResolutionSelector, LoadImage, LoadImage, PreviewAny, ComfySwitchNode, TextGenerateLTX2Prompt, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy anythingIndexSwitch, Seed (rgthree), easy promptList]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图与图片编辑实用版，双模式合一的图生图工作流_2102819239848665090.json`

## 结构

**节点**（123 个）：
- `VAELoader`
- `KSampler`
- `CLIPLoader`
- `VAELoader`
- `KSampler`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `KSampler`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `AddLabel`
- `SaveImage`
- `Seed (rgthree)`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `TextEncodeQwenImage21`
- `AddLabel`
- `BatchImagesNode`
- `CLIPTextEncode`
- `ImagesConcanateToGrid`
- `AddLabel`
- `ResolutionSelector`
- `SaveImage`
- `SaveImage`
- `UNETLoader`
- `CLIPLoader`
- `easy promptList`
- `TextGenerateLTX2Prompt`
- `AILab_QwenVL`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `PrimitiveStringMultiline`
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `CLIPLoader`
- `UNETLoader`
- `KSampler`
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `VAELoader`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `GetImageSize`
- `EmptyLatentImage`
- `VAEDecode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `CLIPLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `easy anythingIndexSwitch`
- `PreviewAny`
- `ComfySwitchNode`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `GetImageSize`
- `EmptyLatentImage`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
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
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **85%**（104/123）

**有卡**：`VAELoader`、`KSampler`、`CLIPLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`AddLabel`、`SaveImage`、`Seed (rgthree)`、`ModelSamplingAuraFlow`、`TextEncodeQwenImage21`、`BatchImagesNode`、`ImagesConcanateToGrid`、`ResolutionSelector`、`easy promptList`、`TextGenerateLTX2Prompt`、`AILab_QwenVL`、`PrimitiveStringMultiline`、`LoadImage`、`PreviewAny`、`QwenImage21Cache`、`GetImageSize`、`Image Comparer (rgthree)`、`easy anythingIndexSwitch`、`ComfySwitchNode`、`孤海注释`

**缺卡**（3）：`easy anythingIndexSwitch`、`Seed (rgthree)`、`easy promptList`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
