---
name: image_to_image_lora_sampler_unet_8
type: Image To Image
frequency: 4
level: strong
coverage: 0.54
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, PlaySound|pysssss, easy promptLine]
members: [图片生成/图生图/2011744883106648065.json, 图片生成/图生图/2056630627348336641.json, 图片生成/图生图/2067296922406313986.json, 图片生成/图生图/2090830266335055873.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2011744883106648065.json、图片生成/图生图/2056630627348336641.json、图片生成/图生图/2067296922406313986.json、图片生成/图生图/2090830266335055873.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `Text` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、PlaySound|pysssss、easy promptLine
