---
name: unknown_workflow_inpaint_sampler_clip_15
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.988143
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/局部重绘 产品替换 产品修复 产品换背景_1920647766408892417.json, 图片生成/图生图/局部重绘-FLUX_1912686838765580289.json, 图片生成/图生图/局部重绘_2031758654524891137.json, 图片生成/图生图/画板填充  扩展画面 图像放大_1897451969622298625.json, 图片生成/文生图/OneReward Fill局部重绘、扩图工作流_2047960078526976002.json, 图片生成/文生图/局部重绘 产品替换 产品修复 产品换背景_1931362971040022529.json, 视频生成/图生视频/局部重绘 产品替换  修复 换背景_1932632244605620225.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/局部重绘 产品替换 产品修复 产品换背景_1920647766408892417.json、图片生成/图生图/局部重绘-FLUX_1912686838765580289.json、图片生成/图生图/局部重绘_2031758654524891137.json、图片生成/图生图/画板填充  扩展画面 图像放大_1897451969622298625.json、图片生成/文生图/OneReward Fill局部重绘、扩图工作流_2047960078526976002.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `ImagePadForOutpaint` —— 2/7 个有
- `DifferentialDiffusion` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | 20 - 25 | 7 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22，观测区间 20 - 25，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
