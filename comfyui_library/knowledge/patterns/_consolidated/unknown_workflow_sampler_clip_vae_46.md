---
name: unknown_workflow_sampler_clip_vae_46
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9502
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json, 图片生成/图生图/REDUX洗图工作流_1967519880650088450.json, 平台全量/F1 洗图  图生图 规避版权_1915291948226117633.json, 平台全量/FLUX Redux单图_多图风格参考图像生图工作流_1927249197257412609.json, 平台全量/人像风格迁移_1920686999265542145.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_46

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux Redux - Official Flux Tools by BFL - Beginner_1864884851341217793.json、图片生成/图生图/REDUX洗图工作流_1967519880650088450.json、平台全量/F1 洗图  图生图 规避版权_1915291948226117633.json、平台全量/FLUX Redux单图_多图风格参考图像生图工作流_1927249197257412609.json、平台全量/人像风格迁移_1920686999265542145.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `StyleModelApply` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `ControlNetLoader` —— 2/5 个有
- `ReduxAdvanced` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `ConditioningCombine` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `ViewText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 5 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 5 | 67% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1000 | 512 - 1280 | 5 | 68% |
| 高度 | 856 | 512 - 1400 | 5 | 68% |
| ControlNet 权重 | 0.85 | - | 2 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，5 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1000，观测区间 512 - 1280，5 个样本
- 高度 中位数 856，观测区间 512 - 1400，5 个样本
- ControlNet 权重 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
