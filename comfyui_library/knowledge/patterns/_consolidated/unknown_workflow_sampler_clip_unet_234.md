---
name: unknown_workflow_sampler_clip_unet_234
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.703833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen标题文字设计_2078468152178073601.json, 图片生成/文生图/Z-image base文生图_2017842003442147330.json, 图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json, 图片生成/文生图/image_qwen_Image_2512 BF16_2073295897374584833.json, 图片生成/文生图/image_qwen_image_1954461836424953858.json, 图片生成/文生图/zimage 文生图_2039168907927359490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_234

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen标题文字设计_2078468152178073601.json、图片生成/文生图/Z-image base文生图_2017842003442147330.json、图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json、图片生成/文生图/image_qwen_Image_2512 BF16_2073295897374584833.json、图片生成/文生图/image_qwen_image_1954461836424953858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `StringConcatenate` —— 2/6 个有
- `PreviewImage` —— 1/6 个有
- `SomethingToString` —— 1/6 个有
- `XXBuHuo_TXT` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `easy textIndexSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | 8 - 50 | 6 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 35% |
| 采样算法 | res_multistep | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，观测区间 8 - 50，6 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 res_multistep，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
