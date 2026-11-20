---
name: unknown_workflow_sampler_vae_62
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.881
common_nodes: [BasicGuider, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RHFibo2EditConditioning, RHFibo2ModelLoader, RHFibo2Scheduler, RHFibo2TextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fibo2工作流修改图片_2111991292468228098.json, 图片生成/图生图/pandy-FIBO2-Turbo4步图像编辑_2114251172331741186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_62

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Fibo2工作流修改图片_2111991292468228098.json、图片生成/图生图/pandy-FIBO2-Turbo4步图像编辑_2114251172331741186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
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
- `GetImageSize` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RHFibo2KeepOutsideMask` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
