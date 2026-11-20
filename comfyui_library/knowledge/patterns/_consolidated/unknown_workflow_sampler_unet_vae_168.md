---
name: unknown_workflow_sampler_unet_vae_168
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.727125
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, KSamplerSelect, LoadImage, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/🎙原生对白一起生成｜MiniMax H3 V5.1 · Ref8 × SelfLift_2115813641588137986.json, 视频生成/图生视频/H3完整版-无LoRA-480P_2099176270763479041.json, 视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json, 视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json, 视频生成/图生视频/Minimax H3 最佳动作视频生成 Ref2V 工作流_2112874707992276993.json, 视频生成/图生视频/YZ金鱼-MiniMax H3-三图参考版_2117081149389500418.json, 视频生成/图生视频/【开源】MiniMax-H3 加速双采-self-lift_2099618432286281730.json, 视频生成/图生视频/（修脸极速）黑科技加速minimax h3 self-lift双采多参生视频_2098223404263497730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_168

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/🎙原生对白一起生成｜MiniMax H3 V5.1 · Ref8 × SelfLift_2115813641588137986.json、视频生成/图生视频/H3完整版-无LoRA-480P_2099176270763479041.json、视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json、视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json、视频生成/图生视频/Minimax H3 最佳动作视频生成 Ref2V 工作流_2112874707992276993.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `SaveVideo` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `H3SigmaRefiner` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `Text` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `BlockSparseAttention` —— 2/8 个有
- `LTXVSeparateAVLatent` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxH3AudioConditioningT8` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
