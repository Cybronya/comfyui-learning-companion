---
key: 平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json
name: 二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json
hash: 00b7a66482cd10ca
coverage: 0.616822
learned_at: 2026-11-14 01:34:18
nodes: [GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, SetNode, DrawMaskOnImage, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, GetImageSizeAndCount, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoSampler, SetNode, GetNode, SetNode, ImageFromBatch+, PreviewImage, PreviewImage, Reroute, Reroute, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, Reroute, WanVideoTextEncodeCached, SeCVideoSegmentation, INTConstant, INTConstant, SetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, VHS_VideoCombine, CR Text, JWInteger, PointsEditor, BlockifyMask, GrowMask, WanVideoAnimateEmbeds, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoInfo, PreviewImage, GetNode, GetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json

> 来源文件 `comfyui_library/workflows/平台全量/二创首选Wan2.2 Animate视频生视频 人物精准替换高质量方案_2089318031020355585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `Reroute`
- `MaskToImage`
- `SeCModelLoader`
- `InvertMask`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `CR Text`
- `JWInteger`
- `PointsEditor`
- `BlockifyMask`
- `GrowMask`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

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

覆盖率 **62%**（66/107）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageFromBatch+`、`ImageConcanate`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`INTConstant`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`CR Text`、`JWInteger`、`PointsEditor`、`BlockifyMask`、`GrowMask`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`VHS_LoadVideo`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
