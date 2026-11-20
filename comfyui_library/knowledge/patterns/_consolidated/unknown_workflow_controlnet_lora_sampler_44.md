---
name: unknown_workflow_controlnet_lora_sampler_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8915
common_nodes: [AlignYourStepsScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, ImageScaleToTotalPixels, KSamplerSelect, LayerColor: Brightness & Contrast, LoadImage, LoraLoader, PreviewImage, RH_Captioner, SamplerCustom, SaveImage, VAEDecode, easy imageSize, easy positive]
problems: []
missing: []
members: [平台全量/Hoko Manga Style 1.5_1869937841319874562.json, 平台全量/写实人像转黑白图像_1848260008881405953.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Hoko Manga Style 1.5_1869937841319874562.json、平台全量/写实人像转黑白图像_1848260008881405953.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AlignYourStepsScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RH_Captioner`
- `SamplerCustom`
- `SaveImage`
- `VAEDecode`
- `easy imageSize`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ConcatText_Zho` —— 1/2 个有
- `ControlNetApply` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageEffectsGrayscale` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.65 | - | 2 | 92% |
| LoRA 模型强度 | 0.75 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
