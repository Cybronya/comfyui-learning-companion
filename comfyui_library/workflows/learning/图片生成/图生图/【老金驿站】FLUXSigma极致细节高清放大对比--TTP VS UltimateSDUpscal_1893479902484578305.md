---
key: 图片生成/图生图/【老金驿站】FLUXSigma极致细节高清放大对比--TTP VS UltimateSDUpscal_1893479902484578305.json
name: 【老金驿站】FLUXSigma极致细节高清放大对比--TTP VS UltimateSDUpscal_1893479902484578305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【老金驿站】FLUXSigma极致细节高清放大对比--TTP VS UltimateSDUpscal_1893479902484578305.json
hash: 0a1bbc484eebf484
coverage: 0.766667
learned_at: 2026-10-23 11:51:22
nodes: [EmptySD3LatentImage, Seed (rgthree), BasicScheduler, Reroute, CLIPTextEncode, SaveImage, easy imageColorMatch, CLIPTextEncode, UpscaleModelLoader, MultiplySigmas, ImageUpscaleWithModel, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy imageBatchToImageList, BasicGuider, ShowText|pysssss, Florence2Run, SamplerCustomAdvanced, FluxGuidance, TTP_Tile_image_size, TTP_Image_Assy, GetImageSize+, easy int, easy int, Power Lora Loader (rgthree), Reroute, Reroute, UpscaleModelLoader, Reroute, ImageScaleToTotalPixels, PreviewImage, Reroute, VAELoader, UNETLoader, TripleCLIPLoader, easy imageListToImageBatch, VAEDecodeTiled, KSamplerSelect, DownloadAndLoadFlorence2Model, SaveImage, Image Comparer (rgthree), ImageSmartSharpen+, VAEEncode, RandomNoise, BasicScheduler, CLIPTextEncode, TTP_Image_Tile_Batch, KSamplerSelect, UltimateSDUpscaleCustomSample, ModelSamplingFlux, Image Comparer (rgthree), StringConstantMultiline, Fast Groups Muter (rgthree), Reroute, Reroute, Reroute, Reroute, LoadImage, DetailDaemonSamplerNode]
patterns: []
missing: []
---

# 图片生成/图生图/【老金驿站】FLUXSigma极致细节高清放大对比--TTP VS UltimateSDUpscal_1893479902484578305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【老金驿站】FLUXSigma极致细节高清放大对比--TTP VS UltimateSDUpscal_1893479902484578305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `EmptySD3LatentImage`
- `Seed (rgthree)`
- `BasicScheduler`
- `Reroute`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy imageColorMatch`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `MultiplySigmas`
- `ImageUpscaleWithModel`
- `SimpleMath+`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `BasicGuider`
- `ShowText|pysssss`
- `Florence2Run`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `TTP_Tile_image_size`
- `TTP_Image_Assy`
- `GetImageSize+`
- `easy int`
- `easy int`
- `Power Lora Loader (rgthree)`
- `Reroute`
- `Reroute`
- `UpscaleModelLoader`
- `Reroute`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Reroute`
- `VAELoader`
- `UNETLoader` ★核心
- `TripleCLIPLoader`
- `easy imageListToImageBatch`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `DownloadAndLoadFlorence2Model`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageSmartSharpen+`
- `VAEEncode` ★核心
- `RandomNoise`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `TTP_Image_Tile_Batch`
- `KSamplerSelect` ★核心
- `UltimateSDUpscaleCustomSample`
- `ModelSamplingFlux`
- `Image Comparer (rgthree)`
- `StringConstantMultiline`
- `Fast Groups Muter (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadImage`
- `DetailDaemonSamplerNode` ★核心

## 知识

覆盖率 **77%**（46/60）

**有卡**：`EmptySD3LatentImage`、`Seed (rgthree)`、`BasicScheduler`、`CLIPTextEncode`、`SaveImage`、`easy imageColorMatch`、`UpscaleModelLoader`、`MultiplySigmas`、`ImageUpscaleWithModel`、`SimpleMath+`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`BasicGuider`、`Florence2Run`、`SamplerCustomAdvanced`、`FluxGuidance`、`TTP_Tile_image_size`、`TTP_Image_Assy`、`GetImageSize+`、`easy int`、`Power Lora Loader (rgthree)`、`ImageScaleToTotalPixels`、`VAELoader`、`UNETLoader`、`TripleCLIPLoader`、`easy imageListToImageBatch`、`VAEDecodeTiled`、`KSamplerSelect`、`DownloadAndLoadFlorence2Model`、`ImageSmartSharpen+`、`VAEEncode`、`RandomNoise`、`TTP_Image_Tile_Batch`、`UltimateSDUpscaleCustomSample`、`ModelSamplingFlux`、`StringConstantMultiline`、`LoadImage`、`DetailDaemonSamplerNode`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、DetailDaemonSamplerNode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
