---
name: text_to_image_lora_sampler_clip_104
type: Text To Image
frequency: 10
level: strong
coverage: 0.6939
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Muter (rgthree), JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MINIMAX H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2106896826518560769.json, 图片生成/文生图/MINIMax H3短剧神器｜全功能加速文生图图生图_2106595105699360770.json, 视频生成/图生视频/H3 SelfLift参考生视频，双采单采加速任选模式_2110850789378977793.json, 视频生成/图生视频/MINIMAX_H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2108736968589926402.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采加单采参考生视频 视频生成加速_2109348613032861697.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采单采，参考生视频提速版_2110810539428499457.json, 视频生成/文生视频/H3全功能多重加速V2短剧神器 视频生成处理工具_2100689948386091009.json, 视频生成/文生视频/H3双采参考视频生成 文生视频图生视频多模态_2098274586579263490.json, 视频生成/文生视频/海螺H3全功能多重加速V2短剧神器｜minimax h3文生视频图生视频数字人通吃_2100444550102872066.json, 视频生成/文生视频/海螺H3全功能文生视频工作流h3多重加速V2短剧神器minimax_2087334573154856962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/MINIMAX H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2106896826518560769.json、图片生成/文生图/MINIMax H3短剧神器｜全功能加速文生图图生图_2106595105699360770.json、视频生成/图生视频/H3 SelfLift参考生视频，双采单采加速任选模式_2110850789378977793.json、视频生成/图生视频/MINIMAX_H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2108736968589926402.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采加单采参考生视频 视频生成加速_2109348613032861697.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 10 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
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
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `LoadAudio` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `Bookmark (rgthree)` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `GetNode` —— 6/10 个有
- `MiniMaxH3ImageToVideo` —— 6/10 个有
- `Mute / Bypass Relay (rgthree)` —— 6/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 6/10 个有
- `PlaySound|pysssss` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `SetReserveVRAM` —— 6/10 个有
- `easy int` —— 6/10 个有
- `BlockSparseAttention` —— 5/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `ExtendIntermediateSigmas` —— 4/10 个有
- `ManualSigmas` —— 4/10 个有
- `MiniMaxChunkFeedForward` —— 4/10 个有
- `MiniMaxLowVRAMAttention` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `SelfLiftH3Sampler` —— 4/10 个有
- `EasyCache` —— 3/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `ImageScale` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
