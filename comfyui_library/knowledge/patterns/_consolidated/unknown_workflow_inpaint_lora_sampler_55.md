---
name: unknown_workflow_inpaint_lora_sampler_55
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.869667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, INPAINT_ExpandMask, INTConstant, ImageSmartSharpen+, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, WD14Tagger|pysssss]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SDXL  klein两种高效对图片修复流（修手 修崩图）-V3_2031552243610161154.json, 图片生成/图生图/★（黑鹤）NSW修复流-V3_2027034021905047554.json, 平台全量/★（黑鹤）NSW修复流-V3_2025576724116803586.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL  klein两种高效对图片修复流（修手 修崩图）-V3_2031552243610161154.json、图片生成/图生图/★（黑鹤）NSW修复流-V3_2027034021905047554.json、平台全量/★（黑鹤）NSW修复流-V3_2025576724116803586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `INPAINT_ExpandMask`
- `INTConstant`
- `ImageSmartSharpen+`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `TT_img_enc_v2` —— 2/3 个有
- `CompressImages` —— 1/3 个有
- `GroupSwitcher` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RAMCleanup` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 6 - 15 | 3 | 65% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 3 | 56% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.45 - 0.5 | 3 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 6 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.45 - 0.5，3 个样本，取值集中（一致性 95%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
