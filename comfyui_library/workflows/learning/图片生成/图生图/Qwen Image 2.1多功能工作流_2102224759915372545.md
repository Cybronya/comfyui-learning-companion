---
key: 图片生成/图生图/Qwen Image 2.1多功能工作流_2102224759915372545.json
name: Qwen Image 2.1多功能工作流_2102224759915372545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多功能工作流_2102224759915372545.json
hash: 9dc69b221872ce65
coverage: 0.691358
learned_at: 2026-10-10 20:48:06
nodes: [EmptyLatentImage, DrawMaskOnImage, easy sam3ImageSegmentation, INPAINT_ExpandMask, INPAINT_ExpandMask, Masks Subtract, easy sam3ImageSegmentation, QwenImage21Cache, TextEncodeQwenImage21, GetNode, PreviewImage, ImageAndMaskPreview, ResolutionSelector, ComfySwitchNode, VAEDecode, KSampler, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyLatentImage, KSampler, VAEDecode, ShowText|pysssss, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, BatchImagesNode, ComfySwitchNode, ResolutionSelector, KSampler, VAEDecode, VAEDecode, ShowText|pysssss, EmptyLatentImage, SetNode, SetNode, DF_Integer, ImageResize+, SimpleMath+, GetImageSize, TTP_Image_Tile_Batch, ImpactMinMax, DF_Integer, TextEncodeQwenImage21, ResolutionSelector, SaveImage, KSampler, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, CR Prompt Text, SaveImage, UNETLoader, CLIPLoader, CLIPLoader, CLIPLoader, TextEncodeQwenImage21, TextGenerateLTX2Prompt, GetNode, VAELoader, Anything Everywhere3, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, LoadImage, LoadImage, easy sam3ModelLoader, LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, TTP_Image_Assy, SaveImage, CR Prompt Text, CR Prompt Text, Fast Groups Bypasser (rgthree), LoadImage, CR Prompt Text, ResizeLongestToNode]
patterns: []
missing: [Masks Subtract, SimpleMath+, easy sam3ImageSegmentation, easy sam3ImageSegmentation, easy sam3ModelLoader, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, ImageResize+]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 359234245958728, "steps": 25, "width": 1024}
discoveries: [次要节点 `Masks Subtract` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy sam3ImageSegmentation` 知识库中没有该节点类型的任何知识, 次要节点 `easy sam3ImageSegmentation` 知识库中没有该节点类型的任何知识, 次要节点 `easy sam3ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1多功能工作流_2102224759915372545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多功能工作流_2102224759915372545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `EmptyLatentImage` ★核心
- `DrawMaskOnImage`
- `easy sam3ImageSegmentation`
- `INPAINT_ExpandMask`
- `INPAINT_ExpandMask`
- `Masks Subtract`
- `easy sam3ImageSegmentation`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `GetNode`
- `PreviewImage`
- `ImageAndMaskPreview`
- `ResolutionSelector`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `BatchImagesNode`
- `ComfySwitchNode`
- `ResolutionSelector`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `SetNode`
- `SetNode`
- `DF_Integer`
- `ImageResize+`
- `SimpleMath+`
- `GetImageSize`
- `TTP_Image_Tile_Batch`
- `ImpactMinMax`
- `DF_Integer`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `VAELoader`
- `Anything Everywhere3`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `LoadImage`
- `easy sam3ModelLoader`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `TTP_Image_Assy`
- `SaveImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `ResizeLongestToNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `359234245958728`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（56/81）

**有卡**：`EmptyLatentImage`、`DrawMaskOnImage`、`INPAINT_ExpandMask`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageAndMaskPreview`、`ResolutionSelector`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`BatchImagesNode`、`DF_Integer`、`GetImageSize`、`TTP_Image_Tile_Batch`、`ImpactMinMax`、`UNETLoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`TTP_Image_Assy`、`ResizeLongestToNode`

**缺卡**（10）：`Masks Subtract`、`SimpleMath+`、`easy sam3ImageSegmentation`、`easy sam3ImageSegmentation`、`easy sam3ModelLoader`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Masks Subtract` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sam3ImageSegmentation` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sam3ImageSegmentation` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sam3ModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
