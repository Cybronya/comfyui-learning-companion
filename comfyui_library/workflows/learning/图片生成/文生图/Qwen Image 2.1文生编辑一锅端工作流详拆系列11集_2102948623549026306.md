---
key: Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json
name: Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json
hash: 43ed1331532a8307
coverage: 0.368852
learned_at: 2026-10-10 20:58:54
nodes: [Seed (rgthree), ShowText|pysssss, 孤海注释, ResolutionSelector, EmptyLatentImage, SaveImage, VAEDecode, easy setNode, TextEncodeQwenImage21, 孤海注释, easy getNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, Seed (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ShowText|pysssss, SaveImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, ResizeLongestToNode, Fast Groups Bypasser (rgthree), LoadImage, 孤海注释, 孤海注释, 孤海注释, 孤海注释, RHLLMChatNode, ResolutionSelector, EmptyLatentImage, Fast Groups Bypasser (rgthree), 孤海注释, easy getNode, easy getNode, SaveImage, Fast Bypasser (rgthree), Any Switch (rgthree), CLIPLoader, VAELoader, KSampler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, VAEDecode, TextEncodeQwenImage21, VAEDecode, TextEncodeQwenImage21, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, LayerUtility: ImageReelComposit, QwenImage21Cache, Fast Groups Bypasser (rgthree), 孤海注释, PreviewImage, LayerUtility: ImageReel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), EmptyLatentImage, ComfySwitchNode, Seed (rgthree), ComfySwitchNode, PreviewImage, easy setNode, PreviewImage, Image Comparer (rgthree), PrimitiveBoolean, Image Comparer (rgthree), ResolutionSelector, CR Prompt Text, KSampler, easy setNode, VOSR2ModelLoader, easy float, 孤海注释, easy setNode, 孤海注释, ImageScaleBy, VOSR2Upscale, SaveImage, 孤海注释, PreviewImage, 孤海注释, 孤海注释, easy getNode, easy getNode, easy getNode, 孤海注释, 孤海注释, Any Switch (rgthree), easy int, SplitImageWithAlpha, MarkdownNote, RHLLMChatNode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), 孤海注释, LoraLoaderModelOnly, UNETLoader, CR Prompt Text, Anything Everywhere3, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, CR Prompt Text]
patterns: []
missing: [Fast Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, easy float, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy int, easy setNode, easy setNode, easy setNode, easy setNode, CR Prompt Text, CR Prompt Text, CR Prompt Text, Seed (rgthree), Seed (rgthree), Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 601247937991586, "steps": 25, "width": 1024}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `Seed (rgthree)`
- `ShowText|pysssss`
- `孤海注释`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy setNode`
- `TextEncodeQwenImage21`
- `孤海注释`
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
- `孤海注释`
- `孤海注释`
- `ResizeLongestToNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `RHLLMChatNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
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
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LayerUtility: ImageReelComposit`
- `QwenImage21Cache`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `PreviewImage`
- `LayerUtility: ImageReel`
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
- `easy setNode`
- `VOSR2ModelLoader`
- `easy float`
- `孤海注释`
- `easy setNode`
- `孤海注释`
- `ImageScaleBy`
- `VOSR2Upscale`
- `SaveImage`
- `孤海注释`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `孤海注释`
- `孤海注释`
- `Any Switch (rgthree)`
- `easy int`
- `SplitImageWithAlpha`
- `MarkdownNote`
- `RHLLMChatNode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `Anything Everywhere3`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `601247937991586`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **37%**（45/122）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`PrimitiveBoolean`、`ResizeLongestToNode`、`RHLLMChatNode`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`SeedVR2VideoUpscaler`、`VOSR2ModelLoader`、`ImageScaleBy`、`VOSR2Upscale`、`SplitImageWithAlpha`、`LoraLoaderModelOnly`、`UNETLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`

**缺卡**（23）：`Fast Bypasser (rgthree)`、`LayerUtility: ImageReel`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReelComposit`、`easy float`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy int`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`、`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

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
