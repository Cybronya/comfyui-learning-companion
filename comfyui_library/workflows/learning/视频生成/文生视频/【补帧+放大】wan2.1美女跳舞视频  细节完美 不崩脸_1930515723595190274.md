---
key: 视频生成/文生视频/【补帧+放大】wan2.1美女跳舞视频  细节完美 不崩脸_1930515723595190274.json
name: 【补帧+放大】wan2.1美女跳舞视频  细节完美 不崩脸_1930515723595190274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【补帧+放大】wan2.1美女跳舞视频  细节完美 不崩脸_1930515723595190274.json
hash: 37b64668ae039432
coverage: 0.95
learned_at: 2026-10-15 22:43:25
nodes: [WanVideoBlockSwap, WanVideoTeaCache, WanVideoSLG, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoSampler, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoTextEncode, LoadWanVideoClipTextEncoder, LoadImage, WanVideoLoraSelect, WanVideoDecode, Upscale Model Loader, ImageUpscaleWithModel, FILM VFI, VHS_VideoCombine, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/【补帧+放大】wan2.1美女跳舞视频  细节完美 不崩脸_1930515723595190274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1930515723595190274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `Upscale Model Loader`
- `ImageUpscaleWithModel`
- `FILM VFI`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoDecode`、`Upscale Model Loader`、`ImageUpscaleWithModel`、`FILM VFI`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
