---
key: 图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json
name: 大炮v5-CCD-V4.1_2066779112580149250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json
hash: 16032f142c38037b
coverage: 0.736264
learned_at: 2026-10-19 23:23:05
nodes: [easy showAnything, easy showAnything, Note Plus (mtb), easy showAnything, EmptyLatentImage, ModelSamplingAuraFlow, ModelSamplingAuraFlow, ConditioningZeroOut, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageResize+, TTP_Image_Assy, ImageScaleBy, GetImageSize+, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageResize+, GetImageSize+, easy cleanGpuUsed, easy int, easy int, easy int, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadDiTModel, Note, easy positive, Dapao_LlamaChat, 孤海注释, 孤海注释, VAEDecode, CheckpointLoaderSimple, UNETLoader, LoraLoaderModelOnly, DapaoImageAspectRatioResizeNode, Dapao_LlamaChat, ImpactSwitch, LoraLoaderModelOnly, easy positive, LoraLoaderModelOnly, Note, DapaoImageRatioLimitNode, CR Prompt List, Note, Note, Note, Note, Note, Int, Int, Int, Int, Note, 忽略多组孤海, DapaoImageCompressionNode, SaveImage, ImpactSwitch, Note, 忽略多组孤海, Note, Seed (rgthree), Note, Note, easy saveText, Text Concatenate (JPS), ImpactSwitch, easy positive, String Literal, Note, Int, 孤海注释, MarkdownNote, CLIPTextEncode, RepeatLatentBatch, Int, LoadImage, easy positive, Note, LoraLoaderModelOnly, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "checkpoint": "Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors", "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `easy showAnything`
- `easy showAnything`
- `Note Plus (mtb)`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `TTP_Image_Assy`
- `ImageScaleBy`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageResize+`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `easy int`
- `easy int`
- `easy int`
- `ImageCASharpening+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadDiTModel`
- `Note`
- `easy positive`
- `Dapao_LlamaChat`
- `孤海注释`
- `孤海注释`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DapaoImageAspectRatioResizeNode`
- `Dapao_LlamaChat`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `DapaoImageRatioLimitNode`
- `CR Prompt List`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `Int`
- `Int`
- `Int`
- `Note`
- `忽略多组孤海`
- `DapaoImageCompressionNode`
- `SaveImage`
- `ImpactSwitch`
- `Note`
- `忽略多组孤海`
- `Note`
- `Seed (rgthree)`
- `Note`
- `Note`
- `easy saveText`
- `Text Concatenate (JPS)`
- `ImpactSwitch`
- `easy positive`
- `String Literal`
- `Note`
- `Int`
- `孤海注释`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `RepeatLatentBatch`
- `Int`
- `LoadImage`
- `easy positive`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `checkpoint` = `Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors`

## 知识

覆盖率 **74%**（67/91）

**有卡**：`Note Plus (mtb)`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`KSamplerAdvanced`、`easy int`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageResize+`、`TTP_Image_Assy`、`ImageScaleBy`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageCASharpening+`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`easy positive`、`Dapao_LlamaChat`、`VAEDecode`、`CheckpointLoaderSimple`、`UNETLoader`、`LoraLoaderModelOnly`、`DapaoImageAspectRatioResizeNode`、`DapaoImageRatioLimitNode`、`CR Prompt List`、`Int`、`忽略多组孤海`、`DapaoImageCompressionNode`、`SaveImage`、`Seed (rgthree)`、`easy saveText`、`Text Concatenate (JPS)`、`String Literal`、`CLIPTextEncode`、`RepeatLatentBatch`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
