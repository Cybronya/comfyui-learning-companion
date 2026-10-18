---
key: 视频生成/图生视频/Qwen_Image_2.1多功能工作流，文生图图生图抠图一体化处理_2105509584877211650.json
name: Qwen_Image_2.1多功能工作流，文生图图生图抠图一体化处理_2105509584877211650
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1多功能工作流，文生图图生图抠图一体化处理_2105509584877211650.json
hash: f652871052dea405
coverage: 0.836364
learned_at: 2026-10-17 22:18:56
nodes: [EmptyLatentImage, DrawMaskOnImage, easy sam3ImageSegmentation, INPAINT_ExpandMask, INPAINT_ExpandMask, Masks Subtract, easy sam3ImageSegmentation, QwenImage21Cache, TextEncodeQwenImage21, GetNode, PreviewImage, ImageAndMaskPreview, ResolutionSelector, ComfySwitchNode, VAEDecode, KSampler, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyLatentImage, KSampler, VAEDecode, ShowText|pysssss, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, BatchImagesNode, ComfySwitchNode, ResolutionSelector, KSampler, VAEDecode, VAEDecode, ShowText|pysssss, EmptyLatentImage, SetNode, SetNode, DF_Integer, ImageResize+, SimpleMath+, GetImageSize, TTP_Image_Tile_Batch, ImpactMinMax, DF_Integer, TextEncodeQwenImage21, ResolutionSelector, SaveImage, KSampler, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, CR Prompt Text, SaveImage, UNETLoader, CLIPLoader, CLIPLoader, CLIPLoader, TextEncodeQwenImage21, TextGenerateLTX2Prompt, GetNode, VAELoader, Anything Everywhere3, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, LoadImage, LoadImage, easy sam3ModelLoader, LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, TTP_Image_Assy, SaveImage, CR Prompt Text, CR Prompt Text, Fast Groups Bypasser (rgthree), LoadImage, CR Prompt Text, ResizeLongestToNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1多功能工作流，文生图图生图抠图一体化处理_2105509584877211650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1多功能工作流，文生图图生图抠图一体化处理_2105509584877211650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
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
- `LoadImage`
- `PreviewImage`

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

覆盖率 **84%**（92/110）

**有卡**：`EmptyLatentImage`、`DrawMaskOnImage`、`easy sam3ImageSegmentation`、`INPAINT_ExpandMask`、`Masks Subtract`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageAndMaskPreview`、`ResolutionSelector`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`BatchImagesNode`、`DF_Integer`、`ImageResize+`、`SimpleMath+`、`GetImageSize`、`TTP_Image_Tile_Batch`、`ImpactMinMax`、`CR Prompt Text`、`UNETLoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`VAELoader`、`easy sam3ModelLoader`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`TTP_Image_Assy`、`ResizeLongestToNode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
