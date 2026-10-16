---
key: 视频生成/图生视频/wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1950422709600698370.json
name: wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1950422709600698370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950422709600698370.json
hash: 7d4f1c39b14dd012
coverage: 0.941176
learned_at: 2026-10-15 22:30:54
nodes: [LayerUtility: PurgeVRAM, WanVideoBlockSwap, WanVideoModelLoader, WanVideoImageClipEncode, WanVideoSampler, WanVideoTextEncode, ImpactInt, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoLoraSelect, LoadImage, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, JjkText, ImpactInt]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1950422709600698370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950422709600698370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `ImpactInt`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoLoraSelect`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JjkText`
- `ImpactInt`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoTextEncode`、`ImpactInt`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoLoraSelect`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
