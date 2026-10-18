---
key: 视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json
name: AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json
hash: 7981e41370ddc6e3
coverage: 0.863636
learned_at: 2026-10-17 01:58:53
nodes: [UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, QwenEditOutputExtractor, CropWithPadInfo, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditConfigPreparer, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, WanVideoContextOptions, RepeatImageBatch, WanVideoModelLoader, OnnxDetectionModelLoader, easy cleanGpuUsed, DrawViTPose, Reroute, CLIPVisionLoader, WanVideoVAELoader, MemoryCleaner, WanVideoTextEncodeCached, MemoryCleaner, WanVideoBlockSwap, WanVideoSampler, MemoryCleaner, MemoryCleaner, WanVideoDecode, ImageFromBatch, WanVideoClipVisionEncode, Reroute, PoseAndFaceDetection, Reroute, Reroute, WanVideoSetLoRAs, ImageBatch, ComfyMathExpression, easy mathInt, ComfyMathExpression, BatchCount+, BatchCount+, ImageFromBatch, Reroute, WanVideoLoraSelect, GoohaiUniversalSlider, VAEDecode, CropWithPadInfo, VHS_VideoInfo, PreviewImage, VHS_VideoCombine, easy imageRemBg, QwenEditConfigPreparer, VHS_LoadVideo, Fast Groups Muter (rgthree), Image Comparer (rgthree), LoadImage, LoadImage, PrimitiveStringMultiline, ImageResizeKJv2, GoohaiUniversalSlider, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 66034775370057, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `QwenEditOutputExtractor`
- `CropWithPadInfo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditConfigPreparer`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `RepeatImageBatch`
- `WanVideoModelLoader`
- `OnnxDetectionModelLoader`
- `easy cleanGpuUsed`
- `DrawViTPose`
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `MemoryCleaner`
- `WanVideoTextEncodeCached`
- `MemoryCleaner`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `MemoryCleaner`
- `MemoryCleaner`
- `WanVideoDecode`
- `ImageFromBatch`
- `WanVideoClipVisionEncode`
- `Reroute`
- `PoseAndFaceDetection`
- `Reroute`
- `Reroute`
- `WanVideoSetLoRAs`
- `ImageBatch`
- `ComfyMathExpression`
- `easy mathInt`
- `ComfyMathExpression`
- `BatchCount+`
- `BatchCount+`
- `ImageFromBatch`
- `Reroute`
- `WanVideoLoraSelect`
- `GoohaiUniversalSlider`
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `VHS_VideoInfo`
- `PreviewImage`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `QwenEditConfigPreparer`
- `VHS_LoadVideo`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `GoohaiUniversalSlider`
- `Int`
- `Int`

## 关键参数

- `seed` = `66034775370057`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **86%**（57/66）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`QwenEditOutputExtractor`、`CropWithPadInfo`、`CLIPTextEncode`、`KSampler`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditConfigPreparer`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`RepeatImageBatch`、`WanVideoModelLoader`、`OnnxDetectionModelLoader`、`easy cleanGpuUsed`、`DrawViTPose`、`CLIPVisionLoader`、`WanVideoVAELoader`、`MemoryCleaner`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`WanVideoSetLoRAs`、`ImageBatch`、`ComfyMathExpression`、`easy mathInt`、`BatchCount+`、`WanVideoLoraSelect`、`GoohaiUniversalSlider`、`VAEDecode`、`VHS_VideoInfo`、`VHS_VideoCombine`、`easy imageRemBg`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJv2`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
