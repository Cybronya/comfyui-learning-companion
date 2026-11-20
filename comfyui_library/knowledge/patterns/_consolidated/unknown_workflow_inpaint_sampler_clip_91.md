---
name: unknown_workflow_inpaint_sampler_clip_91
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.930333
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/电商图片修复_1915376635628163073.json, 平台全量/神奇消失术（消除万物）_1947484264934838273.json, 平台全量/移除工作流_1978340615689789442.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/电商图片修复_1915376635628163073.json、平台全量/神奇消失术（消除万物）_1947484264934838273.json、平台全量/移除工作流_1978340615689789442.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImpactGaussianBlurMask` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
