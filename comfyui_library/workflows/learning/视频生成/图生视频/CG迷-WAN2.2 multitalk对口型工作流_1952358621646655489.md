---
key: 视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json
name: CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json
hash: 79fb462d00bb5e05
coverage: 0.933333
learned_at: 2026-10-15 22:31:01
nodes: [LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetImageSizeAndCount, DownloadAndLoadWav2VecModel, WanVideoDecode, CreateCFGScheduleFloatList, INTConstant, MultiTalkWav2VecEmbeds, INTConstant, PrimitiveNode, VHS_VideoCombine, MarkdownNote, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, INTConstant, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, LoadAudio, WanVideoSampler, WanVideoSampler, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952358621646655489.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `DownloadAndLoadWav2VecModel`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `MultiTalkWav2VecEmbeds`
- `INTConstant`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`INTConstant`、`MultiTalkWav2VecEmbeds`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`MultiTalkModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LoadAudio`、`WanVideoSampler`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
