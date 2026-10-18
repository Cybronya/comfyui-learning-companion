---
key: 视频生成/图生视频/wan2.2 循环动态壁纸_1914160660647768066.json
name: wan2.2 循环动态壁纸_1914160660647768066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 循环动态壁纸_1914160660647768066.json
hash: 0c9e6693f06f40fe
coverage: 0.8125
learned_at: 2026-10-15 22:29:35
nodes: [intToFloat _O, WanVideoEasyCache, WanVideoSLG, WanVideoExperimentalArgs, PrimitiveStringMultiline, RH_Captioner, PrimitiveStringMultiline, Text Concatenate, PrimitiveStringMultiline, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, MarkdownNote, MarkdownNote, WanVideoTextEncode, WanVideoAddExtraLatent, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, WanVideoEncode, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, RHHiddenNodes, RHHiddenNodes, LoadImage, LoadImage, Int, Int, LoadImage, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 循环动态壁纸_1914160660647768066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914160660647768066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `intToFloat _O`
- `WanVideoEasyCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `PrimitiveStringMultiline`
- `RH_Captioner`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoAddExtraLatent`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `LoadImage`
- `Int`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`intToFloat _O`、`WanVideoEasyCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`RH_Captioner`、`Text Concatenate`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`WanVideoAddExtraLatent`、`WanVideoEmptyEmbeds`、`MathExpression|pysssss`、`WanVideoEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`RHHiddenNodes`、`LoadImage`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoAddExtraLatent
