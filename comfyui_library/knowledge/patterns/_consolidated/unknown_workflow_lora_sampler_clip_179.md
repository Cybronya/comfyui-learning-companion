---
name: unknown_workflow_lora_sampler_clip_179
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.871333
common_nodes: [Anything Everywhere, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, Float, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, ImageBlend, InFluxModelSamplingPred, Int, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, OutFluxModelSamplingPred, PreviewBridge, PreviewImage, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy hiresFix]
problems: []
missing: []
members: [图片生成/图生图/产品精修_Flux_1955262700215570434.json, 图片生成/图生图/批量精修工作流_2028307521479380994.json, 图片生成/图生图/服装精修_2027645351355752449.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/产品精修_Flux_1955262700215570434.json、图片生成/图生图/批量精修工作流_2028307521479380994.json、图片生成/图生图/服装精修_2027645351355752449.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `Float`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `ImageBlend`
- `InFluxModelSamplingPred`
- `Int`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader`
- `OutFluxModelSamplingPred`
- `PreviewBridge`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy hiresFix`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RHUploadZip` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.9 - 0.9 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.9 - 0.9，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
