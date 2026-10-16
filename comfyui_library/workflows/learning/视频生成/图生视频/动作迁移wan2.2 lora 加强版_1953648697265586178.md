---
key: 视频生成/图生视频/动作迁移wan2.2 lora 加强版_1953648697265586178.json
name: 动作迁移wan2.2 lora 加强版_1953648697265586178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953648697265586178.json
hash: 7ae2e0218b4ba7ff
coverage: 0.82
learned_at: 2026-10-15 22:31:05
nodes: [LoadWanVideoT5TextEncoder, easy clearCacheAll, easy clearCacheAll, WanVideoExperimentalArgs, WanVideoSLG, easy clearCacheAll, GetImageSizeAndCount, DWPreprocessor, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, PreviewImage, WanVideoModelLoader, RH_Captioner, SetNode, Bjornulf_ShowJson, WanVideoBlockSwap, WanVideoLoraSelect, GetNode, WanVideoTextEncode, WanVideoTeaCache, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoVACEStartToEndFrame, easy clearCacheAll, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, EmptyImage, VHS_SplitImages, DownloadAndLoadGIMMVFIModel, Display Int (rgthree), Display Int (rgthree), GIMMVFI_interpolate, UpscaleModelLoader, ImageScaleToMegapixels, easy cleanGpuUsed, easy clearCacheAll, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, VHS_VideoCombine, LoadImage, VHS_LoadVideo, PreviewImage, PreviewImage, MaskToImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移wan2.2 lora 加强版_1953648697265586178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953648697265586178.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `LoadWanVideoT5TextEncoder`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `easy clearCacheAll`
- `GetImageSizeAndCount`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoModelLoader`
- `RH_Captioner`
- `SetNode`
- `Bjornulf_ShowJson`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoVACEStartToEndFrame`
- `easy clearCacheAll`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `EmptyImage`
- `VHS_SplitImages`
- `DownloadAndLoadGIMMVFIModel`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `GIMMVFI_interpolate`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`LoadWanVideoT5TextEncoder`、`easy clearCacheAll`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`GetImageSizeAndCount`、`DWPreprocessor`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoModelLoader`、`RH_Captioner`、`Bjornulf_ShowJson`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoVACEStartToEndFrame`、`WanVideoSampler`、`WanVideoDecode`、`EmptyImage`、`VHS_SplitImages`、`DownloadAndLoadGIMMVFIModel`、`Display Int (rgthree)`、`GIMMVFI_interpolate`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`easy cleanGpuUsed`、`LoadImage`、`VHS_LoadVideo`、`MaskToImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
