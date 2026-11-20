---
name: unknown_workflow_lora_sampler_unet_315
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [CLIPLoader, CR Text Concatenate, ConditioningZeroOut, Image Comparer (rgthree), Image_Resize_longsize, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, TextInput_, UNETLoader, VAEDecode, VAELoader, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2509 超强一致性图片编辑(零偏移)｜移除｜改背景｜改颜色｜模特图｜改文字_2116061783831175171.json, 平台全量/Qwen Image Edit 2509 超强一致性图片编辑(零偏移)｜改文字｜改颜色｜改背景｜模特图｜移除_2117511644875149314.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_315

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2509 超强一致性图片编辑(零偏移)｜移除｜改背景｜改颜色｜模特图｜改文字_2116061783831175171.json、平台全量/Qwen Image Edit 2509 超强一致性图片编辑(零偏移)｜改文字｜改颜色｜改背景｜模特图｜移除_2117511644875149314.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `Image_Resize_longsize`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
