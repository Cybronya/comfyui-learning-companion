---
name: unknown_workflow_sampler_vae_49
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.839833
common_nodes: [BluePixelCFGGuider, BluePixelCLIPLoader, BluePixelDiffusionLoader, BluePixelEditConditioning, BluePixelEmptyLatent, BluePixelEulerSampler, BluePixelNoise, BluePixelPrepareImage, BluePixelScheduler, BluePixelTextEncode, BluePixelVAELoader, LoadImage, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/BluePixel 4K 快速图像编辑_2116849939245518850.json, 图片生成/图生图/BluePixel 4K 秒级图像编辑_2116227925279330305.json, 图片生成/图生图/BluePixel+4K+秒级图像编辑_极速版_2117140725770055682.json, 平台全量/4k极速单图编辑BluePixel_2118175552208199682.json, 平台全量/BluePixel_4K_秒级图像编辑_2117475022578212865.json, 视频生成/图生视频/BluePixel_4K_秒级图像编辑_2117028378174902273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_49

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/BluePixel 4K 快速图像编辑_2116849939245518850.json、图片生成/图生图/BluePixel 4K 秒级图像编辑_2116227925279330305.json、图片生成/图生图/BluePixel+4K+秒级图像编辑_极速版_2117140725770055682.json、平台全量/4k极速单图编辑BluePixel_2118175552208199682.json、平台全量/BluePixel_4K_秒级图像编辑_2117475022578212865.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `BluePixelCFGGuider`
- `BluePixelCLIPLoader`
- `BluePixelDiffusionLoader`
- `BluePixelEditConditioning`
- `BluePixelEmptyLatent`
- `BluePixelEulerSampler`
- `BluePixelNoise`
- `BluePixelPrepareImage`
- `BluePixelScheduler`
- `BluePixelTextEncode`
- `BluePixelVAELoader`
- `LoadImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `ComfyMathExpression` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `PrimitiveInt` —— 4/6 个有
- `ResolutionSelector` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 3840 | 6 | 30% |
| 高度 | 1024 | 1024 - 2176 | 6 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 3840，6 个样本，取值分散，一致性仅 30%
- 高度 中位数 1024，观测区间 1024 - 2176，6 个样本
