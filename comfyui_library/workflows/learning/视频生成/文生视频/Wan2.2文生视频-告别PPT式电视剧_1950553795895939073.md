---
key: 视频生成/文生视频/Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json
name: Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950553795895939073.json
hash: dfb46621ee634526
coverage: 0.928571
learned_at: 2026-10-15 22:43:36
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, INTConstant, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, INTConstant, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频-告别PPT式电视剧_1950553795895939073.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950553795895939073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（28 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `INTConstant`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`

**用到的条目**：CLIPTextEncode、CLIPLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
