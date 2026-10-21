---
name: unknown_workflow_lora_sampler_unet_6
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.803692
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json, 视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json, 视频生成/图生视频/【开源】MiniMax-H3 加速双采-self-lift_2099618432286281730.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100021900394192897.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100184323868680193.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2101869698915856385.json, 视频生成/图生视频/参考图生视频｜Self-Lift 双采·5秒预检_2098678648126664705.json, 视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2100028907868213250.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2101556853078585345.json, 视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json, 视频生成/文生视频/MiniMax H3｜TaoMate 3步加速 lora_2099873466462855169.json, 视频生成/文生视频/Minimax H3 加速双采 Self-Lift 工作流_2099332965401710594.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_6

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2101858620555223042.json、视频生成/图生视频/MiniMax_H3｜TaoMate_3步加速_lora_2102674471441227777.json、视频生成/图生视频/【开源】MiniMax-H3 加速双采-self-lift_2099618432286281730.json、视频生成/图生视频/全能参考加速双采-self-lift工作流_2100021900394192897.json、视频生成/图生视频/全能参考加速双采-self-lift工作流_2100184323868680193.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/13 个有
- `CreateVideo` —— 11/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `SelfLiftH3Sampler` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 10/13 个有
- `ModelPreviewOverrideKJ` —— 10/13 个有
- `LoadAudio` —— 9/13 个有
- `MiniMaxChunkFeedForward` —— 9/13 个有
- `MiniMaxLowVRAMAttention` —— 9/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `H3SigmaRefiner` —— 8/13 个有
- `LTXVSeparateAVLatent` —— 5/13 个有
- `MiniMaxH3AudioConditioningT8` —— 5/13 个有
- `SaveVideo` —— 4/13 个有
- `LoraLoader` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `JWStringToFloat` —— 2/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `SelfLiftAvatarH3Sampler` —— 2/13 个有
- `Text` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | 0.75 - 0.75 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
