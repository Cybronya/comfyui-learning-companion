---
name: text_to_image_lora_sampler_clip_511
type: Text To Image
frequency: 3
level: strong
coverage: 0.778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, MuyeTextEditOutput, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS文生图+全节点注释_2112471507770372097.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json, 图片生成/文生图/（文生图 电商海报挺好 文字清晰）MOSS image 最强开源文生图｜开源生图的黑马_2112088005384167425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_511

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/MOSS文生图+全节点注释_2112471507770372097.json、图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json、图片生成/文生图/（文生图 电商海报挺好 文字清晰）MOSS image 最强开源文生图｜开源生图的黑马_2112088005384167425.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1200 | 3 | 92% |
| 高度 | 1024 | 1024 - 1600 | 3 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1200，3 个样本，取值集中（一致性 92%）
- 高度 中位数 1024，观测区间 1024 - 1600，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
