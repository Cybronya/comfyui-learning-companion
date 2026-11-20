---
key: 平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json
name: minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json
hash: 96ef642f6379960d
coverage: 0.892857
learned_at: 2026-11-14 01:14:49
nodes: [VAELoader, CLIPLoader, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, ConditioningZeroOut, KSamplerSelect, BasicScheduler, VAEDecode, ResolutionSelector, VHS_LoadVideo, ComfyMathExpression, LoadImage, SelfLiftH3Sampler, SelfLiftH3TST, VHS_VideoCombine, easy positive, easy loraStackApply, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveFloat, easy cleanGpuUsed, VAEDecodeAudio, LoadAudio, LoadAudio, LoadAudio, PrimitiveInt, VHS_LoadVideo, VHS_LoadVideo, easy loraStack, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json

> 来源文件 `comfyui_library/workflows/平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `VHS_LoadVideo`
- `ComfyMathExpression`
- `LoadImage`
- `SelfLiftH3Sampler` ★核心
- `SelfLiftH3TST`
- `VHS_VideoCombine`
- `easy positive`
- `easy loraStackApply`
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `VAEDecodeAudio` ★核心
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `easy loraStack`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`ResolutionSelector`、`VHS_LoadVideo`、`ComfyMathExpression`、`LoadImage`、`SelfLiftH3Sampler`、`SelfLiftH3TST`、`VHS_VideoCombine`、`easy positive`、`easy loraStackApply`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`VAEDecodeAudio`、`LoadAudio`、`easy loraStack`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
