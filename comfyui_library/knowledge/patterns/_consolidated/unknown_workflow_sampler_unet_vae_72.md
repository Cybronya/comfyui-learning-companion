---
name: unknown_workflow_sampler_unet_vae_72
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.665889
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/图生图/2101559779452866561.json, 图片生成/图生图/2101865008786395137.json, 图片生成/图生图/2102191085471752193.json, 图片生成/图生图/2102203525789995009.json, 图片生成/图生图/2102207016054906881.json, 图片生成/图生图/2102212148364668930.json, 图片生成/图生图/2102215048675545090.json, 图片生成/图生图/2102265363466645506.json, 图片生成/图生图/2102621542323675137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_72

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2101559779452866561.json、图片生成/图生图/2101865008786395137.json、图片生成/图生图/2102191085471752193.json、图片生成/图生图/2102203525789995009.json、图片生成/图生图/2102207016054906881.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `SaveImageAdvanced` —— 5/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `GetImageSize` —— 2/9 个有
- `ResizeImageMaskNode` —— 2/9 个有
- `DrawMaskOnImage` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageCompare` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1536 | 9 | 85% |
| 采样步数 | 40 | 25 - 50 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，9 个样本，取值集中（一致性 85%）
- 采样步数 中位数 40，观测区间 25 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
