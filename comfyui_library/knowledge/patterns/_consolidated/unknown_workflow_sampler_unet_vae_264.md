---
name: unknown_workflow_sampler_unet_vae_264
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9558
common_nodes: [ApplyPulidFlux, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux1_文生图，锁定人脸_2062362511936155649.json, 图片生成/文生图/指定人脸出图_1928700813932400642.json, 平台全量/【阡陌】FLUX职业证件照摄影工作流_1902927275757572097.json, 平台全量/【阡陌】儿童证件照高清摄影工作流_1901924578233622530.json, 平台全量/【阡陌】最强换脸Flux PuLID文生图工作流_1910164683675107330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_264

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/flux1_文生图，锁定人脸_2062362511936155649.json、图片生成/文生图/指定人脸出图_1928700813932400642.json、平台全量/【阡陌】FLUX职业证件照摄影工作流_1902927275757572097.json、平台全量/【阡陌】儿童证件照高清摄影工作流_1901924578233622530.json、平台全量/【阡陌】最强换脸Flux PuLID文生图工作流_1910164683675107330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 4/5 个有
- `CLIPSetLastLayer` —— 3/5 个有
- `CLIPTextEncodeFlux` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `DeepTranslatorTextNode` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ViewText` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `CFGGuider` —— 1/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `easy positive` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |
| 宽度 | 1000 | 768 - 1200 | 5 | 86% |
| 高度 | 1400 | 1024 - 1600 | 5 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1000，观测区间 768 - 1200，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1400，观测区间 1024 - 1600，5 个样本，取值集中（一致性 82%）
