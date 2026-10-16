---
key: 视频生成/图生视频/wan2.2图生视频4步加速LORA_1955641756994846722.json
name: wan2.2图生视频4步加速LORA_1955641756994846722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955641756994846722.json
hash: b74937ed15d362ec
coverage: 1
learned_at: 2026-10-15 22:31:09
nodes: [WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoTextEncodeSingle, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, SimpleMath+, SimpleMath+, WanVideoApplyNAG, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSampler, ImpactInt, ImpactInt, ImpactInt, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, CR Text, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频4步加速LORA_1955641756994846722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955641756994846722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoTextEncodeSingle`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CR Text`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImpactInt`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CR Text`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelect
