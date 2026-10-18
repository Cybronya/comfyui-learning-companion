---
key: 视频生成/图生视频/刀切玻璃水晶水果蔬菜 图转视频工作流 wan2.1+lora_2054447841707347969.json
name: 刀切玻璃水晶水果蔬菜 图转视频工作流 wan2.1+lora_2054447841707347969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/刀切玻璃水晶水果蔬菜 图转视频工作流 wan2.1+lora_2054447841707347969.json
hash: e85c18a3ab21ea6b
coverage: 0.903226
learned_at: 2026-10-15 22:37:47
nodes: [LayerUtility: PurgeVRAM, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, ImpactInt, WanVideoVAELoader, RH_Translator, MMAudioModelLoader, MMAudioFeatureUtilsLoader, MMAudioSampler, Float, VHS_VideoCombine, String, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, PreviewAudio, WanVideoModelLoader, easy cleanGpuUsed, WanVideoImageClipEncode, easy cleanGpuUsed, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, JjkText, Note, WanVideoDecode, Note, ImpactInt, WanVideoSampler, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/刀切玻璃水晶水果蔬菜 图转视频工作流 wan2.1+lora_2054447841707347969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054447841707347969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `ImpactInt`
- `WanVideoVAELoader`
- `RH_Translator`
- `MMAudioModelLoader`
- `MMAudioFeatureUtilsLoader`
- `MMAudioSampler` ★核心
- `Float`
- `VHS_VideoCombine`
- `String`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `PreviewAudio`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `WanVideoImageClipEncode`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `JjkText`
- `Note`
- `WanVideoDecode`
- `Note`
- `ImpactInt`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`ImpactInt`、`WanVideoVAELoader`、`RH_Translator`、`MMAudioModelLoader`、`MMAudioFeatureUtilsLoader`、`MMAudioSampler`、`Float`、`VHS_VideoCombine`、`String`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`PreviewAudio`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、MMAudioSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode
