---
key: 视频生成/图生视频/新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json
name: 新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1932026704078766082.json
hash: 2aee121a879709bd
coverage: 0.745098
learned_at: 2026-10-15 22:30:11
nodes: [WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoSLG, WanVideoExperimentalArgs, GetNode, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, GetNode, WanVideoDecode, WanVideoTextEncode, WanVideoSampler, VHS_VideoCombine, SetNode, SetNode, WanVideoVACEModelSelect, VHS_VideoCombine, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, GetImageSizeAndCount, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoLoraSelect, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], VHS_LoadVideo, Note Plus (mtb), GetImageSizeAndCount, GetNode, ImageResizeKJ, ImageResizeKJ, Note, GetNode, RH_Translator, RHHiddenNodes, LoadImage, Bjornulf_ShowJson, AIO_Preprocessor]
patterns: []
missing: []
---

# 视频生成/图生视频/新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1932026704078766082.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（51 个）：
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `Note Plus (mtb)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Note`
- `GetNode`
- `RH_Translator`
- `RHHiddenNodes`
- `LoadImage`
- `Bjornulf_ShowJson`
- `AIO_Preprocessor`

## 知识

覆盖率 **75%**（38/51）

**有卡**：`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoVACEModelSelect`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`Note Plus (mtb)`、`ImageResizeKJ`、`RH_Translator`、`RHHiddenNodes`、`LoadImage`、`Bjornulf_ShowJson`、`AIO_Preprocessor`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
