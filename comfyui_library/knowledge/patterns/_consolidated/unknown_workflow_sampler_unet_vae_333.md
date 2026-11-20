---
name: unknown_workflow_sampler_unet_vae_333
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.797
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json, 平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json, 数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_333

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json、平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json、数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `QwenImage21Cache` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
