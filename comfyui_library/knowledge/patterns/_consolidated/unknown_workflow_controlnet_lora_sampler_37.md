---
name: unknown_workflow_controlnet_lora_sampler_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5895
common_nodes: [Any Switch (rgthree), AnyLineArtPreprocessor_aux, CFGNorm, CLIPLoader, ConditioningCombine, ConditioningSetTimestepRange, ConditioningZeroOut, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, Fast Groups Muter (rgthree), Image Comparer (rgthree), Image Filter Adjustments, Image Save, ImageBlend, ImageScaleToTotalPixels, JWImageResizeByLongerSide, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SimpleMathSlider+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json, 平台全量/方汤圆的Qwen image edit 原生CN控制工作流体验版_1977659517959831553.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/方汤圆Qwen image edit CN控制工作流V1.1_2038879611219611650.json、平台全量/方汤圆的Qwen image edit 原生CN控制工作流体验版_1977659517959831553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AnyLineArtPreprocessor_aux`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `Image Save`
- `ImageBlend`
- `ImageScaleToTotalPixels`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SimpleMathSlider+`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 1/2 个有
- `InpaintCropImproved` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
