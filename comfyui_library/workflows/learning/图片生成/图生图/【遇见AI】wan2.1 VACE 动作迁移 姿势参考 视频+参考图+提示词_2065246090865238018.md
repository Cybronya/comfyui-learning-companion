---
key: 图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json
name: 【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json
hash: eb61a029c40cc558
coverage: 0.888889
learned_at: 2026-10-23 11:52:24
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoBlockSwap, MarkdownNote, LoadImage, LoadImage, WanVideoTeaCache, VHS_VideoInfo, PreviewImage, AIO_Preprocessor, Note, ImageResizeKJv2, WanVideoVACEEncode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 动作迁移 姿势参考 视频+参考图+提示词_2065246090865238018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoTeaCache`
- `VHS_VideoInfo`
- `PreviewImage`
- `AIO_Preprocessor`
- `Note`
- `ImageResizeKJv2`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoTeaCache`、`VHS_VideoInfo`、`AIO_Preprocessor`、`ImageResizeKJv2`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
