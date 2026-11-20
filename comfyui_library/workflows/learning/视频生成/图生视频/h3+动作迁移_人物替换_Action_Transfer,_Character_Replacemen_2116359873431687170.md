---
key: 视频生成/图生视频/h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170.json
name: h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170.json
hash: e42b0b31bb592bbb
coverage: 0.870968
learned_at: 2026-11-02 19:18:53
nodes: [VAELoader, CLIPLoader, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, ConditioningZeroOut, KSamplerSelect, BasicScheduler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, ResolutionSelector, TrimAudioDuration, ComfyMathExpression, VHS_LoadVideo, ComfyMathExpression, LoadImage, SelfLiftH3Sampler, SelfLiftH3TST, VHS_VideoCombine, easy positive, VHS_VideoInfo, ImageFromBatch, ImageBatchMulti, ComfyMathExpression, ComfyMathExpression, RepeatImageBatch, easy loraStack, easy loraStackApply, ComfySwitchNode, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveFloat, easy cleanGpuUsed, ComfySwitchNode, VAEDecodeAudio, LoadAudio, LoadAudio, LoadAudio, ComfySwitchNode, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（62 个）：
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
- `ImageFromBatch`
- `ImageBatchMulti`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RepeatImageBatch`
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
- `ComfySwitchNode`
- `PrimitiveInt`

## 知识

覆盖率 **87%**（54/62）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`ResolutionSelector`、`TrimAudioDuration`、`ComfyMathExpression`、`VHS_LoadVideo`、`LoadImage`、`SelfLiftH3Sampler`、`SelfLiftH3TST`、`VHS_VideoCombine`、`easy positive`、`VHS_VideoInfo`、`ImageFromBatch`、`ImageBatchMulti`、`RepeatImageBatch`、`easy loraStack`、`easy loraStackApply`、`easy cleanGpuUsed`、`VAEDecodeAudio`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
