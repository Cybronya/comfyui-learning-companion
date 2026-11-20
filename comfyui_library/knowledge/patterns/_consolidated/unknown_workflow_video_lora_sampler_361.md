---
name: unknown_workflow_video_lora_sampler_361
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.866875
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveInt, ResolutionSelector, SelfLiftH3Sampler, SelfLiftH3TST, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy loraStack, easy loraStackApply]
problems: []
missing: []
members: [平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json, 平台全量/minimax h3 SelfLift  二采基础工作流_2117833099823374337.json, 平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json, 平台全量/minimax h3 pika_h3 SelfLift 二采基础工作流_2117843603002322946.json, 平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json, 平台全量/minimax h3 动作迁移_SelfLift 人物替换_2114736679738232834.json, "数字人/数字人/h3+动作迁移 人物替换 Action Transfer, Character Replacemen_2116341700925939713.json", "视频生成/图生视频/h3+动作迁移_人物替换_Action_Transfer,_Character_Replacemen_2116359873431687170.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_361

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/minimax h3 Fast_omni模型 SelfLift  二采基础工作流_2117882051616661506.json、平台全量/minimax h3 SelfLift  二采基础工作流_2117833099823374337.json、平台全量/minimax h3 fast_h3_omni模型 动作迁移_SelfLift 人物替换二采_2117825972014772226.json、平台全量/minimax h3 pika_h3 SelfLift 二采基础工作流_2117843603002322946.json、平台全量/minimax h3 pika_h3 lora 人物迁移SelfLift 二采_2117586709830529026.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SelfLiftH3TST`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy loraStack`
- `easy loraStackApply`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `easy positive` —— 6/8 个有
- `ComfySwitchNode` —— 5/8 个有
- `TrimAudioDuration` —— 5/8 个有
- `VHS_VideoInfo` —— 5/8 个有
- `ImageBatchMulti` —— 3/8 个有
- `ImageFromBatch` —— 3/8 个有
- `RepeatImageBatch` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
