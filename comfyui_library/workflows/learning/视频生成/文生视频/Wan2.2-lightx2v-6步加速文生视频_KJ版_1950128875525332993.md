---
key: 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json
name: Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950128875525332993.json
hash: 3b995cf65d2acf20
coverage: 0.878788
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoEmptyEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoDecode, WanVideoSampler, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSampler, Text Multiline, Note, Note, Note, Note, VHS_VideoCombine, SaveVideo, CreateVideo, PreViewVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-lightx2v-6步加速文生视频_KJ版_1950128875525332993.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950128875525332993.json`

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
- `WanVideoTextEncode`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `Text Multiline`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `SaveVideo`
- `CreateVideo`
- `PreViewVideo`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSampler`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`MathExpression|pysssss`、`Text Multiline`、`VHS_VideoCombine`、`SaveVideo`、`CreateVideo`、`PreViewVideo`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
