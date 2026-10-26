---
name: unknown_workflow_sampler_clip_unet_474
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [ApplyPulidFlux, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux1_文生图，锁定人脸_2062362511936155649.json, 图片生成/文生图/指定人脸出图_1928700813932400642.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_474

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux1_文生图，锁定人脸_2062362511936155649.json、图片生成/文生图/指定人脸出图_1928700813932400642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicScheduler`
- `CLIPTextEncode`
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
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `easy positive` —— 1/2 个有
- `easy stylesSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
