---
key: 视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json
name: wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055788920813703169.json
hash: 280f1b2ae3fd3c53
coverage: 0.47561
learned_at: 2026-10-15 22:37:58
nodes: [VHS_VideoInfo, CLIPTextEncode, LoraLoaderModelOnly, CLIPVisionEncode, CreateVideo, SaveVideo, SaveVideo, DrawViTPose, CreateVideo, SaveVideo, PoseAndFaceDetection, Sam2Segmentation, CreateVideo, ImageScale, GetImageSize, OnnxDetectionModelLoader, DownloadAndLoadSAM2Model, BlockifyMask, DrawMaskOnImage, GrowMaskWithBlur, ImageScale, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, PrimitiveInt, WanAnimateToVideo, KSampler, VAEDecode, ImageFromBatch, CreateVideo, TrimVideoLatent, PrimitiveInt, PrimitiveInt, SaveVideo, LoadImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 731424694509425, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055788920813703169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPVisionEncode`
- `CreateVideo`
- `SaveVideo`
- `SaveVideo`
- `DrawViTPose`
- `CreateVideo`
- `SaveVideo`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `CreateVideo`
- `ImageScale`
- `GetImageSize`
- `OnnxDetectionModelLoader`
- `DownloadAndLoadSAM2Model`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GrowMaskWithBlur`
- `ImageScale`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `CreateVideo`
- `TrimVideoLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `731424694509425`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（39/82）

**有卡**：`VHS_VideoInfo`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`CreateVideo`、`SaveVideo`、`DrawViTPose`、`PoseAndFaceDetection`、`Sam2Segmentation`、`ImageScale`、`GetImageSize`、`OnnxDetectionModelLoader`、`DownloadAndLoadSAM2Model`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMaskWithBlur`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`ModelSamplingSD3`、`WanAnimateToVideo`、`KSampler`、`VAEDecode`、`ImageFromBatch`、`TrimVideoLatent`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
