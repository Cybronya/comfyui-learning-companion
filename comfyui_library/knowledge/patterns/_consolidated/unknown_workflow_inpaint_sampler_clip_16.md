---
name: unknown_workflow_inpaint_sampler_clip_16
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9625
common_nodes: [CLIPTextEncode, DifferentialDiffusion, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, MaskBlur+, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/MAD重绘_1955237641445785602.json, 平台全量/Z-image 局部重绘_1997674103219924993.json, 平台全量/Z-image局部重绘_1999406383831318530.json, 平台全量/z-image局部重绘生成明星图片洗图神器_1995761911482429442.json, 平台全量/万物迁移 Z-image局部重绘 完胜Flux2+qwen千问_1995322113810685953.json, 平台全量/万能迁移 Z-image Base  局部重绘  真实自然无痕_2017070254689624065.json, 平台全量/局部重绘 Z-image Base 万能迁移  局部重绘 极速版 真实自然无痕_2017060526060212226.json, 平台全量/局部重绘 Z-image Base 万能迁移  局部重绘 极速版 真实自然无痕_2048286880311025666.json, 平台全量/局部重绘 Z-image Base 万能迁移  局部重绘 极速版 真实自然无痕_2051136159497105409.json, 平台全量/造相-Z-Image-Turbo-标准工作流 Z-image局部重绘_1995771017026998273.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/MAD重绘_1955237641445785602.json、平台全量/Z-image 局部重绘_1997674103219924993.json、平台全量/Z-image局部重绘_1999406383831318530.json、平台全量/z-image局部重绘生成明星图片洗图神器_1995761911482429442.json、平台全量/万物迁移 Z-image局部重绘 完胜Flux2+qwen千问_1995322113810685953.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskBlur+`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `ConditioningZeroOut` —— 9/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `ApplyFBCacheOnModel` —— 1/10 个有
- `DualCLIPLoader` —— 1/10 个有
- `FeatherMask` —— 1/10 个有
- `GrowMask` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/10 个有
- `MaskPreview+` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 0.85 | 0.85 - 1 | 10 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 0.85，观测区间 0.85 - 1，10 个样本，取值集中（一致性 95%）
