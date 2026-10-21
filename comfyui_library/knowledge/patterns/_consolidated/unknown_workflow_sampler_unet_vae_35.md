---
name: unknown_workflow_sampler_unet_vae_35
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.821
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, CR Prompt Text]
members: [图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json, 图片生成/图生图/2101686169661693953.json, 图片生成/图生图/2101886414299426818.json, 图片生成/图生图/2102129332872372226.json, 图片生成/图生图/2102228368161853441.json, 图片生成/图生图/2102243596664655874.json, 图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102235294379630593.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102401855983808514.json, 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json, 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json, 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 PE 文生图_2102401855983808514.json、图片生成/图生图/2101686169661693953.json、图片生成/图生图/2101886414299426818.json、图片生成/图生图/2102129332872372226.json、图片生成/图生图/2102228368161853441.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/13 个有
- `QwenPERewriteT8` —— 10/13 个有
- `easy cleanGpuUsed` —— 10/13 个有
- `easy showAnything` —— 10/13 个有
- `LoadImage` —— 6/13 个有
- `CM_IntToFloat` —— 1/13 个有
- `ImageScale` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `Lora Loader Stack (rgthree)` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 13 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1024 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、CR Prompt Text
