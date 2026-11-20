---
name: text_to_image_lora_sampler_clip_516
type: Text To Image
frequency: 4
level: strong
coverage: 0.91225
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/解码二采放大｜minimaxh3视频超分图生视频_2091181557297016833.json, 视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json, 视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json, 视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_516

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/解码二采放大｜minimaxh3视频超分图生视频_2091181557297016833.json、视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json、视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json、视频生成/文生视频/minmaxH3单采加速｜文生视频图生视频 极速出片小钢炮_2105529286273880065.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ExtendIntermediateSigmas` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MiniMaxH3SigmaShift` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `FlashVSRNode` —— 1/4 个有
- `FlashVSR_SM_KSampler` —— 1/4 个有
- `FlashVSR_SM_Model` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `LTXVConcatAVLatent` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `VAEEncodeAudio` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
