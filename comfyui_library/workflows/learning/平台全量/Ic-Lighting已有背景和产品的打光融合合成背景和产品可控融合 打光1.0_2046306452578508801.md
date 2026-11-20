---
key: 平台全量/Ic-Lighting已有背景和产品的打光融合合成背景和产品可控融合 打光1.0_2046306452578508801.json
name: Ic-Lighting已有背景和产品的打光融合合成背景和产品可控融合 打光1.0_2046306452578508801
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Ic-Lighting已有背景和产品的打光融合合成背景和产品可控融合 打光1.0_2046306452578508801.json
hash: 227ddef2c261c71a
coverage: 0.872727
learned_at: 2026-11-14 00:32:32
nodes: [CLIPTextEncode, CLIPTextEncode, FastCanvasTool, LoadImage, ImageResizeKJv2, SaveImage, VAEDecode, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, FastCanvas, PreviewImage, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEDecode, KSampler, ShowText|pysssss, SaveImage, SaveImage, easy cleanGpuUsed, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), VAEEncode, Int, LoadImage, LoadImage, Florence2Run, RMBG, LoadImage, LoadImage, LoadImage, CheckpointLoaderSimple, ShowText|pysssss, WD14Tagger|pysssss, UNETLoader, DualCLIPLoader, VAELoader, DownloadAndLoadFlorence2Model, LayerUtility: ImageScaleRestore, ImageResizeKJv2, easy hiresFix, ImageResizeKJv2, Int, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), DetailTransfer, VAEEncode, KSampler, IPAdapterAdvanced, CLIPVisionLoader, IPAdapterUnifiedLoader, ICLightConditioning, LoadAndApplyICLightUnet]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5, "checkpoint": "majicMIX realistic 麦橘写实_v7 亚洲男性微调.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 766959674106041, "steps": 40}
---

# 平台全量/Ic-Lighting已有背景和产品的打光融合合成背景和产品可控融合 打光1.0_2046306452578508801.json

> 来源文件 `comfyui_library/workflows/平台全量/Ic-Lighting已有背景和产品的打光融合合成背景和产品可控融合 打光1.0_2046306452578508801.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FastCanvasTool`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `FastCanvas`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `Int`
- `LoadImage`
- `LoadImage`
- `Florence2Run`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ShowText|pysssss`
- `WD14Tagger|pysssss`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `DownloadAndLoadFlorence2Model`
- `LayerUtility: ImageScaleRestore`
- `ImageResizeKJv2`
- `easy hiresFix`
- `ImageResizeKJv2`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `DetailTransfer`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `IPAdapterAdvanced`
- `CLIPVisionLoader`
- `IPAdapterUnifiedLoader`
- `ICLightConditioning`
- `LoadAndApplyICLightUnet`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `766959674106041`
- `steps` = `40`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `majicMIX realistic 麦橘写实_v7 亚洲男性微调.safetensors`

## 知识

覆盖率 **87%**（48/55）

**有卡**：`CLIPTextEncode`、`FastCanvasTool`、`LoadImage`、`ImageResizeKJv2`、`SaveImage`、`VAEDecode`、`easy cleanGpuUsed`、`FastCanvas`、`VAEEncode`、`KSampler`、`Int`、`Florence2Run`、`RMBG`、`CheckpointLoaderSimple`、`WD14Tagger|pysssss`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`DownloadAndLoadFlorence2Model`、`LayerUtility: ImageScaleRestore`、`easy hiresFix`、`DetailTransfer`、`IPAdapterAdvanced`、`CLIPVisionLoader`、`IPAdapterUnifiedLoader`、`ICLightConditioning`、`LoadAndApplyICLightUnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、VAEEncode
