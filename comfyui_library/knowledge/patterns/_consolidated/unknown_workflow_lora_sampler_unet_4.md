---
name: unknown_workflow_lora_sampler_unet_4
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.846938
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json, 视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json, 视频生成/图生视频/Minimax-h3-多参视频生成（不油、不偏色及一致性好）_2107461072583221250.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2099777362543075329.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2100037395591815170.json, 视频生成/图生视频/【开源】MiniMax-H3 加速双采-self-lift_2099618432286281730.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100021900394192897.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100184323868680193.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2101869698915856385.json, 视频生成/图生视频/参考图生视频｜Self-Lift 双采·5秒预检_2098678648126664705.json, 视频生成/图生视频/常规万能流直出1080p 最高质量版 -MMH3 Selflift_2103534009916674049.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2100028907868213250.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2101556853078585345.json, 视频生成/图生视频/短剧制作 直出1080p 最高质量版 -MMH3 Selflift_2106389437042221057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json、视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json、视频生成/图生视频/Minimax-h3-多参视频生成（不油、不偏色及一致性好）_2107461072583221250.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 15/16 个有
- `MiniMaxH3ReferenceToVideo` —— 15/16 个有
- `MiniMaxLowVRAMAttention` —— 15/16 个有
- `H3SigmaRefiner` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `PrimitiveStringMultiline` —— 14/16 个有
- `SelfLiftH3Sampler` —— 14/16 个有
- `VHS_VideoCombine` —— 13/16 个有
- `CreateVideo` —— 12/16 个有
- `LoadAudio` —— 5/16 个有
- `PreviewImage` —— 3/16 个有
- `SaveVideo` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `JWStringToFloat` —— 2/16 个有
- `LTXVSeparateAVLatent` —— 2/16 个有
- `MiniMaxH3AudioConditioningT8` —— 2/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/16 个有
- `PreviewAny` —— 2/16 个有
- `SelfLiftAvatarH3Sampler` —— 2/16 个有
- `MiniMaxH3ImageToVideo` —— 1/16 个有
- `Text` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
