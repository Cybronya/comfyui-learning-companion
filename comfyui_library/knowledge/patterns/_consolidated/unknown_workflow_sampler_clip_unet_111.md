---
name: unknown_workflow_sampler_clip_unet_111
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9213
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI官方示例16：HiDream-I1文生图工作流 _ ComfyUI从入门到精通_1934213208926285826.json, 图片生成/文生图/FLUX Krea文生图_1950966820087988225.json, 图片生成/文生图/FLUX Krea文生图，低“AI味”，真实感_1959107680914845697.json, 图片生成/文生图/FLUX Krea文生图，低“AI味”，真实感_1991804904345907201.json, 图片生成/文生图/FLUX-Krea-BLAZE_1951967199781179393.json, 图片生成/文生图/Flux Krea 基础文生图工作流｜批量生产_1951122744584904705.json, 图片生成/文生图/Flux Krea 文生图 批量版_1951100464836321282.json, 图片生成/文生图/Flux Krea 文生图_1951056396223754242.json, 图片生成/文生图/Hidream 基础文生图_1913248213732683777.json, 图片生成/文生图/flux1-krea-dev（修正手脚细节）_1951256026077188097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_111

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/ComfyUI官方示例16：HiDream-I1文生图工作流 _ ComfyUI从入门到精通_1934213208926285826.json、图片生成/文生图/FLUX Krea文生图_1950966820087988225.json、图片生成/文生图/FLUX Krea文生图，低“AI味”，真实感_1959107680914845697.json、图片生成/文生图/FLUX Krea文生图，低“AI味”，真实感_1991804904345907201.json、图片生成/文生图/FLUX-Krea-BLAZE_1951967199781179393.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/10 个有
- `DualCLIPLoader` —— 8/10 个有
- `CR Prompt List` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `ModelSamplingSD3` —— 2/10 个有
- `QuadrupleCLIPLoader` —— 2/10 个有
- `Fans Prompt Styler Negative` —— 1/10 个有
- `FluxKontextImageScale` —— 1/10 个有
- `HYPIRImageRestoration` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 10 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 10 | 14% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，10 个样本，取值分散，一致性仅 14%
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
