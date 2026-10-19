---
name: unknown_workflow_lora_sampler_unet_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.928
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, ImageMirror, KSampler, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader, YCFaceAlignToCanvas, YCFaceAnalysisModels]
problems: []
missing: [LayerUtility: TextBox, Text Concatenate]
members: [图片生成/文生图/1983057404365549569.json, 图片生成/文生图/1983827405842358274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1983057404365549569.json、图片生成/文生图/1983827405842358274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageMirror`
- `KSampler`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YCFaceAlignToCanvas`
- `YCFaceAnalysisModels`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 100% |
| 采样算法 | euler_cfg_pp | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1280 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_cfg_pp，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: TextBox、Text Concatenate
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
