---
name: unknown_workflow_sampler_clip_vae_68
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RH_Translator, SaveImage, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku FLUX图像编辑极速版_1930474412905238530.json, 图片生成/文生图/FLUX加速文生图_1929527506691375106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_68

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Nunchaku FLUX图像编辑极速版_1930474412905238530.json、图片生成/文生图/FLUX加速文生图_1929527506691375106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RH_Translator`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Aspect Ratio` —— 1/2 个有
- `ImageAndMaskResizeNode` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
