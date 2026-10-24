---
name: image_to_image_lora_sampler_clip_45
type: Image To Image
frequency: 6
level: weak
coverage: 0.977667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json, 图片生成/图生图/LABUBU图生图_1936650163987337217.json, 图片生成/图生图/Qwen-Image图生图3D孙悟空_1954028272784953345.json, 图片生成/图生图/Qwen-Image图生图_1953321268298874882.json, 图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json, 图片生成/图生图/动漫真人转CG风格_2074082230468694017.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json、图片生成/图生图/LABUBU图生图_1936650163987337217.json、图片生成/图生图/Qwen-Image图生图3D孙悟空_1954028272784953345.json、图片生成/图生图/Qwen-Image图生图_1953321268298874882.json、图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `WD14Tagger|pysssss` —— 3/6 个有
- `ClipInterrogator` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `StringConcatenate` —— 2/6 个有
- `DualCLIPLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 34% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.9 | 0.6 - 1 | 6 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.6 - 1，6 个样本
