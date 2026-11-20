---
name: image_to_image_lora_sampler_unet_164
type: Image To Image
frequency: 5
level: weak
coverage: 0.8126
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Edit 2509 (文改图 PLus版）_1979253121035702273.json, 平台全量/Qwen-Edit _ 优化光影_1890300468151853058.json, 平台全量/Qwen_edit最强人物迁移（换脸+姿势+场景）_1990260420713828353.json, 平台全量/Qwen优化光影_1988183543337631746.json, 平台全量/换装-Qwen2509_1983806458766761985.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_164

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-Edit 2509 (文改图 PLus版）_1979253121035702273.json、平台全量/Qwen-Edit _ 优化光影_1890300468151853058.json、平台全量/Qwen_edit最强人物迁移（换脸+姿势+场景）_1990260420713828353.json、平台全量/Qwen优化光影_1988183543337631746.json、平台全量/换装-Qwen2509_1983806458766761985.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LatentUpscaleBy` —— 2/5 个有
- `CR Seed` —— 1/5 个有
- `CR Upscale Image` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 5 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.55 - 1 | 5 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，5 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
