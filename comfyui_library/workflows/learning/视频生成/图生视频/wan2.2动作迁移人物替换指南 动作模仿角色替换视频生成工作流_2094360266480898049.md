---
key: 视频生成/图生视频/wan2.2动作迁移人物替换指南 动作模仿角色替换视频生成工作流_2094360266480898049.json
name: wan2.2动作迁移人物替换指南 动作模仿角色替换视频生成工作流_2094360266480898049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移人物替换指南 动作模仿角色替换视频生成工作流_2094360266480898049.json
hash: 9d1229162e9d70c2
coverage: 0.938462
learned_at: 2026-10-16 23:42:39
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, PoseAndFaceDetection, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageBlend, ImageConcatMulti, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, WanVideoTextEncodeCached, VHS_LoadVideo, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2动作迁移人物替换指南 动作模仿角色替换视频生成工作流_2094360266480898049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移人物替换指南 动作模仿角色替换视频生成工作流_2094360266480898049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **94%**（61/65）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageBlend`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
