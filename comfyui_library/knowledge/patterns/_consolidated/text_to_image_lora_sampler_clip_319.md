---
name: text_to_image_lora_sampler_clip_319
type: Text To Image
frequency: 7
level: strong
coverage: 0.861571
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json, 视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json, 视频生成/文生视频/多参考视频超级加速版｜minimaxH3文生图生视频_2092330253984296962.json, 视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json, 视频生成/文生视频/官方流优化版｜H3 文生视频 图生视频全能直出_2089335705678991361.json, 视频生成/文生视频/官方长视频工作流｜H3文生图生视频生成直出_2092731706536194050.json, 视频生成/文生视频/超级加速版多参考视频｜minimaxH3文生图生视频生视频_2092577712144732161.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_319

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json、视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json、视频生成/文生视频/多参考视频超级加速版｜minimaxH3文生图生视频_2092330253984296962.json、视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json、视频生成/文生视频/官方流优化版｜H3 文生视频 图生视频全能直出_2089335705678991361.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `ComfyMathExpression` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `ModelPreviewOverrideKJ` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `ManualSigmas` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `AudioAdjustVolume` —— 1/7 个有
- `EasyCache` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `MiniMaxH3AddGuide` —— 1/7 个有
- `MiniMaxH3Easy` —— 1/7 个有
- `MiniMaxH3EasyLoader` —— 1/7 个有
- `MiniMaxH3EasyOutput` —— 1/7 个有
- `VideoInfoLoaded` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
