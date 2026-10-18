---
key: 视频生成/文生视频/wan2.2文生视频_自动润色提示词_1951121604451442689.json
name: wan2.2文生视频_自动润色提示词_1951121604451442689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_自动润色提示词_1951121604451442689.json
hash: 984db511dc43f7d7
coverage: 0.972222
learned_at: 2026-10-15 22:43:37
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSampler, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, GetImageSizeAndCount, JWInteger, JWInteger, SimpleMath+, QwenLoader, WanVideoPromptExtender, WanVideoSampler, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, WanVideoScheduler, WanVideoScheduler, INTConstant, WanVideoSigmaToStep, Float, WanVideoTextEncode, ShowText|pysssss, JWInteger, VHS_VideoCombine, CR Text]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频_自动润色提示词_1951121604451442689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951121604451442689.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `QwenLoader`
- `WanVideoPromptExtender`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `CreateCFGScheduleFloatList`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `JWInteger`
- `VHS_VideoCombine`
- `CR Text`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`JWInteger`、`SimpleMath+`、`QwenLoader`、`WanVideoPromptExtender`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`WanVideoTextEncode`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
