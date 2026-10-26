---
name: unknown_workflow_sampler_vae_55
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.831
common_nodes: [Anything Everywhere3, BasicGuider, EmptyFlux2LatentImage, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RHFibo2EditConditioning, RHFibo2ModelLoader, RHFibo2Scheduler, RHFibo2TextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fibo2单图_多图编辑_2113181849085366274.json, 图片生成/图生图/Fibo2单图编辑_2113466985538482178.json, 图片生成/图生图/Fibo2多图编辑_2113823122217590785.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_55

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Fibo2单图_多图编辑_2113181849085366274.json、图片生成/图生图/Fibo2单图编辑_2113466985538482178.json、图片生成/图生图/Fibo2多图编辑_2113823122217590785.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RHFibo2EditConditioning`
- `RHFibo2ModelLoader`
- `RHFibo2Scheduler`
- `RHFibo2TextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: PersonMaskUltra` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
