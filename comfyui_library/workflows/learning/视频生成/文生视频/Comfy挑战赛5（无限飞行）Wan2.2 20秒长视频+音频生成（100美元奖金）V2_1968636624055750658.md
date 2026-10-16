---
key: 视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2 20秒长视频+音频生成（100美元奖金）V2_1968636624055750658.json
name: Comfy挑战赛5（无限飞行）Wan2.2 20秒长视频+音频生成（100美元奖金）V2_1968636624055750658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968636624055750658.json
hash: fd8a8666430dd885
coverage: 0.963303
learned_at: 2026-10-15 22:43:46
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoSampler, Note, INTConstant, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoLoraSelect, INTConstant, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, Float, JWInteger, Note, StringToFloatList, PrimitiveNode, WanVideoTextEncode, WanVideoSampler, VHS_VideoCombine, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetLoRAs, ImageFromBatch+, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, INTConstant, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, Float, WanVideoTextEncode, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, ImageFromBatch+, JWInteger, GetImageSizeAndCount, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, INTConstant, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, Float, WanVideoTextEncode, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, ImageFromBatch+, ImageFromBatch+, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, INTConstant, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, Float, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, WanVideoTextEncode, GetImageSizeAndCount, GetImageSizeAndCount, easy batchAnything, CR Prompt Text, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, CR Prompt Text, CR Prompt Text, VHS_VideoCombine, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VAELoader, SaveLatent, VAEEncode, LayerUtility: PurgeVRAM V2, easy batchAnything, HunyuanVideoFoley, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, easy batchAnything, GetImageSizeAndCount]
patterns: []
missing: []
---

# 视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2 20秒长视频+音频生成（100美元奖金）V2_1968636624055750658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968636624055750658.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（109 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `Note`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `Float`
- `JWInteger`
- `Note`
- `StringToFloatList`
- `PrimitiveNode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `Float`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageFromBatch+`
- `JWInteger`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `Float`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `Float`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy batchAnything`
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `CR Prompt Text`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VAELoader`
- `SaveLatent`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `easy batchAnything`
- `HunyuanVideoFoley`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `easy batchAnything`
- `GetImageSizeAndCount`

## 知识

覆盖率 **96%**（105/109）

**有卡**：`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoSampler`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`Float`、`JWInteger`、`StringToFloatList`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`GetImageSizeAndCount`、`easy batchAnything`、`CR Prompt Text`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`VAELoader`、`SaveLatent`、`VAEEncode`、`HunyuanVideoFoley`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
