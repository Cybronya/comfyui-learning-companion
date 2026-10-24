---
name: unknown_workflow_video_lora_sampler_614
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.438
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, GoohaiUniversalSlider, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json, 视频生成/图生视频/自己用的_2110993734681841665.json, 视频生成/图生视频/自用YZ金鱼-MiniMax H3 终极篇-文武双全_2110932091864174593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_614

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json、视频生成/图生视频/自己用的_2110993734681841665.json、视频生成/图生视频/自用YZ金鱼-MiniMax H3 终极篇-文武双全_2110932091864174593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `GoohaiUniversalSlider`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `MiniMaxChunkFeedForward` —— 1/3 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有
- `T8SpeechReference` —— 1/3 个有
- `ZNGB_AudioConcatMulti` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
