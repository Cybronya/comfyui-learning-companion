---
key: 平台全量/MiniMaxH3人物替换_简易双采版_v1.2_2115645149148700674.json
name: MiniMaxH3人物替换_简易双采版_v1.2_2115645149148700674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMaxH3人物替换_简易双采版_v1.2_2115645149148700674.json
hash: d3da9f03e5ee61d5
coverage: 0.83871
learned_at: 2026-11-14 00:44:38
nodes: [UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, LoadImage, VHS_LoadVideo, ComfyMathExpression, PrimitiveStringMultiline, MiniMaxH3AudioConditioningT8, MiniMaxH3AddGuide, ConditioningZeroOut, KSamplerSelect, BasicScheduler, SelfLiftH3Sampler, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MarkdownNote, Note, GetImageSizeAndCount, PrimitiveFloat, ComfyMathExpression, ComfyMathExpression, VHS_VideoInfoLoaded, PrimitiveInt, ImageFromBatch, TrimAudioDuration, ComfyMathExpression]
patterns: []
missing: []
---

# 平台全量/MiniMaxH3人物替换_简易双采版_v1.2_2115645149148700674.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMaxH3人物替换_简易双采版_v1.2_2115645149148700674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `VHS_LoadVideo`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AddGuide`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `GetImageSizeAndCount`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoInfoLoaded`
- `PrimitiveInt`
- `ImageFromBatch`
- `TrimAudioDuration`
- `ComfyMathExpression`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_LoadVideo`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3AddGuide`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`TrimAudioDuration`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SelfLiftH3Sampler
