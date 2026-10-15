---
key: 视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json
name: Wan2.2文生视频_1994337581800292354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json
hash: 4e29761b5e30cc57
coverage: 0.972222
learned_at: 2026-10-15 22:47:15
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoBlockSwap, GetImageSizeAndCount, SimpleMath+, WanVideoSampler, WanVideoEmptyEmbeds, INTConstant, WanVideoSigmaToStep, Float, WanVideoTextEncode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoScheduler, WanVideoScheduler, JWInteger, JWInteger, JWInteger, QwenLoader, CR Text, WanVideoPromptExtender, ShowText|pysssss, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `QwenLoader`
- `CR Text`
- `WanVideoPromptExtender`
- `ShowText|pysssss`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`SimpleMath+`、`WanVideoEmptyEmbeds`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`JWInteger`、`QwenLoader`、`CR Text`、`WanVideoPromptExtender`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
