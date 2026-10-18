---
key: 视频生成/图生视频/Wan 2.2动作迁移动作模仿角色替换人物替换处理工具_2101379827570921473.json
name: Wan 2.2动作迁移动作模仿角色替换人物替换处理工具_2101379827570921473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2动作迁移动作模仿角色替换人物替换处理工具_2101379827570921473.json
hash: dd10c4dbbd6537bf
coverage: 0.940299
learned_at: 2026-10-17 02:14:38
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, LayerUtility: ImageMaskScaleAsV2, easy int, ClothesSegment, ImageFromBatch, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, ImageBlend, WanVideoTextEncodeCached, ImageConcatMulti, GetImageSizeAndCount, SeCVideoSegmentation, SeCModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_LoadVideo, Evaluate Integers, DrawViTPose, WanVideoClipVisionEncode, WanVideoContextOptions, BlockifyMask, PoseAndFaceDetection, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan 2.2动作迁移动作模仿角色替换人物替换处理工具_2101379827570921473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan 2.2动作迁移动作模仿角色替换人物替换处理工具_2101379827570921473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ClothesSegment`
- `ImageFromBatch`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VHS_LoadVideo`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `BlockifyMask`
- `PoseAndFaceDetection`
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

覆盖率 **94%**（63/67）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ClothesSegment`、`ImageFromBatch`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoLoraSelectMulti`、`ImageBlend`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`SeCVideoSegmentation`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_LoadVideo`、`Evaluate Integers`、`DrawViTPose`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`BlockifyMask`、`PoseAndFaceDetection`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
