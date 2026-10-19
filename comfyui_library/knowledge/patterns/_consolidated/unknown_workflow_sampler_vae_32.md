---
name: unknown_workflow_sampler_vae_32
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.962714
common_nodes: [DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1938503902566506497.json, 图片生成/文生图/1952701907708088321.json, 图片生成/文生图/1954159231169642497.json, 图片生成/文生图/1954834253982908418.json, 图片生成/文生图/1957280959416692738.json, 图片生成/文生图/1975059574103347202.json, 图片生成/文生图/1981703392366084098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1938503902566506497.json、图片生成/文生图/1952701907708088321.json、图片生成/文生图/1954159231169642497.json、图片生成/文生图/1954834253982908418.json、图片生成/文生图/1957280959416692738.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/7 个有
- `ConditioningZeroOut` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `FluxGuidance` —— 5/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `TeaCache` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `ImageUpscaleWithModel` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `CLIPTextEncodeFlux` —— 1/7 个有
- `LoraLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 7 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 7 | 0% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 57% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
