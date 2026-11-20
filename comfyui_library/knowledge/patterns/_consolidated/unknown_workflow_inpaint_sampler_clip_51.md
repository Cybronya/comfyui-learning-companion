---
name: unknown_workflow_inpaint_sampler_clip_51
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.844
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/即梦、豆包、可灵等全平台图片去水印_1940363548763779074.json, 图片生成/图生图/最新Flux自动修复手部畸形工作流_1891472578710507522.json, 图片生成/文生图/OneReward移除_1989974232891355137.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/即梦、豆包、可灵等全平台图片去水印_1940363548763779074.json、图片生成/图生图/最新Flux自动修复手部畸形工作流_1891472578710507522.json、图片生成/文生图/OneReward移除_1989974232891355137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MaskPreview` —— 2/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `MediapipeHandNode` —— 1/3 个有
- `SAMModelLoader (segment anything)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
