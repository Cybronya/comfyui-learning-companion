---
name: unknown_workflow_inpaint_sampler_clip_26
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.873
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图 超强胸部增强 丰胸工作流_1969969383927914498.json, 图片生成/图生图/FLUX模型基础工作流-局部重绘_1898170958396477442.json, 图片生成/图生图/Fill-flux-dev 重绘 OneReward fp8 工作流_1965826858283634690.json, 图片生成/图生图/Flux-fill局部重绘（手脚还原比较好）_1968246530505363458.json, 图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json, 图片生成/图生图/flux丰胸_1902291922483093505.json, 平台全量/手部修复-手动涂抹_1922560532849594370.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX图生图 超强胸部增强 丰胸工作流_1969969383927914498.json、图片生成/图生图/FLUX模型基础工作流-局部重绘_1898170958396477442.json、图片生成/图生图/Fill-flux-dev 重绘 OneReward fp8 工作流_1965826858283634690.json、图片生成/图生图/Flux-fill局部重绘（手脚还原比较好）_1968246530505363458.json、图片生成/图生图/OneReward——Fill-flux-dev 局部重绘_1966159114428649474.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 4/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `YC_SingleTextNode` —— 2/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `String` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 36% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
