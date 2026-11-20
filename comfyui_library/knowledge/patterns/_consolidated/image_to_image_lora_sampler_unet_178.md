---
name: image_to_image_lora_sampler_unet_178
type: Image To Image
frequency: 3
level: strong
coverage: 0.856
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 Identity Edit V1 图像编辑工作流_2075210429613297666.json, 图片生成/图生图/Krea2 一键全能动态角色设计表_2090405298501677057.json, 图片生成/图生图/Krea2_Ostris_Edit_outfit_2081442410726514690.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_178

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2 Identity Edit V1 图像编辑工作流_2075210429613297666.json、图片生成/图生图/Krea2 一键全能动态角色设计表_2090405298501677057.json、图片生成/图生图/Krea2_Ostris_Edit_outfit_2081442410726514690.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `ComfyUI-Krea2T-Enhancer` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Krea2OstrisEditModelPatch` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `StringReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
