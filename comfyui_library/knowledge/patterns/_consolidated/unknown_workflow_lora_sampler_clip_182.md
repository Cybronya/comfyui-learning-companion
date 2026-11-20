---
name: unknown_workflow_lora_sampler_clip_182
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87325
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, InFluxModelSamplingPred, LayerUtility: ImageScaleByAspectRatio V2, LoraLoader, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品精修_Flux_1955262700215570434.json, 图片生成/图生图/批量精修工作流_2028307521479380994.json, 图片生成/图生图/服装精修_2027645351355752449.json, 平台全量/生成自己的创意形象_形象转绘_万物转绘_1893944807910211585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/产品精修_Flux_1955262700215570434.json、图片生成/图生图/批量精修工作流_2028307521479380994.json、图片生成/图生图/服装精修_2027645351355752449.json、平台全量/生成自己的创意形象_形象转绘_万物转绘_1893944807910211585.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `InFluxModelSamplingPred`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `Anything Everywhere3` —— 3/4 个有
- `Float` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageBlend` —— 3/4 个有
- `Int` —— 3/4 个有
- `LayerColor: Brightness & Contrast` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewBridge` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy hiresFix` —— 3/4 个有
- `ArgosTranslateTextNode` —— 1/4 个有
- `Primitive string [Crystools]` —— 1/4 个有
- `RHUploadZip` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.9 - 0.9 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.9 - 0.9，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
