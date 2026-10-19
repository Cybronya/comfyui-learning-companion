---
name: text_to_image_sampler_clip_unet_4
type: Text To Image
frequency: 10
level: weak
coverage: 0.9787
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1953718095699431426.json, 图片生成/文生图/1953804613029908482.json, 图片生成/文生图/1953818850963935234.json, 图片生成/文生图/1953997948080279554.json, 图片生成/文生图/1954438175747928065.json, 图片生成/文生图/1955652380474818561.json, 图片生成/文生图/1956201968337342466.json, 图片生成/文生图/1962088539834007553.json, 图片生成/文生图/1973965175168569346.json, 图片生成/文生图/1974013476374974466.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1953718095699431426.json、图片生成/文生图/1953804613029908482.json、图片生成/文生图/1953818850963935234.json、图片生成/文生图/1953997948080279554.json、图片生成/文生图/1954438175747928065.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 8/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `Anything Everywhere3` —— 2/10 个有
- `DualCLIPLoader` —— 2/10 个有
- `FluxGuidance` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `QwenEditResolution` —— 2/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `NunchakuQwenImageDiTLoader` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `RH_Prompter` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `VAEEncode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 4 - 25 | 10 | 47% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 10 | 10 | 4% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.2 - 1 | 10 | 74% |
| 宽度 | 1024 | 768 - 1328 | 10 | 85% |
| 高度 | 1136 | 1024 - 1536 | 10 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 4 - 25，10 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 10，10 个样本，取值分散，一致性仅 4%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，10 个样本
- 宽度 中位数 1024，观测区间 768 - 1328，10 个样本，取值集中（一致性 85%）
- 高度 中位数 1136，观测区间 1024 - 1536，10 个样本，取值集中（一致性 82%）
