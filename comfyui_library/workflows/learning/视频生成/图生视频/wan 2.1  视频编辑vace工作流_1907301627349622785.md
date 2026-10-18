---
key: 视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json
name: wan 2.1  视频编辑vace工作流_1907301627349622785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json
hash: 443518680e318f78
coverage: 0.944444
learned_at: 2026-10-15 22:29:27
nodes: [VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_LoadVideo, PreviewImage, WanVideoDecode, LoadImage, ImageResizeKJ, AIO_Preprocessor, ImageResizeKJ, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, VHS_LoadVideo, WanVideoExperimentalArgs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1907301627349622785.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（18 个）：
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `PreviewImage`
- `WanVideoDecode`
- `LoadImage`
- `ImageResizeKJ`
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoDecode`、`LoadImage`、`ImageResizeKJ`、`AIO_Preprocessor`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageResizeKJ
