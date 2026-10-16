---
key: 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json
name: Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950206171439390721.json
hash: bbc9feb64dd29702
coverage: 0.878788
learned_at: 2026-10-15 22:43:35
nodes: [WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoEmptyEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoDecode, WanVideoSampler, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSampler, Note, Note, Note, Note, WanVideoTextEncode, Text Multiline, PreViewVideo, CreateVideo, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版非常逼真目前最牛_1950206171439390721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950206171439390721.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（33 个）：
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `Text Multiline`
- `PreViewVideo`
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSampler`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoTextEncode`、`Text Multiline`、`PreViewVideo`、`CreateVideo`、`SaveVideo`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
