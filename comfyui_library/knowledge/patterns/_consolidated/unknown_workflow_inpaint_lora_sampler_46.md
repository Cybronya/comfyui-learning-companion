---
name: unknown_workflow_inpaint_lora_sampler_46
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.951
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoaderGGUF, EmptyImage, FluxGuidance, ImageCrop, ImageScale, ImageScaleToTotalPixels, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: NumberCalculator, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, ReduxAdvanced, SaveImage, StyleModelLoader, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json, 数字人/数字人/Flux-AI一键换脸_1929072980595261441.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json、数字人/数字人/Flux-AI一键换脸_1929072980595261441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoaderGGUF`
- `EmptyImage`
- `FluxGuidance`
- `ImageCrop`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: NumberCalculator`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ACE_TextTranslate` —— 1/2 个有
- `BboxDetectorCombined_v2` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `JWFloat` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
