---
name: image_to_image_lora_sampler_unet_106
type: Image To Image
frequency: 6
level: strong
coverage: 0.9495
common_nodes: [CFGNorm, CLIPLoader, CR Text, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/XX2256_1989184998232174594.json, 图片生成/图生图/qwen2511一键换衣千问图像编辑换装_2060331107287134210.json, 图片生成/图生图/一键完美图片去水印TextEncode QwenlmageEdit2511_1988876685514772482.json, 图片生成/图生图/一键换衣千问qwen2511最新图像编辑换装千问2511_2034603108478754818.json, 图片生成/图生图/一键换装工作流，无需遮罩_2096447517775978497.json, 图片生成/图生图/人物换发型_2037156801669505026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_106

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/XX2256_1989184998232174594.json、图片生成/图生图/qwen2511一键换衣千问图像编辑换装_2060331107287134210.json、图片生成/图生图/一键完美图片去水印TextEncode QwenlmageEdit2511_1988876685514772482.json、图片生成/图生图/一键换衣千问qwen2511最新图像编辑换装千问2511_2034603108478754818.json、图片生成/图生图/一键换装工作流，无需遮罩_2096447517775978497.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ImageScaleToTotalPixels`
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
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `ImageConcanate` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `FillMaskedArea_UTK` —— 1/6 个有
- `GrowMask` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Prompts Everywhere` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 2480 | - | 1 | 100% |
| 采样步数 | 4 | 4 - 8 | 6 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
