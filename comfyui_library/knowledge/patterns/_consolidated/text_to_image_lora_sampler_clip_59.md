---
name: text_to_image_lora_sampler_clip_59
type: Text To Image
frequency: 14
level: strong
coverage: 0.709
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2106873837555113985.json, 视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2109810746019373058.json, 视频生成/图生视频/Minimax图生视频I2V工作流，图生视频官方图生视频处理工具_2107908610960486402.json, 视频生成/图生视频/Minimax图生视频I2V方案，图生视频高效直出_2111192151311872002.json, 视频生成/图生视频/Minimax图生视频I2V方案｜图片动起来就这么简单_2107697471907516418.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2106851933465169922.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2110209158552317953.json, 视频生成/图生视频/Minimax多参考生视频R2V，9张参考图3段视频方案_2110867933206503425.json, 视频生成/图生视频/Minmax R2V参考生视频｜多图参考图生视频一键出片｜视频创作利器_2102208736826847234.json, 视频生成/图生视频/Minmax多参考生成视频R2V 多模态输入视频生成方案_2108651204296400897.json, 视频生成/图生视频/Minmax多参考生视频R2V，视频生视频多图精准控制_2111190495966883841.json, 视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json, 视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json, 视频生成/文生视频/Minimax文生视频T2V工作流，文生视频官方文生视频处理工具_2107930345889943553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2106873837555113985.json、视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2109810746019373058.json、视频生成/图生视频/Minimax图生视频I2V工作流，图生视频官方图生视频处理工具_2107908610960486402.json、视频生成/图生视频/Minimax图生视频I2V方案，图生视频高效直出_2111192151311872002.json、视频生成/图生视频/Minimax图生视频I2V方案｜图片动起来就这么简单_2107697471907516418.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
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
- `LoadAudio` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `孤海注释` —— 12/14 个有
- `SaveImage` —— 11/14 个有
- `AudioCrop` —— 8/14 个有
- `MiniMaxH3ReferenceToVideo` —— 8/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `MiniMaxH3ImageToVideo` —— 6/14 个有
- `VHS_LoadVideo` —— 6/14 个有
- `easy minimaxH3AudioLock` —— 6/14 个有
- `GetImageSize` —— 5/14 个有
- `ImageScaleToTotalPixels` —— 5/14 个有
- `EmptyImage` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `MiniMaxH3AudioLock` —— 2/14 个有
- `MiniMaxH3SaveLatent` —— 2/14 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/14 个有
- `ModelAttentionBackend` —— 1/14 个有
- `XB_ReferenceAny` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
