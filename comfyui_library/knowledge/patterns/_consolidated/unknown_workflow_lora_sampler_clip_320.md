---
name: unknown_workflow_lora_sampler_clip_320
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6065
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, Image Comparer (rgthree), JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, Qwen3_VQA, SaveImage, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/高真实性动漫转真人Q+Z二次采样工作流_2015763807888478210.json, 平台全量/QIANSUI+Qwen-Edit-2511+动漫转真人_2026572307510075394.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_320

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高真实性动漫转真人Q+Z二次采样工作流_2015763807888478210.json、平台全量/QIANSUI+Qwen-Edit-2511+动漫转真人_2026572307510075394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `Image Comparer (rgthree)`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ImageOnlyCheckpointLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_2m | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
