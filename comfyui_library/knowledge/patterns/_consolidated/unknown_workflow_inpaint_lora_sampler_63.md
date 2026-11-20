---
name: unknown_workflow_inpaint_lora_sampler_63
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.919
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageCrop+, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/人物换脸（面部占比尽量大）_1945037639822270466.json, 图片生成/图生图/迁移工作流_1906365355587981313.json, 平台全量/【FLUX redux】换脸原度超高_1907063356610469890.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物换脸（面部占比尽量大）_1945037639822270466.json、图片生成/图生图/迁移工作流_1906365355587981313.json、平台全量/【FLUX redux】换脸原度超高_1907063356610469890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop+`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 2/3 个有
- `ConditioningConcat` —— 1/3 个有
- `Florence2` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LoadFlorence2Model` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 10 - 30 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.1 - 1 | 3 | 39% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 10 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，3 个样本，取值分散，一致性仅 39%
