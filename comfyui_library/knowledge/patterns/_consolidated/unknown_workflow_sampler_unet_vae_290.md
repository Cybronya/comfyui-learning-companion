---
name: unknown_workflow_sampler_unet_vae_290
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.859333
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json, 图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json, 图片生成/文生图/【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_290

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json、图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json、图片生成/文生图/【Qwen_Image_2.1】文生图_官方PE丨老许Gary_2102919042645454849.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PreviewAny` —— 2/3 个有
- `StringConstantMultiline` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
