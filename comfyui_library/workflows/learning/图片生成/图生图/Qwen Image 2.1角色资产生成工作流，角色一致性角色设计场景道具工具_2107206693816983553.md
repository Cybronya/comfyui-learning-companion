---
key: 图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json
name: Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json
hash: b2ceb47b69676ac0
coverage: 0.622807
learned_at: 2026-10-06 21:41:46
nodes: [SaveImageAdvanced, ResolutionSelector, SaveImageAdvanced, LoadImage, LoadImage, SaveImageAdvanced, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy cleanGpuUsed, easy showAnything, TextEncodeQwenImage21, CR Prompt Text, UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, easy cleanGpuUsed, LoadImage, ImageResizeKJv2, CLIPLoader, ResolutionSelector, easy showAnything, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, easy cleanGpuUsed, CLIPLoader, easy showAnything, LoadImage, ImageResizeKJv2, UNETLoader, VAELoader, EmptyLatentImage, KSampler, QwenImage21Cache, VAEDecode, SaveImageAdvanced, PreviewImage, CLIPLoader, easy showAnything, TextEncodeQwenImage21, easy cleanGpuUsed, ImageStitch, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, MuyeTextEditOutput, TextGenerate, CR Prompt Text, MuyeTextEditOutput, PrimitiveStringMultiline, MuyeTextEditOutput, TextGenerate, TextGenerate, CR Prompt Text, MuyeTextEditOutput, TextGenerate, BatchImagesNode, Fast Groups Bypasser (rgthree), ResolutionSelector, CLIPLoader, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [BatchImagesNode, Fast Groups Bypasser (rgthree), ImageStitch, TextGenerate, TextGenerate, TextGenerate, TextGenerate, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, MuyeTextEditOutput, MuyeTextEditOutput, MuyeTextEditOutput, MuyeTextEditOutput, SaveImageAdvanced, SaveImageAdvanced, SaveImageAdvanced, SaveImageAdvanced, TTResolutionSelector, TTResolutionSelector, TTResolutionSelector, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageStitch` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（114 个）：
- `SaveImageAdvanced`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `easy cleanGpuUsed`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPLoader`
- `ResolutionSelector`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `easy showAnything`
- `LoadImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `PreviewImage`
- `CLIPLoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `ImageStitch`
- `TTResolutionSelector`
- `CR Prompt Text`
- `CLIPLoader`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `MuyeTextEditOutput`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `PrimitiveStringMultiline`
- `MuyeTextEditOutput`
- `TextGenerate`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `TextGenerate`
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `CLIPLoader`
- `SaveImage`
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

覆盖率 **62%**（71/114）

**有卡**：`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（30）：`BatchImagesNode`、`Fast Groups Bypasser (rgthree)`、`ImageStitch`、`TextGenerate`、`TextGenerate`、`TextGenerate`、`TextGenerate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ImageResizeKJv2`、`MuyeTextEditOutput`、`MuyeTextEditOutput`、`MuyeTextEditOutput`、`MuyeTextEditOutput`、`SaveImageAdvanced`、`SaveImageAdvanced`、`SaveImageAdvanced`、`SaveImageAdvanced`、`TTResolutionSelector`、`TTResolutionSelector`、`TTResolutionSelector`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageStitch` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `MuyeTextEditOutput` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `TTResolutionSelector` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
