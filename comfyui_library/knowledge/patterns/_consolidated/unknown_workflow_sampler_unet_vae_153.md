---
name: unknown_workflow_sampler_unet_vae_153
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.789
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1文生图_2101860458935439362.json, 图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json, 图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json, 图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json, 图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json, 图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json, 图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_153

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1文生图_2101860458935439362.json、图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json、图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json、图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json、图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/7 个有
- `TextGenerateLTX2Prompt` —— 4/7 个有
- `Text` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `TextGenerate` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `easy promptList` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 30 - 50 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 30 - 50，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
