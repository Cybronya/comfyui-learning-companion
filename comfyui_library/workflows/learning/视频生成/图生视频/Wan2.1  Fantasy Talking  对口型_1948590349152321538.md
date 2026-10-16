---
key: 视频生成/图生视频/Wan2.1  Fantasy Talking  对口型_1948590349152321538.json
name: Wan2.1  Fantasy Talking  对口型_1948590349152321538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948590349152321538.json
hash: 3c520f87750b8bef
coverage: 0.574074
learned_at: 2026-10-15 22:30:47
nodes: [GetNode, GetNode, GetNode, easy clearCacheAll, easy clearCacheAll, GetNode, easy clearCacheAll, GetNode, GetNode, GetNode, GetNode, GetNode, easy clearCacheAll, easy clearCacheAll, GetNode, easy clearCacheAll, WanVideoBlockSwap, WanVideoVRAMManagement, WanVideoSampler, WanVideoDecode, GetNode, FantasyTalkingWav2VecEmbeds, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoTeaCache, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, SetNode, LoadAudio, SetNode, GetNode, SetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTorchCompileSettings, SetNode, FantasyTalkingModelLoader, WanVideoModelLoader, SetNode, LoadImage, ImageResizeKJ, VHS_VideoCombine, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1  Fantasy Talking  对口型_1948590349152321538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948590349152321538.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `GetNode`
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `GetNode`
- `easy clearCacheAll`
- `WanVideoBlockSwap`
- `WanVideoVRAMManagement`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `FantasyTalkingWav2VecEmbeds`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoTeaCache`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `FantasyTalkingModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `LoadImage`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **57%**（31/54）

**有卡**：`easy clearCacheAll`、`WanVideoBlockSwap`、`WanVideoVRAMManagement`、`WanVideoSampler`、`WanVideoDecode`、`FantasyTalkingWav2VecEmbeds`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoTeaCache`、`DownloadAndLoadWav2VecModel`、`INTConstant`、`LoadAudio`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`FantasyTalkingModelLoader`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJ`、`VHS_VideoCombine`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
