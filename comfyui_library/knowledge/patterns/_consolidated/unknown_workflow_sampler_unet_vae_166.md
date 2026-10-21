---
name: unknown_workflow_sampler_unet_vae_166
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.75325
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json, 图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json, 图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json, 图片生成/文生图/qwen2.1文生图_2103878768724107266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json、图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json、图片生成/文生图/qwen image 2.1 文生图提示词扩写_2102006301646745601.json、图片生成/文生图/qwen2.1文生图_2103878768724107266.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
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
- `StringConstantMultiline` —— 3/4 个有
- `TextGenerate` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `PreviewAny` —— 2/4 个有
- `StringFunction|pysssss` —— 2/4 个有
- `StringReplace` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 40 | 40 - 50 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 50，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
