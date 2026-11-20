---
name: unknown_workflow_unet_vae_12
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.74375
common_nodes: [CLIPLoader, EmptyLatentImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json, 图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2111477762887348225.json, 平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 Turbo 文生图_2113964528772935682.json、图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json、图片生成/文生图/image_qwen_image_2_1_t2i_2111477762887348225.json、平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 3/4 个有
- `ComfySwitchNode` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RandomNoise` —— 3/4 个有
- `SamplerCustomAdvanced` —— 3/4 个有
- `TextGenerate` —— 3/4 个有
- `PreviewAny` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
