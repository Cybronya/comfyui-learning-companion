---
key: 视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json
name: 阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json
hash: 7e4c3d344658ebc2
coverage: 0.467742
learned_at: 2026-10-15 22:49:05
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVRAMManagement, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, easy clearCacheAll, easy clearCacheAll, GetNode, WanVideoDecode, CreateCFGScheduleFloatList, SetNode, Note, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, GetNode, easy clearCacheAll, SetNode, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetNode, GetNode, GetNode, easy clearCacheAll, FantasyTalkingWav2VecEmbeds, VHS_VideoCombine, WanVideoModelLoader, CLIPVisionLoader, Note, Note, MarkdownNote, Note, Note, Note, WanVideoSampler, SetNode, GetNode, easy clearCacheAll, GetNode, easy clearCacheAll, Note, SetNode, INTConstant, SetNode, SetNode, Note, Note, WanVideoTeaCache, WanVideoTextEncode, ImageResizeKJ, INTConstant, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVRAMManagement`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `GetNode`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `SetNode`
- `Note`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `easy clearCacheAll`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `FantasyTalkingWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `Note`
- `Note`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `easy clearCacheAll`
- `GetNode`
- `easy clearCacheAll`
- `Note`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `INTConstant`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **47%**（29/62）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVRAMManagement`、`easy clearCacheAll`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`FantasyTalkingWav2VecEmbeds`、`VHS_VideoCombine`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoSampler`、`INTConstant`、`WanVideoTeaCache`、`WanVideoTextEncode`、`ImageResizeKJ`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
