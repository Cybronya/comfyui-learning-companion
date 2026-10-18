---
key: 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json
name: Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json
hash: e657a20b610d725c
coverage: 1
learned_at: 2026-10-15 22:30:14
nodes: [LoadImage, LoadImage, WanVideoBlockSwap, WanVideoVAELoader, GetImageSizeAndCount, ImageResizeKJ, ImageResizeKJ, WanVideoModelLoader, CR Prompt Text, WanVideoTextEncode, LoadWanVideoT5TextEncoder, JWInteger, WanVideoVACEStartToEndFrame, WanVideoExperimentalArgs, WanVideoSLG, WanVideoVACEEncode, WanVideoTeaCache, WanVideoSampler, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933717714491854849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（20 个）：
- `LoadImage`
- `LoadImage`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `CR Prompt Text`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoVACEStartToEndFrame`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`LoadImage`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`ImageResizeKJ`、`WanVideoModelLoader`、`CR Prompt Text`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`WanVideoVACEStartToEndFrame`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、CR Prompt Text
