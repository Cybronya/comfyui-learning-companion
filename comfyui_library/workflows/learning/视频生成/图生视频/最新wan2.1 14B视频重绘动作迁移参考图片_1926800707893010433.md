---
key: 视频生成/图生视频/最新wan2.1 14B视频重绘动作迁移参考图片_1926800707893010433.json
name: 最新wan2.1 14B视频重绘动作迁移参考图片_1926800707893010433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新wan2.1 14B视频重绘动作迁移参考图片_1926800707893010433.json
hash: 0c9446a31a830a91
coverage: 1
learned_at: 2026-10-15 22:29:53
nodes: [WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoTeaCache, LoadWanVideoT5TextEncoder, WanVideoVAELoader, AIO_Preprocessor, WanVideoTextEncode, WanVideoVACEEncode, WanVideoBlockSwap, WanVideoVACEModelSelect, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoModelLoader, VHS_VideoCombine, ImageResizeKJ, TextInput_, VHS_LoadVideo, LoadImage, ImageResizeKJ]
patterns: []
missing: []
---

# 视频生成/图生视频/最新wan2.1 14B视频重绘动作迁移参考图片_1926800707893010433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1926800707893010433.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `AIO_Preprocessor`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `TextInput_`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJ`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`AIO_Preprocessor`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`ImageResizeKJ`、`TextInput_`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageResizeKJ
