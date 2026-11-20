---
name: unknown_workflow_lora_sampler_unet_59
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8901
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen视角控制_2055330832017043457.json, 图片生成/图生图/▶Qwen Edit 2511多角度视角控制_2086719564179656705.json, 图片生成/图生图/一键换装，电商福音，复杂场景超高一致性_2054931613225635841.json, 图片生成/图生图/一键换装，电商福音，复杂场景超高一致性_2055107672713768961.json, 图片生成/图生图/一键换装：完美替换衣物，超高一致性保持。_2078040033306693634.json, 图片生成/图生图/一键换装：完美替换衣物，超高一致性保持（超低费用）_2068049220736733186.json, 图片生成/图生图/人物光影修图_2049318930015068162.json, 图片生成/图生图/多角度视角控制_2017241324424011778.json, 图片生成/图生图/没啥用的 qwen 多角度视角控制_2040817872036962306.json, 图片生成/文生图/Qwen Edit 2511多角度视角控制_2073300184922148866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/qwen视角控制_2055330832017043457.json、图片生成/图生图/▶Qwen Edit 2511多角度视角控制_2086719564179656705.json、图片生成/图生图/一键换装，电商福音，复杂场景超高一致性_2054931613225635841.json、图片生成/图生图/一键换装，电商福音，复杂场景超高一致性_2055107672713768961.json、图片生成/图生图/一键换装：完美替换衣物，超高一致性保持。_2078040033306693634.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 9/10 个有
- `QwenEditOutputExtractor` —— 9/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `QwenEditAdaptiveLongestEdge` —— 5/10 个有
- `QwenMultiangleCameraNode` —— 5/10 个有
- `easy showAnything` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 10 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta57 | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，10 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta57，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
