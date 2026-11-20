---
name: text_to_image_lora_sampler_clip_277
type: Text To Image
frequency: 8
level: strong
coverage: 0.8965
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2106875364315324417.json, 视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2109447261494272002.json, 视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3一键直出_2090902980487892993.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3文生图生视频_2092019899022528514.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3视频生成直出_2092021354127253506.json, 视频生成/文生视频/全模态多参考视频生成｜MiniMax H3时间线控制+独立音频_2091205063564943362.json, 视频生成/文生视频/量化加速参考生视频｜MiniMaxH3 文本图像音视频全参考_2089345982659121153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_277

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2106875364315324417.json、视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2109447261494272002.json、视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json、视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3一键直出_2090902980487892993.json、视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3文生图生视频_2092019899022528514.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `GetVideoComponents` —— 4/8 个有
- `LoadVideo` —— 4/8 个有
- `SaveImage` —— 3/8 个有
- `BlockSparseAttention` —— 2/8 个有
- `MiniMaxH3MotionContext` —— 2/8 个有
- `MiniMaxH3MotionContextChain` —— 2/8 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/8 个有
- `MiniMaxH3MotionContextSaveLatent` —— 2/8 个有
- `MiniMaxH3MotionContextTrim` —— 2/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `ViggleAnimateConditioningWindowed` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `PreviewImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
