---
name: unknown_workflow_lora_sampler_clip_101
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9385
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1913513255921250305.json, 图片生成/文生图/1954772987443503106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_101

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1913513255921250305.json、图片生成/文生图/1954772987443503106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `AIO_Preprocessor` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `LineArtPreprocessor` —— 1/2 个有
- `PoseNode` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |
| 宽度 | 940 | - | 2 | 95% |
| 高度 | 1240 | - | 2 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 940，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 高度 中位数 1240，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
