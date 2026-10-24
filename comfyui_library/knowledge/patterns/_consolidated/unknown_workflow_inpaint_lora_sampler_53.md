---
name: unknown_workflow_inpaint_lora_sampler_53
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.888
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, INPAINT_ExpandMask, INTConstant, ImageSmartSharpen+, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, WD14Tagger|pysssss]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SDXL  klein两种高效对图片修复流（修手 修崩图）-V3_2031552243610161154.json, 图片生成/图生图/★（黑鹤）NSW修复流-V3_2027034021905047554.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SDXL  klein两种高效对图片修复流（修手 修崩图）-V3_2031552243610161154.json、图片生成/图生图/★（黑鹤）NSW修复流-V3_2027034021905047554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CompressImages` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GroupSwitcher` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RAMCleanup` —— 1/2 个有
- `TT_img_enc_v2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.475 | - | 2 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.475，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
