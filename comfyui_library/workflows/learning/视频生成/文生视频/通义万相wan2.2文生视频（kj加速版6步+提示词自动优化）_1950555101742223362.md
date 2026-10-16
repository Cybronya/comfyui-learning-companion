---
key: 视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步+提示词自动优化）_1950555101742223362.json
name: 通义万相wan2.2文生视频（kj加速版6步+提示词自动优化）_1950555101742223362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950555101742223362.json
hash: e0903154de31e994
coverage: 0.805556
learned_at: 2026-10-15 22:43:36
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, WanVideoDecode, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, Note, Note, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, MathExpression|pysssss, WanVideoTextEncode, WanVideoVAELoader, WanVideoEmptyEmbeds, Note, Primitive integer [Crystools], Primitive integer [Crystools], VHS_VideoCombine, Wan22PromptSelector, ShowText|pysssss, ShowText|pysssss, Text Multiline, RH_LLMAPI_NODE]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相wan2.2文生视频（kj加速版6步+提示词自动优化）_1950555101742223362.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950555101742223362.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
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
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Text Multiline`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Primitive integer [Crystools]`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`Wan22PromptSelector`、`Text Multiline`、`RH_LLMAPI_NODE`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
