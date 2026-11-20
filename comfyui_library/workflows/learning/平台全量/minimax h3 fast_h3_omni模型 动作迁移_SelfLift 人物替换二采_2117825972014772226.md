---
key: 平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json
name: minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json
hash: fb2550929480fb11
coverage: 0.875
learned_at: 2026-11-14 01:14:51
nodes: [VAELoader, CLIPLoader, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, ConditioningZeroOut, KSamplerSelect, BasicScheduler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ResolutionSelector, TrimAudioDuration, ComfyMathExpression, VHS_LoadVideo, ComfyMathExpression, LoadImage, SelfLiftH3Sampler, SelfLiftH3TST, VHS_VideoCombine, easy positive, VHS_VideoInfo, easy loraStack, easy loraStackApply, ComfySwitchNode, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveFloat, easy cleanGpuUsed, ComfySwitchNode, VAEDecodeAudio, LoadAudio, LoadAudio, LoadAudio, PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json

> 来源文件 `comfyui_library/workflows/平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json`

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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `VHS_LoadVideo`
- `ComfyMathExpression`
- `LoadImage`
- `SelfLiftH3Sampler` ★核心
- `SelfLiftH3TST`
- `VHS_VideoCombine`
- `easy positive`
- `VHS_VideoInfo`
- `easy loraStack`
- `easy loraStackApply`
- `ComfySwitchNode`
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
- `ComfySwitchNode`
- `VAEDecodeAudio` ★核心
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveInt`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ResolutionSelector`、`TrimAudioDuration`、`ComfyMathExpression`、`VHS_LoadVideo`、`LoadImage`、`SelfLiftH3Sampler`、`SelfLiftH3TST`、`VHS_VideoCombine`、`easy positive`、`VHS_VideoInfo`、`easy loraStack`、`easy loraStackApply`、`easy cleanGpuUsed`、`VAEDecodeAudio`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
