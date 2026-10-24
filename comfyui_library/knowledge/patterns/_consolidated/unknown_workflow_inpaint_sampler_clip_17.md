---
name: unknown_workflow_inpaint_sampler_clip_17
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.863667
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图 超强胸部增强 丰胸工作流_1969969383927914498.json, 图片生成/图生图/FLUX模型基础工作流-局部重绘_1898170958396477442.json, 图片生成/图生图/Fill-flux-dev 重绘 OneReward fp8 工作流_1965826858283634690.json, 图片生成/图生图/Flux-fill局部重绘（手脚还原比较好）_1968246530505363458.json, 图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json, 图片生成/图生图/flux丰胸_1902291922483093505.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX图生图 超强胸部增强 丰胸工作流_1969969383927914498.json、图片生成/图生图/FLUX模型基础工作流-局部重绘_1898170958396477442.json、图片生成/图生图/Fill-flux-dev 重绘 OneReward fp8 工作流_1965826858283634690.json、图片生成/图生图/Flux-fill局部重绘（手脚还原比较好）_1968246530505363458.json、图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `YC_SingleTextNode` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `String` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 34% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
