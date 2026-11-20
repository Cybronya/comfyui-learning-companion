---
key: 平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json
name: Wan 2.1 SCAIL 视频人物替换_2062884370725302274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json
hash: 26f926aeb7a4446a
coverage: 0.878049
learned_at: 2026-11-14 01:03:50
nodes: [CreateVideo, SaveVideo, MarkdownNote, GetVideoComponents, WanVideoContextOptions, WanVideoAddSCAILReferenceEmbeds, WanVideoAddSCAILPoseEmbeds, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, Note, LoadNLFModel, PoseDetectionVitPoseToDWPose, NLFPredict, PoseDetectionVitPoseToDWPose, SimpleMath+, SimpleMath+, RenderNLFPoses, WanVideoSchedulerv2, WanVideoSamplerExtraArgs, WanVideoDecode, WanVideoClipVisionEncode, MarkdownNote, WanVideoSamplerv2, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, ImageResizeKJv2, WanVideoModelLoader, WanVideoEmptyEmbeds, ImageResizeKJv2, MarkdownNote, WanVideoSetLoRAs, WanVideoTextEncode, CreateVideo, ImageFromBatch, MarkdownNote, LoadImage, LoadVideo, SaveVideo]
patterns: []
missing: []
---

# 平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan 2.1 SCAIL 视频人物替换_2062884370725302274.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `GetVideoComponents`
- `WanVideoContextOptions`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `Note`
- `LoadNLFModel`
- `PoseDetectionVitPoseToDWPose`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `SimpleMath+`
- `SimpleMath+`
- `RenderNLFPoses`
- `WanVideoSchedulerv2`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `MarkdownNote`
- `WanVideoSamplerv2` ★核心
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoEmptyEmbeds`
- `ImageResizeKJv2`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `CreateVideo`
- `ImageFromBatch`
- `MarkdownNote`
- `LoadImage`
- `LoadVideo`
- `SaveVideo`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`CreateVideo`、`SaveVideo`、`GetVideoComponents`、`WanVideoContextOptions`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadNLFModel`、`PoseDetectionVitPoseToDWPose`、`NLFPredict`、`SimpleMath+`、`RenderNLFPoses`、`WanVideoSchedulerv2`、`WanVideoSamplerExtraArgs`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoSamplerv2`、`LoadWanVideoT5TextEncoder`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoEmptyEmbeds`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`ImageFromBatch`、`LoadImage`、`LoadVideo`

**用到的条目**：LoadImage、WanVideoSamplerExtraArgs、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
