---
name: unknown_workflow_lora_unet_vae_9
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8408
common_nodes: [CLIPLoader, ImageResizeKJv2, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, RHLLMChatNode, SaveVideo, UNETLoader, UniBlockSwap, VAEDecode, VAEDecodeAudio, VAELoader, easy blocker, easy ifElse, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy seed, easy splitImages]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/MiniMax 动作参考（多参图+视频）- 8步极速生成_2084889766784495618.json, 视频生成/图生视频/MiniMax 1080P 短剧创作Ⅰ（音频参考）- 8步极速生成_2084932680696815617.json, 视频生成/图生视频/MiniMax 1080P 短剧创作Ⅲ（分镜）- 8步极速生成_2085089066273558530.json, 视频生成/图生视频/MiniMax 文_图_首尾_参考多合一 - 全球最夯视频剪辑导演台_2072179712750870529.json, 视频生成/图生视频/Minimax 30~60秒短片循环流_2085300016134057986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/MiniMax 动作参考（多参图+视频）- 8步极速生成_2084889766784495618.json、视频生成/图生视频/MiniMax 1080P 短剧创作Ⅰ（音频参考）- 8步极速生成_2084932680696815617.json、视频生成/图生视频/MiniMax 1080P 短剧创作Ⅲ（分镜）- 8步极速生成_2085089066273558530.json、视频生成/图生视频/MiniMax 文_图_首尾_参考多合一 - 全球最夯视频剪辑导演台_2072179712750870529.json、视频生成/图生视频/Minimax 30~60秒短片循环流_2085300016134057986.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `RHLLMChatNode`
- `SaveVideo`
- `UNETLoader`
- `UniBlockSwap`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy blocker`
- `easy ifElse`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy seed`
- `easy splitImages`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `KSampler` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `BasicGuider` —— 2/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/5 个有
- `RandomNoise` —— 2/5 个有
- `SamplerCustomAdvanced` —— 2/5 个有
- `easy saveVideo` —— 2/5 个有
- `DA3Inference` —— 1/5 个有
- `DA3Render` —— 1/5 个有
- `GetVideoComponents` —— 1/5 个有
- `LoadDA3Model` —— 1/5 个有
- `StringContains` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy mergeVideosFromPaths` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
