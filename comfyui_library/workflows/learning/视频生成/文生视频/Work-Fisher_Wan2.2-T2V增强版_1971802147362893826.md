---
key: 视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json
name: Work-Fisher_Wan2.2-T2V增强版_1971802147362893826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json
hash: 5dfa3a987832b1fe
coverage: 0.806452
learned_at: 2026-10-10 23:08:21
nodes: [WanVideoVAELoader, Int, Note, Note, WanVideoEmptyEmbeds, INTConstant, INTConstant, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoDecode, WanVideoSampler, Note, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, RIFE VFI, ImageListToImageBatch, ImageFromBatch, SaveImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, Note, WanVideoTextEncode, Int, VHS_VideoCombine, LoadImage, Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, Int]
patterns: []
missing: [RIFE VFI]
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Work-Fisher_Wan2.2-T2V增强版_1971802147362893826.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（31 个）：
- `WanVideoVAELoader`
- `Int`
- `Note`
- `Note`
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Note`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `ImageListToImageBatch`
- `ImageFromBatch`
- `SaveImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `WanVideoTextEncode`
- `Int`
- `VHS_VideoCombine`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelectMulti`
- `Int`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`WanVideoVAELoader`、`Int`、`WanVideoEmptyEmbeds`、`INTConstant`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`ImageListToImageBatch`、`ImageFromBatch`、`SaveImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelectMulti`

**缺卡**（1）：`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
