---
name: unknown_workflow_inpaint_lora_sampler_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.827667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/眼镜迁移至模特工作流_1921010202764840961.json, 平台全量/ACE++万物迁移_1964640850301079554.json, 视频生成/图生视频/ACE++换脸换产品工作流_2010001647530942465.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/眼镜迁移至模特工作流_1921010202764840961.json、平台全量/ACE++万物迁移_1964640850301079554.json、视频生成/图生视频/ACE++换脸换产品工作流_2010001647530942465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `Get resolution [Crystools]` —— 1/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `InpaintResize` —— 1/3 个有
- `JanusImageUnderstanding` —— 1/3 个有
- `JanusModelLoader` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy imageSize` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 3 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.25 | 3 | 89% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.25，3 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
