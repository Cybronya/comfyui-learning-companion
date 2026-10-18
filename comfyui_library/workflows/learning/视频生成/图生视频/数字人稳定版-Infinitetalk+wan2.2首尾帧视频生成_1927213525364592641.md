---
key: 视频生成/图生视频/数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json
name: 数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json
hash: bcb6c02fed0714f1
coverage: 0.90625
learned_at: 2026-10-15 22:29:54
nodes: [PathchSageAttentionKJ, VAELoader, AudioEncoderLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), CLIPLoader, easy seed, ModelPatchLoader, INTConstant, INTConstant, LayerUtility: ImageScaleRestore V2, CLIPTextEncode, ImageResizeKJv2, LoadImage, LoadAudio, LoadAudio, easy cleanGpuUsed, easy cleanGpuUsed, IndexTTS2Run, Float, JjkText, PreviewAudio, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, JjkText, VHS_VideoCombine, LoadImage, RHHiddenNodes, UNETLoader, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人稳定版-Infinitetalk+wan2.2首尾帧视频生成_1927213525364592641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1927213525364592641.json`

## 结构

**生成流程**：Model → Condition → Process → Other

**节点**（32 个）：
- `PathchSageAttentionKJ`
- `VAELoader`
- `AudioEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `easy seed`
- `ModelPatchLoader`
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleRestore V2`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `IndexTTS2Run`
- `Float`
- `JjkText`
- `PreviewAudio`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `JjkText`
- `VHS_VideoCombine`
- `LoadImage`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **91%**（29/32）

**有卡**：`PathchSageAttentionKJ`、`VAELoader`、`AudioEncoderLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`easy seed`、`ModelPatchLoader`、`INTConstant`、`LayerUtility: ImageScaleRestore V2`、`CLIPTextEncode`、`ImageResizeKJv2`、`LoadImage`、`LoadAudio`、`easy cleanGpuUsed`、`IndexTTS2Run`、`Float`、`PreviewAudio`、`ModelSamplingSD3`、`VHS_VideoCombine`、`RHHiddenNodes`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、easy seed、AudioEncoderLoader
