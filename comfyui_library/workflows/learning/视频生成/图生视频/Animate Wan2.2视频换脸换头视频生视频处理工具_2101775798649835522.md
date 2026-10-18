---
key: 视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json
name: Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json
hash: 39774589c83970e3
coverage: 0.634783
learned_at: 2026-10-17 02:14:01
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, GrowMask, DrawMaskOnImage, BlockifyMask, GetNode, SetNode, SetNode, GetNode, easy sam3ModelLoader, WanVideoModelLoader, LayerUtility: PurgeVRAM, easy sam3VideoSegmentation, WanVideoBlockSwap, WanVideoVAELoader, LayerUtility: PurgeVRAM, SetNode, SetNode, VHS_VideoInfo, PixelPerfectResolution, GetNode, Reroute, DWPreprocessor, WanVideoLoraSelectMulti, ImageResizeKJv2, JWInteger, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, SetNode, SimpleMath+, SetNode, SetNode, ImageCropByMaskAndResize, CLIPVisionLoader, GetNode, ImageResizeKJv2, SetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoClipVisionEncode, WanVideoDecode, GetImageSizeAndCount, GetNode, GetNode, SimpleMath+, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, SimpleMath+, SetNode, easy cleanGpuUsed, GetNode, Int, CM_IntToFloat, GetNode, Audio Duration (mtb), ImageFromBatch+, SetNode, SimpleMath+, easy showAnything, GetImageRangeFromBatch, GetNode, GetNode, GetNode, PrimitiveInt, JWInteger, JjkText, JWInteger, VHS_LoadVideo, LoadImage, TextOverlay, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Animate Wan2.2视频换脸换头视频生视频处理工具_2101775798649835522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（115 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GrowMask`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy sam3ModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `easy sam3VideoSegmentation`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `GetNode`
- `Reroute`
- `DWPreprocessor`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `SimpleMath+`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `Int`
- `CM_IntToFloat`
- `GetNode`
- `Audio Duration (mtb)`
- `ImageFromBatch+`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `JWInteger`
- `JjkText`
- `JWInteger`
- `VHS_LoadVideo`
- `LoadImage`
- `TextOverlay`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
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
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（73/115）

**有卡**：`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`easy sam3ModelLoader`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`easy sam3VideoSegmentation`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`VHS_VideoInfo`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`FaceMaskFromPoseKeypoints`、`SimpleMath+`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`easy cleanGpuUsed`、`Int`、`CM_IntToFloat`、`Audio Duration (mtb)`、`ImageFromBatch+`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`LoadImage`、`TextOverlay`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
