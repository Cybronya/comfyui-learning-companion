---
key: 视频生成/图生视频/WAN2.2人物替换角色替换动作迁移 图生视频人物类特效一站式_2092550993358704641.json
name: WAN2.2人物替换角色替换动作迁移 图生视频人物类特效一站式_2092550993358704641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2人物替换角色替换动作迁移 图生视频人物类特效一站式_2092550993358704641.json
hash: e68063af6da43571
coverage: 0.938462
learned_at: 2026-10-16 22:59:22
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, LoadImage, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoContextOptions, ImageBlend, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, VHS_LoadVideo, easy int, SeCVideoSegmentation, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, SeCModelLoader, OnnxDetectionModelLoader, DrawMaskOnImage, PoseAndFaceDetection, WanVideoVAELoader, CLIPVisionLoader, VHS_VideoCombine, ClothesSegment, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2人物替换角色替换动作迁移 图生视频人物类特效一站式_2092550993358704641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/WAN2.2人物替换角色替换动作迁移 图生视频人物类特效一站式_2092550993358704641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoContextOptions`
- `ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `easy int`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `ClothesSegment`
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

覆盖率 **94%**（61/65）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`LoadImage`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoContextOptions`、`ImageBlend`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`VHS_LoadVideo`、`easy int`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ClothesSegment`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
