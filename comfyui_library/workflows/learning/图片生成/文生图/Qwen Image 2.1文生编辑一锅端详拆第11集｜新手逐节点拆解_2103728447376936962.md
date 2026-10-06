---
key: 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json
name: Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json
hash: fc1c1742fb7229c4
coverage: 0.617647
learned_at: 2026-10-07 02:21:58
nodes: [Seed (rgthree), ShowText|pysssss, UNETLoader, LoraLoaderModelOnly, ResolutionSelector, EmptyLatentImage, SaveImage, VAEDecode, easy setNode, RHLLMChatNode, TextEncodeQwenImage21, easy getNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, Seed (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ShowText|pysssss, SaveImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ResizeLongestToNode, Fast Groups Bypasser (rgthree), LoadImage, RHLLMChatNode, ResolutionSelector, EmptyLatentImage, Fast Groups Bypasser (rgthree), easy getNode, easy getNode, SaveImage, Fast Bypasser (rgthree), Any Switch (rgthree), CLIPLoader, VAELoader, KSampler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, VAEDecode, TextEncodeQwenImage21, VAEDecode, TextEncodeQwenImage21, LayerUtility: ImageReelComposit, QwenImage21Cache, Anything Everywhere3, Fast Groups Bypasser (rgthree), PreviewImage, LayerUtility: ImageReel, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), EmptyLatentImage, ComfySwitchNode, Seed (rgthree), ComfySwitchNode, PreviewImage, easy setNode, PreviewImage, Image Comparer (rgthree), PrimitiveBoolean, Image Comparer (rgthree), ResolutionSelector, CR Prompt Text, KSampler, CR Prompt Text, easy setNode, VOSR2ModelLoader, easy float, easy setNode, ImageScaleBy, VOSR2Upscale, SaveImage, Image Comparer (rgthree), PreviewImage, easy getNode, easy getNode, easy getNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Any Switch (rgthree), easy int, SplitImageWithAlpha, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [Fast Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, easy float, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy int, easy setNode, easy setNode, easy setNode, easy setNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, Seed (rgthree), Seed (rgthree), Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端详拆第11集｜新手逐节点拆解_2103728447376936962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy setNode`
- `RHLLMChatNode`
- `TextEncodeQwenImage21`
- `easy getNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `Seed (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `ShowText|pysssss`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ResizeLongestToNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RHLLMChatNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `Fast Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageReelComposit`
- `QwenImage21Cache`
- `Anything Everywhere3`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `PreviewImage`
- `easy setNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PrimitiveBoolean`
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `CR Prompt Text`
- `KSampler` ★核心
- `CR Prompt Text`
- `easy setNode`
- `VOSR2ModelLoader`
- `easy float`
- `easy setNode`
- `ImageScaleBy`
- `VOSR2Upscale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `easy int`
- `SplitImageWithAlpha`
- `CR Prompt Text`
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

覆盖率 **62%**（84/136）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`RHLLMChatNode`、`TextEncodeQwenImage21`、`LoadImage`、`PrimitiveBoolean`、`ResizeLongestToNode`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VOSR2ModelLoader`、`ImageScaleBy`、`VOSR2Upscale`、`SplitImageWithAlpha`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（23）：`Fast Bypasser (rgthree)`、`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`easy float`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy int`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
