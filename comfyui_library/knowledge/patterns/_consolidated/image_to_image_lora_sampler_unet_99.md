---
name: image_to_image_lora_sampler_unet_99
type: Image To Image
frequency: 8
level: strong
coverage: 0.9305
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-2509-人物镜头多角度展示_1995104571196366850.json, 图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json, 图片生成/图生图/Qwen-image-2511-人物镜头多角度展示_2006023840396218370.json, 图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（人物固定版）_2021135812963864577.json, 图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（脸部跟随版）_2015620861742555138.json, 图片生成/图生图/ygd生图-多图生成多角度-QwenEdit_1988117156808269826.json, 图片生成/图生图/工作流系列10-物品多视角工作流-基于QWEN-EDIT-2511_2056559560298684417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_99

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2509-人物镜头多角度展示_1995104571196366850.json、图片生成/图生图/Qwen-image-2511-Multiple-Angles-LoRA_2013960041979715586.json、图片生成/图生图/Qwen-image-2511-人物镜头多角度展示_2006023840396218370.json、图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json、图片生成/图生图/WH-AI-Studio-千问2511-一键人物镜头多角度展示（人物固定版）_2021135812963864577.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `easy promptLine` —— 7/8 个有
- `Text Multiline` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 5/8 个有
- `AddLabel` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `ImageAndMaskPreview` —— 1/8 个有
- `Int` —— 1/8 个有
- `QwenMultiangleCameraNode` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 8 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
