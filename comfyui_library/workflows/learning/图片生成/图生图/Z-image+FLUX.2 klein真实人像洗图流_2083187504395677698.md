---
key: 图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json
name: Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json
hash: 4cef38ea2a0a56ea
coverage: 0.786885
learned_at: 2026-10-23 11:30:33
nodes: [CLIPLoader, VAELoader, KSamplerSelect, Flux2Scheduler, SeedVR2VideoUpscaler, RandomNoise, CLIPTextEncode, LoraLoaderModelOnly, easy promptConcat, BasicScheduler, VAEEncode, UNETLoader, ConditioningZeroOut, GetNode, SigmasPreview, KSamplerAdvanced, VAEDecode, PreviewImage, Image Comparer (rgthree), Florence2Run, ShowText|pysssss, ShowText|pysssss, easy promptReplace, ShowText|pysssss, UNETLoader, CLIPLoader, VAELoader, VAEEncode, CLIPTextEncode, ReferenceLatent, CFGGuider, ConditioningZeroOut, SamplerCustomAdvanced, VAEDecode, PreviewImage, easy imageColorMatch, Image Comparer (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, DownloadAndLoadFlorence2Model, Fast Groups Bypasser (rgthree), LoadImage, WD14Tagger|pysssss, SetNode, ImageResize+, MarkdownNote, LoadImage, PreviewImage, Image Comparer (rgthree), SaveImage, ImageResize+, TTP_Image_Assy, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, ImageScaleBy, GetImageSize+, ImageResize+, TTP_Tile_image_size]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SeedVR2VideoUpscaler`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy promptConcat`
- `BasicScheduler`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `GetNode`
- `SigmasPreview`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Florence2Run`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `easy promptReplace`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CFGGuider`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `easy imageColorMatch`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `DownloadAndLoadFlorence2Model`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `WD14Tagger|pysssss`
- `SetNode`
- `ImageResize+`
- `MarkdownNote`
- `LoadImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageResize+`
- `TTP_Image_Assy`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageScaleBy`
- `GetImageSize+`
- `ImageResize+`
- `TTP_Tile_image_size`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **79%**（48/61）

**有卡**：`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`Flux2Scheduler`、`SeedVR2VideoUpscaler`、`RandomNoise`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`easy promptConcat`、`BasicScheduler`、`VAEEncode`、`UNETLoader`、`ConditioningZeroOut`、`SigmasPreview`、`KSamplerAdvanced`、`VAEDecode`、`Florence2Run`、`easy promptReplace`、`ReferenceLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`easy imageColorMatch`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`DownloadAndLoadFlorence2Model`、`LoadImage`、`WD14Tagger|pysssss`、`ImageResize+`、`SaveImage`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`GetImageSize+`、`TTP_Tile_image_size`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
