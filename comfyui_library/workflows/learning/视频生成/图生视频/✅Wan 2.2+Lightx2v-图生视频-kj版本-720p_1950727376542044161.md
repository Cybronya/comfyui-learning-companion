---
key: 视频生成/图生视频/✅Wan 2.2+Lightx2v-图生视频-kj版本-720p_1950727376542044161.json
name: ✅Wan 2.2+Lightx2v-图生视频-kj版本-720p_1950727376542044161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950727376542044161.json
hash: 8b1d2c6ae95675c3
coverage: 0.578313
learned_at: 2026-10-15 22:30:56
nodes: [SetNode, SetNode, SetNode, JWInteger, SetNode, GetNode, WanVideoVAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, SetNode, SetNode, SetNode, GetImageSizeAndCount, JWInteger, easy seed, GetNode, WanVideoModelLoader, WanVideoModelLoader, WanVideoModelLoader, SetNode, WanVideoLoraSelect, GetNode, SetNode, SetNode, LoadWanVideoT5TextEncoder, GetNode, GetNode, SetNode, ImageResizeKJv2, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, GetNode, easy promptConcat, Reroute, WanVideoModelLoader, GetNode, GetNode, WanVideoTextEncode, GetNode, GetNode, GetNode, LoadImage, SetNode, ImageSmartSharpen+, CR Prompt Text, easy showAnything, Wan22PromptSelector, WanVideoLoraSelect, PreviewImage, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoImageToVideoEncode, LayerFilter: FilmV2, CR Prompt Text, VHS_VideoCombine, RH_LLMAPI_NODE, Float, WanVideoSigmaToStep, PrimitiveNode, WanVideoSampler, WanVideoScheduler, WanVideoScheduler]
patterns: []
missing: []
---

# 视频生成/图生视频/✅Wan 2.2+Lightx2v-图生视频-kj版本-720p_1950727376542044161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950727376542044161.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `JWInteger`
- `easy seed`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `GetNode`
- `easy promptConcat`
- `Reroute`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `ImageSmartSharpen+`
- `CR Prompt Text`
- `easy showAnything`
- `Wan22PromptSelector`
- `WanVideoLoraSelect`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `LayerFilter: FilmV2`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `RH_LLMAPI_NODE`
- `Float`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`

## 知识

覆盖率 **58%**（48/83）

**有卡**：`JWInteger`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`easy seed`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`easy promptConcat`、`WanVideoTextEncode`、`LoadImage`、`ImageSmartSharpen+`、`CR Prompt Text`、`Wan22PromptSelector`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`LayerFilter: FilmV2`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`Float`、`WanVideoSigmaToStep`、`WanVideoScheduler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
