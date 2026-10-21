---
name: unknown_workflow_controlnet_upscale_lora_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7315
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Upscale Image, ControlNetApplyAdvanced, ControlNetLoader, EasyCache, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler (Efficient), LoadImage, LoraLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2, SetUnionControlNetType, UNETLoader, UltimateSDUpscale, UnetLoaderGGUF, UpscaleModelLoader, VAEEncode, VAELoader]
problems: []
missing: [KSampler (Efficient), CR Upscale Image]
members: [图片生成/文生图/1980987335540084737.json, 图片生成/文生图/Qwen-Image多重LoRA文生图+高清放大综合工作流_1997901457099751425.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1980987335540084737.json、图片生成/文生图/Qwen-Image多重LoRA文生图+高清放大综合工作流_1997901457099751425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Upscale Image`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EasyCache`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SetUnionControlNetType`
- `UNETLoader`
- `UltimateSDUpscale`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.75 | - | 2 | 67% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 35 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：KSampler (Efficient)、CR Upscale Image
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
