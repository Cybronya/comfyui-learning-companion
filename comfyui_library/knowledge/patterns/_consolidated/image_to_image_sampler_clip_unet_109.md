---
name: image_to_image_sampler_clip_unet_109
type: Image To Image
frequency: 6
level: weak
coverage: 0.950333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Anima局部重绘_2061066117896036353.json, 平台全量/Anima简单重绘工作流_2062525112309608449.json, 平台全量/Flux Klein 白模建筑参考图渲染_2029788958317617154.json, 平台全量/Flux2-Klein  图片编辑(多图)_2060281624557871106.json, 平台全量/Flux2-Klein-图片编辑 (多图)_2057752273941516289.json, 平台全量/场景精修_2073405921899933698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Anima局部重绘_2061066117896036353.json、平台全量/Anima简单重绘工作流_2062525112309608449.json、平台全量/Flux Klein 白模建筑参考图渲染_2029788958317617154.json、平台全量/Flux2-Klein  图片编辑(多图)_2060281624557871106.json、平台全量/Flux2-Klein-图片编辑 (多图)_2057752273941516289.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `ReferenceLatent` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `AnimaLLLiteApply` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `SetLatentNoiseMask` —— 2/6 个有
- `ConditioningCombine` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 30 | 6 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 29% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 30，6 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
