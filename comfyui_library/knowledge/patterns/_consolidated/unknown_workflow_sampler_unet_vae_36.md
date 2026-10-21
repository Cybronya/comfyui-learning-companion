---
name: unknown_workflow_sampler_unet_vae_36
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.843615
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102217964954152961.json, 图片生成/图生图/2102232455502716929.json, 图片生成/图生图/2102236996667265025.json, 图片生成/图生图/2102319407006572545.json, 图片生成/图生图/2102322312635834369.json, 图片生成/图生图/2102343043620888578.json, 图片生成/图生图/2102572577544818689.json, 图片生成/图生图/2102593163918667778.json, 图片生成/图生图/2102599002511462402.json, 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json, 图片生成/文生图/Qwen-Image-2.1-图生图_2101854452645978114.json, 图片生成/文生图/Qwen_Image_2.1_文生图_6步加速无PE_2107979311847399426.json, 图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_36

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/2102217964954152961.json、图片生成/图生图/2102232455502716929.json、图片生成/图生图/2102236996667265025.json、图片生成/图生图/2102319407006572545.json、图片生成/图生图/2102322312635834369.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/13 个有
- `EmptyLatentImage` —— 9/13 个有
- `QwenImage21Cache` —— 9/13 个有
- `ResolutionSelector` —— 8/13 个有
- `ComfySwitchNode` —— 6/13 个有
- `SaveImageAdvanced` —— 6/13 个有
- `PrimitiveStringMultiline` —— 5/13 个有
- `PreviewImage` —— 4/13 个有
- `EmptyImage` —— 3/13 个有
- `YK_LoadImageFromURL` —— 2/13 个有
- `AIO_Preprocessor` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 40 | 13 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 40，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
