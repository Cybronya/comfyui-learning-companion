---
name: unknown_workflow_lora_sampler_unet_27
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.445333
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/H3_家庭储能广告_15秒_三图参考_2110987996991410177.json, 视频生成/图生视频/MiniMax H3 终极篇-文武双全_2110682294628474882.json, 视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json, 视频生成/图生视频/改至YZ金鱼-MiniMax H3 终极篇-文武双全_2111027801062203393.json, 视频生成/图生视频/自己用的_2110993734681841665.json, 视频生成/图生视频/自用YZ金鱼-MiniMax H3 终极篇-文武双全_2110932091864174593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3_家庭储能广告_15秒_三图参考_2110987996991410177.json、视频生成/图生视频/MiniMax H3 终极篇-文武双全_2110682294628474882.json、视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json、视频生成/图生视频/改至YZ金鱼-MiniMax H3 终极篇-文武双全_2111027801062203393.json、视频生成/图生视频/自己用的_2110993734681841665.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
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
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `GoohaiUniversalSlider` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `CM_FloatToInt` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `GetVideoComponents` —— 1/6 个有
- `LoadVideo` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `ShowAnything|Mie` —— 1/6 个有
- `T8SpeechReference` —— 1/6 个有
- `ZNGB_AudioConcatMulti` —— 1/6 个有
- `easy loraStack` —— 1/6 个有
- `easy loraStackApply` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
