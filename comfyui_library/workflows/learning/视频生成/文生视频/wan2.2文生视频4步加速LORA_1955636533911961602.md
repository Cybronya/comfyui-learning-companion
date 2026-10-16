---
key: 视频生成/文生视频/wan2.2文生视频4步加速LORA_1955636533911961602.json
name: wan2.2文生视频4步加速LORA_1955636533911961602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955636533911961602.json
hash: 933849a3fbf76cfb
coverage: 1
learned_at: 2026-10-15 22:43:40
nodes: [WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoApplyNAG, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoSetBlockSwap, ImpactInt, ImpactInt, SimpleMath+, WanVideoEmptyEmbeds, SimpleMath+, WanVideoSampler, INTConstant, VHS_VideoCombine, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoContextOptions, ImpactInt, CR Text]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频4步加速LORA_1955636533911961602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955636533911961602.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `ImpactInt`
- `ImpactInt`
- `SimpleMath+`
- `WanVideoEmptyEmbeds`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `ImpactInt`
- `CR Text`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImpactInt`、`SimpleMath+`、`WanVideoEmptyEmbeds`、`INTConstant`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoContextOptions`、`CR Text`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoLoraSelect、WanVideoSetLoRAs、GetImageSizeAndCount
