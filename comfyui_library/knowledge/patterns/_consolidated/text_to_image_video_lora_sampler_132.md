---
name: text_to_image_video_lora_sampler_132
type: Text To Image
frequency: 5
level: strong
coverage: 0.5662
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2110451947428995074.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频直出_2093456500986568705.json, 视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json, 视频生成/文生视频/官方全能参考版单采｜文生视频视频生视频图生视频｜三模式任选_2104778746879369218.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2110451947428995074.json、视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json、视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频直出_2093456500986568705.json、视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json、视频生成/文生视频/官方全能参考版单采｜文生视频视频生视频图生视频｜三模式任选_2104778746879369218.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `MiniMaxH3SigmaShift` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `ModelPreviewOverrideKJ` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `Text` —— 2/5 个有
- `AudioSeparation` —— 1/5 个有
- `CR Value` —— 1/5 个有
- `Float` —— 1/5 个有
- `JWImageResizeToMegapixels` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `SplitSigmas` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `ViggleAnimateConditioning` —— 1/5 个有
- `ViggleTextCondLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
