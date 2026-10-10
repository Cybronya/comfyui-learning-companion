---
key: 视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json
name: WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json
hash: e85ec1674fb865ea
coverage: 0.83871
learned_at: 2026-10-10 23:05:52
nodes: [ImageScale, ImageUpscaleWithModel, WanVideoSLG, Reroute, WanVideoExperimentalArgs, ShowText|pysssss, ImageResizeKJ, WanVideoDecode, RIFE VFI, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEEncode, CR Combine Prompt, Florence2, LoadFlorence2Model, Reroute, AIO_Preprocessor, LoadWanVideoT5TextEncoder, WanVideoVAELoader, UpscaleModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoBlockSwap, ImageScale, LoadImage, VHS_LoadVideo]
patterns: []
missing: [RIFE VFI, CR Combine Prompt]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **84%**（26/31）

**有卡**：`ImageScale`、`ImageUpscaleWithModel`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageResizeKJ`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`Florence2`、`LoadFlorence2Model`、`AIO_Preprocessor`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`UpscaleModelLoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`

**缺卡**（2）：`RIFE VFI`、`CR Combine Prompt`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageUpscaleWithModel

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
