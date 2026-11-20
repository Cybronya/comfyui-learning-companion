---
name: unknown_workflow_inpaint_sampler_clip_90
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.958
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/图片破损划痕污点预处理+去水印_1917818805807157249.json, 平台全量/局部重绘工作流-可换装换物品_1905559066784239618.json, 平台全量/局部重绘移除工作流_1929523569284517889.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图片破损划痕污点预处理+去水印_1917818805807157249.json、平台全量/局部重绘工作流-可换装换物品_1905559066784239618.json、平台全量/局部重绘移除工作流_1929523569284517889.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
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
- `Image Comparer (rgthree)` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `CLIPTextEncodeWithWeight //Inspire` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImpactGaussianBlurMask` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
