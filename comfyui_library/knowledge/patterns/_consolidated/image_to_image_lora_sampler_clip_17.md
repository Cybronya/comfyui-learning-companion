---
name: image_to_image_lora_sampler_clip_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.612
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Draw Shape, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1965378348828475394.json, 图片生成/文生图/1982996678984773634.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1965378348828475394.json、图片生成/文生图/1982996678984773634.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Draw Shape` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `NineGridMosaicNode` —— 1/2 个有
- `NunchakuQwenImageDiTLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `SeargePromptCombiner` —— 1/2 个有
- `SeargePromptText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Draw Shape、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
