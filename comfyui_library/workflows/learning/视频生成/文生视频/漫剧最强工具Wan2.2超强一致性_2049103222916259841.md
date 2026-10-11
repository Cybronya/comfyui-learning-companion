---
key: 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json
name: 漫剧最强工具Wan2.2超强一致性_2049103222916259841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json
hash: 524020d0df5a8e69
coverage: 0.765957
learned_at: 2026-10-11 19:49:50
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelect, WanVideoVAELoader, Note, Note, Note, Note, INTConstant, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoDecode, RIFE VFI, VHS_VideoCombine, RIFE VFI, MarkdownNote, MarkdownNote, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSampler, LoadImage, WanVideoTorchCompileSettings, MarkdownNote, CreateCFGScheduleFloatList, WanVideoBlockSwap, VHS_VideoCombine, Int, Int, Int, INTConstant, INTConstant, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, ImageResizeKJv2, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoTextEncode]
patterns: []
missing: [RIFE VFI, RIFE VFI]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `Note`
- `Note`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `RIFE VFI`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `INTConstant`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoTextEncode`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`INTConstant`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`Int`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`WanVideoTextEncode`

**缺卡**（2）：`RIFE VFI`、`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
