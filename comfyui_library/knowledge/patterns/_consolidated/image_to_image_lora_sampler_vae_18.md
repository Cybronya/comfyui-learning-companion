---
name: image_to_image_lora_sampler_vae_18
type: Image To Image
frequency: 5
level: strong
coverage: 0.8268
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json, 图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json, 图片生成/图生图/多图万能处理（QWEN EDIT 2511）_2015346327189725186.json, 图片生成/图生图/工作流系列10-物品多视角工作流-基于QWEN-EDIT-2511_2056559560298684417.json, 图片生成/文生图/一键多角度+全节点注释_2056923210242936834.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物多角度一键生成《Next Scene》_1984265817120522242.json、图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json、图片生成/图生图/多图万能处理（QWEN EDIT 2511）_2015346327189725186.json、图片生成/图生图/工作流系列10-物品多视角工作流-基于QWEN-EDIT-2511_2056559560298684417.json、图片生成/文生图/一键多角度+全节点注释_2056923210242936834.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/5 个有
- `Int` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
