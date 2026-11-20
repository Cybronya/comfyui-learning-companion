---
name: text_to_image_lora_sampler_clip_580
type: Text To Image
frequency: 3
level: strong
coverage: 0.664
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, EmptyLatentImage, GetNode, H3AutoContextSampler, H3Parameter, H3SeamCorrection, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, ResolutionSelector, SaveImage, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 AutoContext无限时长视频单采直出处理工具_2101723121383460866.json, 视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大1080P直出工具_2101721113498841089.json, 视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大武戏1080P直出工具_2101719041944674305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_580

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 AutoContext无限时长视频单采直出处理工具_2101723121383460866.json、视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大1080P直出工具_2101721113498841089.json、视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大武戏1080P直出工具_2101719041944674305.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateVideo`
- `EmptyLatentImage`
- `GetNode`
- `H3AutoContextSampler`
- `H3Parameter`
- `H3SeamCorrection`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxLowVRAMAttention`
- `ResolutionSelector`
- `SaveImage`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `H3SigmaRefiner` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `SolAttnPatch` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
