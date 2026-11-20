---
name: image_to_image_lora_sampler_unet_141
type: Image To Image
frequency: 5
level: weak
coverage: 0.9654
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/建筑立面迁移_泛化 qwen_image_edit_2511_2010382464266543105.json, 图片生成/图生图/替换物品，人物，让人物穿上你想要的衣服，鞋子_1998034291772784642.json, 图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json, 图片生成/图生图/电商模特三视图_qwen_image_edit_2509_Jefsky_1976877911221456897.json, 图片生成/图生图/自由打光QwenImageEdit2511_1995384002708168706.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/建筑立面迁移_泛化 qwen_image_edit_2511_2010382464266543105.json、图片生成/图生图/替换物品，人物，让人物穿上你想要的衣服，鞋子_1998034291772784642.json、图片生成/图生图/橘-qwen edit 2509 多图编辑基础流_2003471485438181377.json、图片生成/图生图/电商模特三视图_qwen_image_edit_2509_Jefsky_1976877911221456897.json、图片生成/图生图/自由打光QwenImageEdit2511_1995384002708168706.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `AIO_Preprocessor` —— 2/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `ControlNetLoader` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `SetUnionControlNetType` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `ImitationHueNode` —— 1/5 个有
- `PIP_StringConcatenation` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `QwenMultiangleLightningNode` —— 1/5 个有
- `easy bookmark` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 5 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 37% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.4 | - | 2 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，5 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.4，样本不足，未给区间，2 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
