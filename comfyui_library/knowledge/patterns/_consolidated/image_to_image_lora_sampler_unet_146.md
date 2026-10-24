---
name: image_to_image_lora_sampler_unet_146
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9045
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Put It Here v1 Qwen Edit万物融图_1965935009678954497.json, 图片生成/图生图/Put It Here v1 Qwen Edit融图_1994337831405502465.json, 图片生成/图生图/Qwen Edit图像融合_1966514470820458497.json, 图片生成/图生图/Qwen2512洗图&批量获取不同比例图_2054158368167743489.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Put It Here v1 Qwen Edit万物融图_1965935009678954497.json、图片生成/图生图/Put It Here v1 Qwen Edit融图_1994337831405502465.json、图片生成/图生图/Qwen Edit图像融合_1966514470820458497.json、图片生成/图生图/Qwen2512洗图&批量获取不同比例图_2054158368167743489.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FastCanvas` —— 3/4 个有
- `FastCanvasTool` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `TextEncodeQwenImageEditEnhanced` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `QwenImageLatentAspectRatio` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 15 | 4 | 69% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 4 | 69% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 15，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
