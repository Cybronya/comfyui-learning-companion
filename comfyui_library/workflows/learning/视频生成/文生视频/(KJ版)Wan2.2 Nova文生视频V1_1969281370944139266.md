---
key: 视频生成/文生视频/(KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json
name: (KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json
hash: 695dfc590dd4413f
coverage: 0.853659
learned_at: 2026-10-15 22:43:46
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoLoraSelect, PrimitiveNode, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoLoraSelect, CR Prompt Text, Float, INTConstant, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, ImageFromBatch+, StringToFloatList, WanVideoSetBlockSwap, WanVideoBlockSwap, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969281370944139266.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `CR Prompt Text`
- `Float`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringToFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `RHHiddenNodes`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`JWInteger`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`CR Prompt Text`、`Float`、`INTConstant`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageFromBatch+`、`StringToFloatList`、`WanVideoBlockSwap`、`RHHiddenNodes`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
