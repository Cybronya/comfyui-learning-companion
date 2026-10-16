---
key: 视频生成/文生视频/(KJ版)Wan2.2 MiniCpm 4.5视频洗稿工作流V1_1961658398267916290.json
name: (KJ版)Wan2.2 MiniCpm 4.5视频洗稿工作流V1_1961658398267916290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1961658398267916290.json
hash: 43a5467836a85186
coverage: 0.815789
learned_at: 2026-10-15 22:43:43
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, JWInteger, GetImageSizeAndCount, VHS_VideoCombine, VHS_LoadVideoFFmpeg, LayerUtility: PurgeVRAM, WanVideoEmptyEmbeds, easy showAnything, AILab_MiniCPM_4_V, JWInteger, JWInteger, WanVideoSampler, PrimitiveNode, LoadVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2 MiniCpm 4.5视频洗稿工作流V1_1961658398267916290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1961658398267916290.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `JWInteger`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_LoadVideoFFmpeg`
- `LayerUtility: PurgeVRAM`
- `WanVideoEmptyEmbeds`
- `easy showAnything`
- `AILab_MiniCPM_4_V`
- `JWInteger`
- `JWInteger`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `LoadVideo`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`JWInteger`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`VHS_LoadVideoFFmpeg`、`LayerUtility: PurgeVRAM`、`WanVideoEmptyEmbeds`、`AILab_MiniCPM_4_V`、`LoadVideo`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
