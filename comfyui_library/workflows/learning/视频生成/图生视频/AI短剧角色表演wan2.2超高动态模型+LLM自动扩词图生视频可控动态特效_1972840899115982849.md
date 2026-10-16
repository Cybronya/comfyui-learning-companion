---
key: 视频生成/图生视频/AI短剧角色表演wan2.2超高动态模型+LLM自动扩词图生视频可控动态特效_1972840899115982849.json
name: AI短剧角色表演wan2.2超高动态模型+LLM自动扩词图生视频可控动态特效_1972840899115982849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972840899115982849.json
hash: 02aa4fadb11a6980
coverage: 0.891892
learned_at: 2026-10-15 22:32:00
nodes: [WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetLoRAs, PrimitiveString, SimpleMath+, WanVideoDecode, GetImageSizeAndCount, Wan22PromptSelector, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM V2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, ShowText|pysssss, easy anythingIndexSwitch, INTConstant, CreateCFGScheduleFloatList, PrimitiveInt, WanVideoSampler, WanVideoSampler, WanVideoSigmaToStep, Float, LoadImage, RHHiddenNodes, WanVideoTextEncode, CR Text, Note, WanVideoScheduler, WanVideoScheduler]
patterns: []
missing: []
---

# 视频生成/图生视频/AI短剧角色表演wan2.2超高动态模型+LLM自动扩词图生视频可控动态特效_1972840899115982849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972840899115982849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `PrimitiveString`
- `SimpleMath+`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `Wan22PromptSelector`
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM V2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `easy anythingIndexSwitch`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSigmaToStep`
- `Float`
- `LoadImage`
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `CR Text`
- `Note`
- `WanVideoScheduler`
- `WanVideoScheduler`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`SimpleMath+`、`WanVideoDecode`、`GetImageSizeAndCount`、`Wan22PromptSelector`、`WanVideoImageToVideoEncode`、`LayerUtility: PurgeVRAM V2`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoSigmaToStep`、`Float`、`LoadImage`、`RHHiddenNodes`、`WanVideoTextEncode`、`CR Text`、`WanVideoScheduler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
