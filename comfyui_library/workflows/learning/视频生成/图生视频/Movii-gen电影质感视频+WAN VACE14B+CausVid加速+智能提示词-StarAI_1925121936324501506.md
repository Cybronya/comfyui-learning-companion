---
key: 视频生成/图生视频/Movii-gen电影质感视频+WAN VACE14B+CausVid加速+智能提示词-StarAI_1925121936324501506.json
name: Movii-gen电影质感视频+WAN VACE14B+CausVid加速+智能提示词-StarAI_1925121936324501506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Movii-gen电影质感视频+WAN VACE14B+CausVid加速+智能提示词-StarAI_1925121936324501506.json
hash: 79f4376773c894a8
coverage: 0.756757
learned_at: 2026-10-15 22:29:51
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, SetNode, LoadWanVideoT5TextEncoder, SimpleMath+, JWInteger, easy showAnything, GetNode, GetNode, GetNode, LoadImage, ColorMatch, WanVideoDecode, Note Plus (mtb), VHS_VideoCombine, WanVideoSampler, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, ImageRepeat, JWInteger, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTextEncode, GetImageSizeAndCount, WanVideoExperimentalArgs, PreviewImage, Int, RHHiddenNodes, CR Text, ImpactSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/Movii-gen电影质感视频+WAN VACE14B+CausVid加速+智能提示词-StarAI_1925121936324501506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1925121936324501506.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `JWInteger`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `ColorMatch`
- `WanVideoDecode`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageRepeat`
- `JWInteger`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `Int`
- `RHHiddenNodes`
- `CR Text`
- `ImpactSwitch`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`JWInteger`、`LoadImage`、`ColorMatch`、`WanVideoDecode`、`Note Plus (mtb)`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageRepeat`、`WanVideoVACEEncode`、`WanVideoVACEStartToEndFrame`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoExperimentalArgs`、`Int`、`RHHiddenNodes`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
