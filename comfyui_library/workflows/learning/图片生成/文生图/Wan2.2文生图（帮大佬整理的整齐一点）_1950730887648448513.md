---
key: 图片生成/文生图/Wan2.2文生图（帮大佬整理的整齐一点）_1950730887648448513.json
name: Wan2.2文生图（帮大佬整理的整齐一点）_1950730887648448513
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图（帮大佬整理的整齐一点）_1950730887648448513.json
hash: 9bb77e64fc9c98de
coverage: 0.660714
learned_at: 2026-10-10 20:59:14
nodes: [UNETLoader, CLIPLoader, UNETLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, VAEDecode, easy cleanGpuUsed, SaveAnimatedWEBP, UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingSD3, easy cleanGpuUsed, VAEEncode, ImageScaleToTotalPixels, ImageUpscaleWithModel, UpscaleModelLoader, easy imageBatchToImageList, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageListToImageBatch, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, TTP_Image_Assy, KSampler, SaveImage, CLIPLoader, easy showAnything, TextCombinerTwo, TextCombinerTwo, easy showAnything, easy showAnything, ShowText|pysssss, RH_Translator, easy anythingIndexSwitch, Image Comparer (rgthree), RH_Captioner, CLIPTextEncode, JjkText, EmptyHunyuanLatentVideo, JjkText, KSamplerAdvanced, KSamplerAdvanced, RH_Prompter, LoadImage, Note, JjkText, Note, Note, Note, Note]
patterns: [image_to_image]
missing: [easy anythingIndexSwitch, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList]
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2文生图（帮大佬整理的整齐一点）_1950730887648448513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图（帮大佬整理的整齐一点）_1950730887648448513.json`

## 结构

**节点**（56 个）：
- `UNETLoader`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `VAEDecode`
- `easy cleanGpuUsed`
- `SaveAnimatedWEBP`
- `UNETLoader`
- `VAELoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `VAEEncode`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode`
- `TTP_Image_Assy`
- `KSampler`
- `SaveImage`
- `CLIPLoader`
- `easy showAnything`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `easy showAnything`
- `easy showAnything`
- `ShowText|pysssss`
- `RH_Translator`
- `easy anythingIndexSwitch`
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `CLIPTextEncode`
- `JjkText`
- `EmptyHunyuanLatentVideo`
- `JjkText`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `RH_Prompter`
- `LoadImage`
- `Note`
- `JjkText`
- `Note`
- `Note`
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `20`
- `denoise` = `normal`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`easy cleanGpuUsed`、`SaveAnimatedWEBP`、`LoraLoaderModelOnly`、`VAEEncode`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageListToImageBatch`、`TTP_Image_Assy`、`KSampler`、`SaveImage`、`easy showAnything`、`TextCombinerTwo`

**缺卡**（6）：`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`

## 学习发现

- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
