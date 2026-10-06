---
key: 图片生成/文生图/精品大合集Qwen image 2.1好用的都在这里啦-截止到260929_2104209467754770434.json
name: 精品大合集Qwen image 2.1好用的都在这里啦-截止到260929_2104209467754770434
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/精品大合集Qwen image 2.1好用的都在这里啦-截止到260929_2104209467754770434.json
hash: 8ecb3fe42b1b24a5
coverage: 0.698113
learned_at: 2026-10-06 23:00:26
nodes: [easy showAnything, EmptyLatentImage, ComfySwitchNode, 孤海注释, SaveImage, CLIPLoader, TextEncodeQwenImage21, KSampler, VAEDecode, easy cleanGpuUsed, easy showAnything, ComfySwitchNode, EmptyLatentImage, PrimitiveBoolean, ResolutionSelector, 孤海注释, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAELoader, easy showAnything, KSampler, easy cleanGpuUsed, VAEDecode, CLIPLoader, VAEDecode, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, QwenPERewriteT8, LoadImage, LoadImage, TextEncodeQwenImage21, KSampler, 忽略多组孤海, 忽略多组孤海, easy cleanGpuUsed, ConditioningZeroOut, VAEEncode, VAEDecode, easy imageBatchToImageList, easy imageListToImageBatch, ResolutionSelector, 孤海注释, 孤海注释, 孤海注释, TTP_Image_Assy, VAELoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, KSampler, TTP_Tile_image_size, SimpleMath+, TTP_Image_Tile_Batch, SimpleMath+, LoraLoaderModelOnly, CLIPLoader, ReferenceLatent, UNETLoader, CLIPTextEncode, CR Prompt Text, ResolutionSelector, UNETLoader, UNETLoader, LoadImage, VAELoader, CLIPTextEncode, ConditioningZeroOut, ImageConcanate, SetNode, GetNode, GetNode, Image Comparer (rgthree), SetNode, GetNode, GetNode, PreviewImage, UNETLoader, CLIPLoader, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, ImageScaleToTotalPixels, GetImageSize, Flux2Scheduler, EmptyFlux2LatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAEDecode, SetNode, 孤海注释, 孤海注释, LoadImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, LoadImage, CR Prompt Text, CR Prompt Text, PrimitiveStringMultiline, PrimitiveBoolean, ResolutionSelector, UNETLoader, VAELoader, CLIPLoader, VAEDecode, TextGenerateLTX2Prompt, LoadImage, LoadImage, LoadImage, BatchImagesNode, QwenPERewriteT8, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, QwenImage21SageAttentionT8, QwenPERewriteT8, LoadImage, CR Text, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, KSampler]
patterns: [text_to_image, image_to_image]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1075617768064495, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/精品大合集Qwen image 2.1好用的都在这里啦-截止到260929_2104209467754770434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/精品大合集Qwen image 2.1好用的都在这里啦-截止到260929_2104209467754770434.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（159 个）：
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `孤海注释`
- `SaveImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `ResolutionSelector`
- `孤海注释`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `easy showAnything`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ResolutionSelector`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `TTP_Image_Assy`
- `VAELoader`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `TTP_Tile_image_size`
- `SimpleMath+`
- `TTP_Image_Tile_Batch`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ImageConcanate`
- `SetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `QwenPERewriteT8`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `QwenImage21SageAttentionT8`
- `QwenPERewriteT8`
- `LoadImage`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1075617768064495`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（111/159）

**有卡**：`EmptyLatentImage`、`SaveImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`PrimitiveBoolean`、`ResolutionSelector`、`LoadImage`、`QwenImage21Cache`、`VAELoader`、`QwenPERewriteT8`、`ConditioningZeroOut`、`VAEEncode`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`LoraLoaderModelOnly`、`ReferenceLatent`、`UNETLoader`、`CLIPTextEncode`、`ImageConcanate`、`CFGGuider`、`ImageScaleToTotalPixels`、`GetImageSize`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`QwenImage21SageAttentionT8`

**缺卡**（17）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
