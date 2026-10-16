---
key: 视频生成/文生视频/万相Wan2.1-VACE-14B视频扩展_1923941763244093441.json
name: 万相Wan2.1-VACE-14B视频扩展_1923941763244093441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1923941763244093441.json
hash: a41a39aebf38ef99
coverage: 1
learned_at: 2026-10-15 22:43:24
nodes: [ImagePadKJ, WanVideoVACEModelSelect, WanVideoBlockSwap, GetImageSize+, ImageResizeKJ, WanVideoTorchCompileSettings, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoTeaCache, VHS_VideoCombine, VHS_LoadVideo, WanVideoDecode, WanVideoVACEEncode, WanVideoTextEncode, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/万相Wan2.1-VACE-14B视频扩展_1923941763244093441.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1923941763244093441.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `ImagePadKJ`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `GetImageSize+`
- `ImageResizeKJ`
- `WanVideoTorchCompileSettings`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`ImagePadKJ`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`GetImageSize+`、`ImageResizeKJ`、`WanVideoTorchCompileSettings`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoDecode`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageResizeKJ、GetImageSize+
