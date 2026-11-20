---
name: image_to_image_lora_sampler_clip_40
type: Image To Image
frequency: 8
level: weak
coverage: 0.967625
common_nodes: [CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json, 图片生成/图生图/LABUBU图生图_1936650163987337217.json, 图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json, 图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json, 图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json, 图片生成/图生图/Z-image-base-极速洗图_2021931573834158081.json, 图片生成/图生图/anima edit 2秒（提示词待优化）_2061288008342663170.json, 图片生成/图生图/动漫真人转CG风格_2074082230468694017.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json、图片生成/图生图/LABUBU图生图_1936650163987337217.json、图片生成/图生图/Magic-Wan2.2-V2洗图工作流_1994768271901700098.json、图片生成/图生图/Magic-Wan2.2-洗图工作流_1995468058045112322.json、图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `WD14Tagger|pysssss` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `StringConcatenate` —— 2/8 个有
- `ApplyCosmosReferenceLatent` —— 1/8 个有
- `DualCLIPLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 30 | 8 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 37% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 0.6 | 0.23 - 1 | 8 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 30，8 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 0.6，观测区间 0.23 - 1，8 个样本
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
