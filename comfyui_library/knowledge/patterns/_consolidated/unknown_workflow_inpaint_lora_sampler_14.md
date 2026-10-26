---
name: unknown_workflow_inpaint_lora_sampler_14
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.853714
common_nodes: [CLIPLoader, ConditioningZeroOut, GrowMaskWithBlur, Image Comparer (rgthree), InpaintCropImproved, InpaintStitchImproved, KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview+, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部批图p图修改文字美工电商图文修改_2067435903903166466.json, 图片生成/图生图/局部批图p图修改文字美工电商图文修改_2067549170898132994.json, 图片生成/图生图/局部批图p图修改文字美工电商图文修改_2082712829043499009.json, 图片生成/图生图/局部重绘_2081739421422022657.json, 图片生成/图生图/局部重绘_P图改字_2073664975360585729.json, 图片生成/图生图/局部重绘_P图改字（美工必备）_2005210269997559809.json, 图片生成/图生图/局部重绘_P图改字（美工必备）_2056598235896176642.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/局部批图p图修改文字美工电商图文修改_2067435903903166466.json、图片生成/图生图/局部批图p图修改文字美工电商图文修改_2067549170898132994.json、图片生成/图生图/局部批图p图修改文字美工电商图文修改_2082712829043499009.json、图片生成/图生图/局部重绘_2081739421422022657.json、图片生成/图生图/局部重绘_P图改字_2073664975360585729.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `ETN_LoadMaskBase64` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
