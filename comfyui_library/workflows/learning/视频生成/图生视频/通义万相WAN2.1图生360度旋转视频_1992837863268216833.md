---
key: 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json
name: 通义万相WAN2.1图生360度旋转视频_1992837863268216833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json
hash: d5bd93d0c84d25dc
coverage: 0.947368
learned_at: 2026-10-15 22:33:17
nodes: [WanVideoImageClipEncode, easy imageSize, WanVideoTextEncode, WanVideoTeaCache, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoDecode, UpscaleModelLoader, TextInput_, WanVideoLoraSelect, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoClipTextEncoder, Note, VHS_VideoCombine, LoadImage, ImageUpscaleWithModel]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1992837863268216833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992837863268216833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoImageClipEncode`
- `easy imageSize`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `UpscaleModelLoader`
- `TextInput_`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageUpscaleWithModel`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoImageClipEncode`、`easy imageSize`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`UpscaleModelLoader`、`TextInput_`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`LoadImage`、`ImageUpscaleWithModel`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
