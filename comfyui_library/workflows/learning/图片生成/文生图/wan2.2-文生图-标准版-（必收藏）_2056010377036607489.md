---
key: 图片生成/文生图/wan2.2-文生图-标准版-（必收藏）_2056010377036607489.json
name: wan2.2-文生图-标准版-（必收藏）_2056010377036607489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2-文生图-标准版-（必收藏）_2056010377036607489.json
hash: 84d4a199650ddede
coverage: 1
learned_at: 2026-10-21 02:57:40
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, StringToFloatList, FloatToSigmas, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, Int, Int, WanVideoSampler, WanVideoSEVAELoader, WanVideoTextEncode, VHS_VideoCombine, UpscaleModelLoader, VHS_VideoCombine, WanVideoDecode, PurgeVRAM_UTK, ImageUpscaleWithModel, PurgeVRAM_UTK, PurgeVRAM_UTK, WanVideoSampler]
patterns: []
missing: []
---

# 图片生成/文生图/wan2.2-文生图-标准版-（必收藏）_2056010377036607489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2-文生图-标准版-（必收藏）_2056010377036607489.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `StringToFloatList`
- `FloatToSigmas`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `WanVideoSampler` ★核心
- `WanVideoSEVAELoader`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `PurgeVRAM_UTK`
- `ImageUpscaleWithModel`
- `PurgeVRAM_UTK`
- `PurgeVRAM_UTK`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`StringToFloatList`、`FloatToSigmas`、`WanVideoLoraSelect`、`Int`、`WanVideoSampler`、`WanVideoSEVAELoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`UpscaleModelLoader`、`WanVideoDecode`、`PurgeVRAM_UTK`、`ImageUpscaleWithModel`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoSEVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、ImageUpscaleWithModel
