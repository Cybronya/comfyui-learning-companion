---
key: 视频生成/图生视频/KJ-Wan2.2-6步加速文生视频_1950060354116214786.json
name: KJ-Wan2.2-6步加速文生视频_1950060354116214786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/KJ-Wan2.2-6步加速文生视频_1950060354116214786.json
hash: 635671e979eb94b1
coverage: 0.848485
learned_at: 2026-10-15 22:30:52
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, WanVideoDecode, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, Note, Note, Note, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, MathExpression|pysssss, WanVideoVAELoader, WanVideoEmptyEmbeds, LoadImage, Note, Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ-Wan2.2-6步加速文生视频_1950060354116214786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950060354116214786.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `Note`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `LoadImage`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`Primitive integer [Crystools]`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`LoadImage`、`Text Multiline`、`WanVideoBlockSwap`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
