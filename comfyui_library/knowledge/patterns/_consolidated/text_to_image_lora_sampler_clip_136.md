---
name: text_to_image_lora_sampler_clip_136
type: Text To Image
frequency: 7
level: strong
coverage: 0.873
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveFloat, RHLLMChatNode, RHSettingsNode, RandomNoise, SamplerCustomAdvanced, SaveVideo, SimpleMathDual+, UNETLoader, UniBlockSwap, VAEDecode, VAEDecodeAudio, VAELoader, easy blocker, easy ifElse, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy seed, easy splitImages, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1080P短剧创作更新双采｜MiniMax质量更佳图生视频_2091305280138211329.json, 视频生成/图生视频/1080P短剧创作更新双采｜MiniMax质量更佳图生视频_2091883064552148994.json, 视频生成/图生视频/MiniMax 短剧创作导演台_1080P 双采图生视频_2089609241664507906.json, 视频生成/图生视频/MiniMax短剧创作导演台1080P双采｜图生视频高清生成_2090458408708296706.json, 视频生成/图生视频/导演台短剧创作｜MiniMax 1080P双采图生视频_2090186981660782594.json, 视频生成/图生视频/短剧创作Ⅱ双采更新｜MiniMax 1080P质量更佳图生视频_2090213941472481281.json, 视频生成/图生视频/短剧创作Ⅱ导演台｜MiniMax 1080P双采图生视频质量升级_2089037699893260289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1080P短剧创作更新双采｜MiniMax质量更佳图生视频_2091305280138211329.json、视频生成/图生视频/1080P短剧创作更新双采｜MiniMax质量更佳图生视频_2091883064552148994.json、视频生成/图生视频/MiniMax 短剧创作导演台_1080P 双采图生视频_2089609241664507906.json、视频生成/图生视频/MiniMax短剧创作导演台1080P双采｜图生视频高清生成_2090458408708296706.json、视频生成/图生视频/导演台短剧创作｜MiniMax 1080P双采图生视频_2090186981660782594.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `RHSettingsNode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleMathDual+`
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/7 个有
- `PT_H3ConcatAVLatent` —— 5/7 个有
- `VAEEncode` —— 5/7 个有
- `VAEEncodeAudio` —— 5/7 个有
- `BasicScheduler` —— 4/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `ExtendIntermediateSigmas` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `ManualSigmas` —— 3/7 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
