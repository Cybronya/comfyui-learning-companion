---
name: unknown_workflow_sampler_unet_vae_272
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.825
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json, 图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json, 图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_272

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json、图片生成/图生图/Qwen-Image 2.1图像编辑（海报）_2109584446545551362.json、图片生成/图生图/qwen-image2.1 一键图片自动透明分层_2109549307715211265.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenPERewriteT8` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `JjkShowText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextGenerate` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1920 | 3 | 68% |
| 采样步数 | 25 | 8 - 25 | 3 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1920，3 个样本
- 采样步数 中位数 25，观测区间 8 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
