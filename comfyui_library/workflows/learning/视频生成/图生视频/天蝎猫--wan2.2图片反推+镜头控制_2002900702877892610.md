---
key: 视频生成/图生视频/天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json
name: 天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json
hash: 744e3622e8d9a373
coverage: 0.61194
learned_at: 2026-10-15 22:33:49
nodes: [SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, LoadWanVideoT5TextEncoder, Anything Everywhere, Anything Everywhere, WanVideoSetLoRAs, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, VHS_VideoCombine, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, GetNode, GetNode, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, PrimitiveInt, SetNode, GetNode, ImageResizeKJ, GetNode, SetNode, GetNode, WanVideoEncode, ImageResizeKJ, CreateCFGScheduleFloatList, Seed (rgthree), WanVideoSigmaToStep, FloatConstant, GetNode, GetNode, GetNode, SetNode, GetNode, ImageConcanate, WanVideoImageToVideoEncode, PrimitiveInt, PrimitiveInt, SetNode, PreviewImage, WanVideoScheduler, WanVideoScheduler, VHS_LoadVideo, VHS_VideoCombine, SaveVideo, Text Multiline (Code Compatible), LoadImage, easy showAnything, CR Prompt Text, RH_Jimeng_Image2Video_V2, Qwen3_VQA]
patterns: []
missing: []
---

# 视频生成/图生视频/天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2002900702877892610.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoSetLoRAs`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `ImageResizeKJ`
- `CreateCFGScheduleFloatList`
- `Seed (rgthree)`
- `WanVideoSigmaToStep`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageConcanate`
- `WanVideoImageToVideoEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `PreviewImage`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `SaveVideo`
- `Text Multiline (Code Compatible)`
- `LoadImage`
- `easy showAnything`
- `CR Prompt Text`
- `RH_Jimeng_Image2Video_V2`
- `Qwen3_VQA`

## 知识

覆盖率 **61%**（41/67）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoSampler`、`ImageResizeKJ`、`WanVideoEncode`、`CreateCFGScheduleFloatList`、`Seed (rgthree)`、`WanVideoSigmaToStep`、`FloatConstant`、`ImageConcanate`、`WanVideoImageToVideoEncode`、`WanVideoScheduler`、`VHS_LoadVideo`、`SaveVideo`、`Text Multiline (Code Compatible)`、`LoadImage`、`CR Prompt Text`、`RH_Jimeng_Image2Video_V2`、`Qwen3_VQA`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
