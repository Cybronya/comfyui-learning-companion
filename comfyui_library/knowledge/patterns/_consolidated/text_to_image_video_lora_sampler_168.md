---
name: text_to_image_video_lora_sampler_168
type: Text To Image
frequency: 4
level: strong
coverage: 0.8695
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, RHLLMChatNode, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/双人完美数字人｜MiniMaxH3人物特效图生视频_2090208010038767617.json, 视频生成/图生视频/完美数字人模特产品展示｜MiniMaxH3图生视频数字人工作流_2087203587905638401.json, 视频生成/图生视频/自然循环动态壁纸v2｜MiniMax H3人物特效图生视频_2092874835826401281.json, 视频生成/图生视频/自然循环动态壁纸v2｜MiniMax H3图生视频生成_2092686110370648065.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/双人完美数字人｜MiniMaxH3人物特效图生视频_2090208010038767617.json、视频生成/图生视频/完美数字人模特产品展示｜MiniMaxH3图生视频数字人工作流_2087203587905638401.json、视频生成/图生视频/自然循环动态壁纸v2｜MiniMax H3人物特效图生视频_2092874835826401281.json、视频生成/图生视频/自然循环动态壁纸v2｜MiniMax H3图生视频生成_2092686110370648065.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `RHLLMChatNode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `JWFloat` —— 2/4 个有
- `LazySwitch1way` —— 2/4 个有
- `LazySwitch2way` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `StringToInt` —— 2/4 个有
- `ttN concat` —— 2/4 个有

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
