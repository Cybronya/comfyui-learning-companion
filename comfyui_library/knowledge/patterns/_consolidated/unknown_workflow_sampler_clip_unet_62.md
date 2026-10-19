---
name: unknown_workflow_sampler_clip_unet_62
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8785
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [StringFunction|pysssss, ttN concat, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1912174132275150850.json, 图片生成/文生图/1913620524503891969.json, 图片生成/文生图/1920133263510142977.json, 图片生成/文生图/1967227108663627778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1912174132275150850.json、图片生成/文生图/1913620524503891969.json、图片生成/文生图/1920133263510142977.json、图片生成/文生图/1967227108663627778.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 3/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `Joy_caption` —— 2/4 个有
- `Joy_caption_load` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Bjornulf_FreeVRAM` —— 1/4 个有
- `Bjornulf_ShowStringText` —— 1/4 个有
- `EG_FX_BDAPI` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 924 | - | 2 | 83% |
| 高度 | 1472 | - | 2 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 924，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、ttN concat、LayerUtility: ImageScaleByAspectRatio V2
