---
name: image_to_image_lora_sampler_unet_5
type: Image To Image
frequency: 9
level: strong
coverage: 0.931222
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json, 视频生成/图生视频/1979088227527200769.json, 视频生成/图生视频/1989475956505104385.json, 视频生成/图生视频/1987684744014049282.json, 视频生成/图生视频/1987671585945489409.json, 视频生成/图生视频/1987680109538816002.json, 视频生成/图生视频/1987680874936381442.json, 视频生成/图生视频/1987676437924745217.json, 视频生成/文生视频/一句话生成和小时候的自己对话_1987677418305556481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json、视频生成/图生视频/1979088227527200769.json、视频生成/图生视频/1989475956505104385.json、视频生成/图生视频/1987684744014049282.json、视频生成/图生视频/1987671585945489409.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 8/9 个有
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `EmptySD3LatentImage` —— 7/9 个有
- `RH_Sora2_I2V` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `SaveImage` —— 6/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `CR Text` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 9 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
