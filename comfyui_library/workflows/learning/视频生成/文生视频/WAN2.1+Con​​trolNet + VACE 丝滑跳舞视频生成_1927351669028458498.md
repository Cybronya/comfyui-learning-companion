---
key: 视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json
name: WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json
hash: e85ec1674fb865ea
coverage: 0.903226
learned_at: 2026-10-15 22:47:03
nodes: [ImageScale, ImageUpscaleWithModel, WanVideoSLG, Reroute, WanVideoExperimentalArgs, ShowText|pysssss, ImageResizeKJ, WanVideoDecode, RIFE VFI, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEEncode, CR Combine Prompt, Florence2, LoadFlorence2Model, Reroute, AIO_Preprocessor, LoadWanVideoT5TextEncoder, WanVideoVAELoader, UpscaleModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoBlockSwap, ImageScale, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `ImageScale`
- `ImageUpscaleWithModel`
- `WanVideoSLG`
- `Reroute`
- `WanVideoExperimentalArgs`
- `ShowText|pysssss`
- `ImageResizeKJ`
- `WanVideoDecode`
- `RIFE VFI`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `CR Combine Prompt`
- `Florence2`
- `LoadFlorence2Model`
- `Reroute`
- `AIO_Preprocessor`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `UpscaleModelLoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `ImageScale`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`ImageScale`、`ImageUpscaleWithModel`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageResizeKJ`、`WanVideoDecode`、`RIFE VFI`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`CR Combine Prompt`、`Florence2`、`LoadFlorence2Model`、`AIO_Preprocessor`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`UpscaleModelLoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageUpscaleWithModel
