---
key: 视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json
name: rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json
hash: e3bb281a8ee42bdf
coverage: 0.770833
learned_at: 2026-10-10 23:09:15
nodes: [WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelect, WanVideoVAELoader, Note, INTConstant, WanVideoSampler, WanVideoEmptyEmbeds, GetImageSizeAndCount, WanVideoSampler, WanVideoDecode, WanVideoDecode, RIFE VFI, VHS_VideoCombine, RIFE VFI, MarkdownNote, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSampler, LoadImage, WanVideoTorchCompileSettings, MarkdownNote, VHS_VideoCombine, CreateCFGScheduleFloatList, WanVideoBlockSwap, VHS_VideoCombine, Int, Int, Int, INTConstant, INTConstant, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoSampler, CreateCFGScheduleFloatList, ImageResizeKJv2, VHS_VideoCombine, ShellAgentPluginSaveImage, MarkdownNote, Note, Note, Note, WanVideoTextEncode]
patterns: []
missing: [RIFE VFI, RIFE VFI]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `Note`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoDecode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `RIFE VFI`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `VHS_VideoCombine`
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
- `ShellAgentPluginSaveImage`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncode`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`INTConstant`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`Int`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`ShellAgentPluginSaveImage`、`WanVideoTextEncode`

**缺卡**（2）：`RIFE VFI`、`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
