---
key: 图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json
name: z-image+qwen3.8  文生图+洗图双切换_2116426410230378498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json
hash: 9bdf9000812750e4
coverage: 0.854545
learned_at: 2026-11-02 19:11:56
nodes: [Dapao_LlamaChat, easy showAnything, DapaoImageRatioLimitNode, easy positive, easy showAnything, easy positive, easy positive, DapaoImageAspectRatioResizeNode, Dapao_LlamaChat, UNETLoader, EmptyLatentImage, ModelSamplingAuraFlow, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, LoraLoaderModelOnly, easy int, easy int, CheckpointLoaderSimple, Seed (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 忽略多组孤海, 孤海注释, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageResize+, TTP_Image_Assy, ImageScaleBy, GetImageSize+, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageResize+, GetImageSize+, easy cleanGpuUsed, easy int, easy int, easy int, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadDiTModel, Note, DapaoImageCompressionNode, 忽略多组孤海, MarkdownNote, LoadImage, ImpactSwitch, Int, DapaoSafeSaveImage, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 3, "checkpoint": "Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors", "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1024}
---

# 图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `Dapao_LlamaChat`
- `easy showAnything`
- `DapaoImageRatioLimitNode`
- `easy positive`
- `easy showAnything`
- `easy positive`
- `easy positive`
- `DapaoImageAspectRatioResizeNode`
- `Dapao_LlamaChat`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `CheckpointLoaderSimple` ★核心
- `Seed (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `忽略多组孤海`
- `孤海注释`
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
- `DapaoImageCompressionNode`
- `忽略多组孤海`
- `MarkdownNote`
- `LoadImage`
- `ImpactSwitch`
- `Int`
- `DapaoSafeSaveImage`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `4`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `checkpoint` = `Z-Image-Base-8steps-White_Marble-AIO_v2-fp8.safetensors`

## 知识

覆盖率 **85%**（47/55）

**有卡**：`Dapao_LlamaChat`、`DapaoImageRatioLimitNode`、`easy positive`、`DapaoImageAspectRatioResizeNode`、`UNETLoader`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`LoraLoaderModelOnly`、`easy int`、`CheckpointLoaderSimple`、`Seed (rgthree)`、`忽略多组孤海`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageResize+`、`TTP_Image_Assy`、`ImageScaleBy`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageCASharpening+`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`DapaoImageCompressionNode`、`LoadImage`、`Int`、`DapaoSafeSaveImage`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2
