---
key: 视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json
name: 阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/阿里巴巴最新免费数字人 Fantasy Talking for comfyUI工作流_1917812826264502273.json
hash: 7e4c3d344658ebc2
coverage: 0.370968
learned_at: 2026-10-10 23:14:17
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVRAMManagement, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, easy clearCacheAll, easy clearCacheAll, GetNode, WanVideoDecode, CreateCFGScheduleFloatList, SetNode, Note, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, GetNode, easy clearCacheAll, SetNode, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetNode, GetNode, GetNode, easy clearCacheAll, FantasyTalkingWav2VecEmbeds, VHS_VideoCombine, WanVideoModelLoader, CLIPVisionLoader, Note, Note, MarkdownNote, Note, Note, Note, WanVideoSampler, SetNode, GetNode, easy clearCacheAll, GetNode, easy clearCacheAll, Note, SetNode, INTConstant, SetNode, SetNode, Note, Note, WanVideoTeaCache, WanVideoTextEncode, ImageResizeKJ, INTConstant, LoadAudio, LoadImage]
patterns: []
missing: [easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
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

覆盖率 **37%**（23/62）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVRAMManagement`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`DownloadAndLoadWav2VecModel`、`FantasyTalkingModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`FantasyTalkingWav2VecEmbeds`、`VHS_VideoCombine`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoSampler`、`INTConstant`、`WanVideoTeaCache`、`WanVideoTextEncode`、`ImageResizeKJ`、`LoadAudio`、`LoadImage`

**缺卡**（6）：`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
