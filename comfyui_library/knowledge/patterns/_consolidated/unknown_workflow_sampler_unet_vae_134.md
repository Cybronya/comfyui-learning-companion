---
name: unknown_workflow_sampler_unet_vae_134
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8164
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json, 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json, 图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json, 图片生成/文生图/qwen-image2.1-文生图_2105500926474801154.json, 图片生成/文生图/千问2.1 文生图片（支持生成透明图片）_2103811218925510657.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json、图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json、图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json、图片生成/文生图/qwen-image2.1-文生图_2105500926474801154.json、图片生成/文生图/千问2.1 文生图片（支持生成透明图片）_2103811218925510657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `SaveImageAdvanced` —— 3/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1080 | 5 | 98% |
| 高度 | 1024 | 1024 - 1920 | 5 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，5 个样本
