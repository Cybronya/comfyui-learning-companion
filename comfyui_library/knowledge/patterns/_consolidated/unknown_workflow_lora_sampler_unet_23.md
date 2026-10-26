---
name: unknown_workflow_lora_sampler_unet_23
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.873579
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json, 视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json, 视频生成/图生视频/Minimax-H3-多参Singularity-V2版_2113596965647896577.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json, 视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json, 视频生成/图生视频/Minimax-h3-多参视频生成（不油、不偏色及一致性好）_2107461072583221250.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2099777362543075329.json, 视频生成/图生视频/Minimax_H3-加速双采-self-lift工作流_2100037395591815170.json, 视频生成/图生视频/minimax-H3超写实颜值赛道起号神器_2113569756015054850.json, 视频生成/图生视频/minimax-H3超写实颜值赛道起号神器_2113599325896003585.json, 视频生成/图生视频/【开源】MiniMax-H3 加速双采-self-lift_2099618432286281730.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100021900394192897.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2100184323868680193.json, 视频生成/图生视频/全能参考加速双采-self-lift工作流_2101869698915856385.json, 视频生成/图生视频/参考图生视频｜Self-Lift 双采·5秒预检_2098678648126664705.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2100028907868213250.json, 视频生成/图生视频/整合音频修复的双采-self-lift工作流_2101556853078585345.json, 视频生成/图生视频/黑科技加速双采-self-lift工作流_2099386693676785665.json, 视频生成/图生视频/黑科技加速双采-self-lift高动态_2102398843047469057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/Minimax H3-360度视频生成_2108541709025112066.json、视频生成/图生视频/Minimax H3-加速双采-self-lift工作流_2097544900240822273.json、视频生成/图生视频/Minimax-H3-多参Singularity-V2版_2113596965647896577.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097641972067557378.json、视频生成/图生视频/Minimax-H3开源 黑科技加速双采-self-lift图生视频_2097665516235223042.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 18/19 个有
- `H3SigmaRefiner` —— 17/19 个有
- `MiniMaxChunkFeedForward` —— 17/19 个有
- `ModelPreviewOverrideKJ` —— 17/19 个有
- `PrimitiveStringMultiline` —— 16/19 个有
- `VHS_VideoCombine` —— 16/19 个有
- `MiniMaxLowVRAMAttention` —— 15/19 个有
- `CreateVideo` —— 14/19 个有
- `LoadAudio` —— 4/19 个有
- `BlockSparseAttention` —— 3/19 个有
- `PreviewImage` —— 3/19 个有
- `SaveVideo` —— 3/19 个有
- `EmptyImage` —— 2/19 个有
- `LoraLoaderBypassModelOnly` —— 2/19 个有
- `MiniMaxH3AudioConditioningT8` —— 2/19 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/19 个有
- `MiniMaxH3SigmaShift` —— 2/19 个有
- `StringFormat` —— 2/19 个有
- `Text` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `CR Prompt Text` —— 1/19 个有
- `MiniMaxH3ImageToVideo` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
