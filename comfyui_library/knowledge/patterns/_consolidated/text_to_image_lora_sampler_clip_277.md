---
name: text_to_image_lora_sampler_clip_277
type: Text To Image
frequency: 8
level: strong
coverage: 0.863125
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3超级长视频1-10顺序生成 自动合并输出_2098819352618426369.json, 视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3视频生成直出_2092021354127253506.json, 视频生成/文生视频/全模态多参考视频生成｜MiniMax H3时间线控制+独立音频_2091205063564943362.json, 视频生成/文生视频/六段式自动生成自动校验MiniMax H3 Ref2VA剧本直出9图参考成片原生音画同步_2088355373936893954.json, 视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json, 视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json, 视频生成/文生视频/官方流优化版｜H3 文生视频 图生视频全能直出_2089335705678991361.json, 视频生成/文生视频/官方长视频工作流｜H3文生图生视频生成直出_2092731706536194050.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_277

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3超级长视频1-10顺序生成 自动合并输出_2098819352618426369.json、视频生成/文生视频/全模态多参考视频生成器｜MiniMax H3视频生成直出_2092021354127253506.json、视频生成/文生视频/全模态多参考视频生成｜MiniMax H3时间线控制+独立音频_2091205063564943362.json、视频生成/文生视频/六段式自动生成自动校验MiniMax H3 Ref2VA剧本直出9图参考成片原生音画同步_2088355373936893954.json、视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `BasicScheduler` —— 6/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `ManualSigmas` —— 2/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `AudioConcatenate` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageBatch` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3BlockCacheT8` —— 1/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VRAM_Debug` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

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
