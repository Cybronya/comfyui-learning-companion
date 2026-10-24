---
name: unknown_workflow_lora_vae
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8348
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, RHLLMChatNode, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader, easy ifElse, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy seed, easy splitImages]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax 1080P 短剧创作Ⅰ（音频参考）- 8步极速生成_2084932680696815617.json, 视频生成/图生视频/MiniMax 1080P 短剧创作Ⅱ- 更新双采 - 质量更佳_2085049706593472514.json, 视频生成/图生视频/MiniMax 1080P 短剧创作Ⅲ（分镜）- 8步极速生成_2085089066273558530.json, 视频生成/图生视频/MiniMax 文_图_首尾_参考多合一 - 全球最夯视频剪辑导演台_2072179712750870529.json, 视频生成/文生视频/Minimax 最新简易单_双采全能 _ 3D潜空间放大 _ 自由切换_2087982435916148737.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_vae

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax 1080P 短剧创作Ⅰ（音频参考）- 8步极速生成_2084932680696815617.json、视频生成/图生视频/MiniMax 1080P 短剧创作Ⅱ- 更新双采 - 质量更佳_2085049706593472514.json、视频生成/图生视频/MiniMax 1080P 短剧创作Ⅲ（分镜）- 8步极速生成_2085089066273558530.json、视频生成/图生视频/MiniMax 文_图_首尾_参考多合一 - 全球最夯视频剪辑导演台_2072179712750870529.json、视频生成/文生视频/Minimax 最新简易单_双采全能 _ 3D潜空间放大 _ 自由切换_2087982435916148737.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `RHLLMChatNode`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy ifElse`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy seed`
- `easy splitImages`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `UniBlockSwap` —— 4/5 个有
- `easy blocker` —— 4/5 个有
- `BasicGuider` —— 3/5 个有
- `RandomNoise` —— 3/5 个有
- `SamplerCustomAdvanced` —— 3/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `KSamplerSelect` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `RHSettingsNode` —— 2/5 个有
- `SimpleMathDual+` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `LTXVConcatAVLatent` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/5 个有
- `MiniMaxH3HybridLoader` —— 1/5 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/5 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `StringContains` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy matchLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
