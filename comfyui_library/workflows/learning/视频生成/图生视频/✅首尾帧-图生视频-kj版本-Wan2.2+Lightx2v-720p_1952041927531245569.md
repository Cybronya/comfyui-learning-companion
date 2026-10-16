---
key: 视频生成/图生视频/✅首尾帧-图生视频-kj版本-Wan2.2+Lightx2v-720p_1952041927531245569.json
name: ✅首尾帧-图生视频-kj版本-Wan2.2+Lightx2v-720p_1952041927531245569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952041927531245569.json
hash: 9c9d4a00473bde36
coverage: 0.542553
learned_at: 2026-10-15 22:30:59
nodes: [SetNode, SetNode, GetNode, LoadImage, LoadImage, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoTextEncode, SetNode, GetNode, SetNode, SetNode, ImageSmartSharpen+, SetNode, GetNode, SetNode, ImageSmartSharpen+, SetNode, PreviewImage, GetNode, ImageResizeKJv2, ImageResizeKJv2, JWInteger, JWInteger, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, GetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, SetNode, GetImageSizeAndCount, GetNode, GetNode, CreateCFGScheduleFloatList, GetNode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSampler, WanVideoSampler, Float, WanVideoVAELoader, SetNode, easy seed, PrimitiveNode, ShowText|pysssss, easy imageConcat, easy promptConcat, GetNode, Wan22PromptSelector, WanVideoLoraSelect, JWInteger, PreviewImage, CR Prompt Text, VHS_VideoCombine, WanVideoLoraSelect, PrimitiveNode, WanVideoImageToVideoEncode, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, CR Prompt Text, CR Prompt Text, RH_LLMAPI_NODE, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/✅首尾帧-图生视频-kj版本-Wan2.2+Lightx2v-720p_1952041927531245569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952041927531245569.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageSmartSharpen+`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Float`
- `WanVideoVAELoader`
- `SetNode`
- `easy seed`
- `PrimitiveNode`
- `ShowText|pysssss`
- `easy imageConcat`
- `easy promptConcat`
- `GetNode`
- `Wan22PromptSelector`
- `WanVideoLoraSelect`
- `JWInteger`
- `PreviewImage`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `CR Prompt Text`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`

## 知识

覆盖率 **54%**（51/94）

**有卡**：`LoadImage`、`WanVideoTextEncode`、`ImageSmartSharpen+`、`ImageResizeKJv2`、`JWInteger`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`Float`、`WanVideoVAELoader`、`easy seed`、`easy imageConcat`、`easy promptConcat`、`Wan22PromptSelector`、`CR Prompt Text`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`RH_LLMAPI_NODE`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
