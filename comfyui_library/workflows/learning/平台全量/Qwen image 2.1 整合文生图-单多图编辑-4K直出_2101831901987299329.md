---
key: 平台全量/Qwen image 2.1 整合文生图-单多图编辑-4K直出_2101831901987299329.json
name: Qwen image 2.1 整合文生图-单多图编辑-4K直出_2101831901987299329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image 2.1 整合文生图-单多图编辑-4K直出_2101831901987299329.json
hash: 061cec8ea4808998
coverage: 0.78481
learned_at: 2026-11-14 00:50:41
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, easy showAnything, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, MuyeTextEditOutput, SaveImage, UNETLoader, UNETLoader, SaveImageAdvanced, SaveImage, UNETLoader, VAELoader, SaveImageAdvanced, UNETLoader, KSampler, CLIPLoader, EmptyLatentImage, ResolutionSelector, Fast Groups Bypasser (rgthree), UNETLoader, UNETLoader, CLIPLoader, VAELoader, easy showAnything, EmptyLatentImage, ResolutionSelector, MuyeTextEditOutput, TextGenerateLTX2Prompt, CLIPLoader, TextEncodeQwenImage21, KSampler, TextEncodeQwenImage21, MuyeTextEditOutput, Fast Groups Bypasser (rgthree), SaveImage, LoadImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), LoadImage, VAEDecode, VAEDecode, VAEDecode, easy showAnything, easy showAnything, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleBy, easy showAnything, easy showAnything, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, GetImageSize+, Note, Note, Note, Image Comparer (rgthree), Image Comparer (rgthree), PreviewImage, TTP_Image_Assy, GetImageSize+, KOOK_ImageCompression, SeedVR2LoadDiTModel, Node Collector (rgthree), ImageScaleBy, SaveImage, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 平台全量/Qwen image 2.1 整合文生图-单多图编辑-4K直出_2101831901987299329.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image 2.1 整合文生图-单多图编辑-4K直出_2101831901987299329.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `MuyeTextEditOutput`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MuyeTextEditOutput`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `MuyeTextEditOutput`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `easy showAnything`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `GetImageSize+`
- `Note`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `TTP_Image_Assy`
- `GetImageSize+`
- `KOOK_ImageCompression`
- `SeedVR2LoadDiTModel`
- `Node Collector (rgthree)`
- `ImageScaleBy`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（62/79）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`MuyeTextEditOutput`、`SaveImage`、`UNETLoader`、`TextGenerateLTX2Prompt`、`VAEDecode`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`GetImageSize+`、`TTP_Image_Assy`、`KOOK_ImageCompression`、`SeedVR2LoadDiTModel`、`Node Collector (rgthree)`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage
