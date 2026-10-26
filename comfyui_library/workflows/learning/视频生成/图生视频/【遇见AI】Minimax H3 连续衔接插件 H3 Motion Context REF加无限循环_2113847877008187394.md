---
key: 视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json
name: 【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json
hash: 77c2b523677f393a
coverage: 0.755556
learned_at: 2026-10-26 22:15:13
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, SamplerCustomAdvanced, LoadAudio, VHS_LoadVideo, RandomNoise, KSamplerSelect, BasicScheduler, ResolutionSelector, ComfyMathExpression, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, VAEDecode, VAEDecodeAudio, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, easy batchAnything, easy showAnything, easy textIndexSwitch, LoadImage, LoadImage, MiniMaxH3MotionContextTrim, CreateVideo, easy forLoopEnd, ShowText|pysssss, easy ifElse, easy forLoopStart, BasicGuider, CreateVideo, PrimitiveFloat, MiniMaxH3ReferenceToVideo, MiniMaxH3MotionContext, GoohaiAnySwitch, easy ifElse, MiniMaxH3MotionContextLoadLatent, ComfyMathExpression, MiniMaxH3MotionContextSaveLatent, SaveVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【遇见AI】Minimax H3 连续衔接插件 H3 Motion Context REF加无限循环_2113847877008187394.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SamplerCustomAdvanced` ★核心
- `LoadAudio`
- `VHS_LoadVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy batchAnything`
- `easy showAnything`
- `easy textIndexSwitch`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MotionContextTrim`
- `CreateVideo`
- `easy forLoopEnd`
- `ShowText|pysssss`
- `easy ifElse`
- `easy forLoopStart`
- `BasicGuider`
- `CreateVideo`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3MotionContext`
- `GoohaiAnySwitch`
- `easy ifElse`
- `MiniMaxH3MotionContextLoadLatent`
- `ComfyMathExpression`
- `MiniMaxH3MotionContextSaveLatent`
- `SaveVideo`
- `SaveVideo`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SamplerCustomAdvanced`、`LoadAudio`、`VHS_LoadVideo`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`VAEDecodeAudio`、`easy batchAnything`、`easy textIndexSwitch`、`LoadImage`、`MiniMaxH3MotionContextTrim`、`CreateVideo`、`easy forLoopEnd`、`easy forLoopStart`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MotionContext`、`GoohaiAnySwitch`、`MiniMaxH3MotionContextLoadLatent`、`MiniMaxH3MotionContextSaveLatent`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
