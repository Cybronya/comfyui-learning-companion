---
name: text_to_image_lora_sampler_clip_387
type: Text To Image
frequency: 5
level: strong
coverage: 0.8678
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3全能图像编辑低显存故事板四视图处理工具_2102494252348563457.json, 图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json, 图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json, 图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json, 图片生成/图生图/minimax H3全能图像编辑｜低显存也能跑的图生图｜改图换景都拿手_2102235515952132097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_387

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MiniMax H3全能图像编辑低显存故事板四视图处理工具_2102494252348563457.json、图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json、图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json、图片生成/图生图/Qwen Image 2.1精准扩图｜按25%或300像素延展画布，一键扩展16_9_2104507613303107585.json、图片生成/图生图/minimax H3全能图像编辑｜低显存也能跑的图生图｜改图换景都拿手_2102235515952132097.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 3/5 个有
- `TextEncodeQwenImage21` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `MaskFillHoles` —— 2/5 个有
- `MiniMaxH3ReferenceToVideo` —— 2/5 个有
- `Text` —— 2/5 个有
- `ImpactSwitch` —— 1/5 个有
- `easy imageSizeByLongerSide` —— 1/5 个有
- `easy int` —— 1/5 个有
- `孤海外补画板按方向` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
