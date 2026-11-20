---
key: 平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json
name: minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json
hash: cde38588f7dee553
coverage: 0.836364
learned_at: 2026-11-14 01:14:52
nodes: [ResolutionSelector, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, CLIPLoader, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, SelfLiftH3Sampler, BasicScheduler, ConditioningZeroOut, UNETLoader, easy loraStack, easy loraStackApply, ComfySwitchNode, PrimitiveInt, PrimitiveFloat, PrimitiveInt, SelfLiftH3TST, ModelPreviewOverrideKJ, VHS_LoadVideo, VHS_VideoInfo, ComfySwitchNode, PrimitiveFloat, ComfyMathExpression, TrimAudioDuration, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadAudio, LoadAudio, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json

> 来源文件 `comfyui_library/workflows/平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`
- `SelfLiftH3Sampler` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `easy loraStack`
- `easy loraStackApply`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SelfLiftH3TST`
- `ModelPreviewOverrideKJ`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `ComfySwitchNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `TrimAudioDuration`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`CLIPLoader`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`、`SelfLiftH3Sampler`、`BasicScheduler`、`ConditioningZeroOut`、`UNETLoader`、`easy loraStack`、`easy loraStackApply`、`SelfLiftH3TST`、`ModelPreviewOverrideKJ`、`VHS_LoadVideo`、`VHS_VideoInfo`、`TrimAudioDuration`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
