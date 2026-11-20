---
name: text_to_image_sampler_clip_unet_75
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9775
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json, 图片生成/文生图/Z-image 文生图_2006288280186265601.json, 图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json, 图片生成/文生图/Z-image 超清快速30秒文生图 省时省币_2038518587316506625.json, 图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json, 图片生成/文生图/Z-image 超清快速文生图_2010897242143592450.json, 图片生成/文生图/Z-image 超清快速文生图_2038470583129743361.json, 图片生成/文生图/Z-image-Turbo电影质感文生图_2056911427314737153.json, 图片生成/文生图/z-image-turbo flow dpo版文生图 自用_2050564898463207426.json, 图片生成/文生图/z-image-turbo-flow-dpo版文生图_2027731924940230658.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json、图片生成/文生图/Z-image 文生图_2006288280186265601.json、图片生成/文生图/Z-image 最新模型 文生图工作流V1.0_1993835227038629890.json、图片生成/文生图/Z-image 超清快速30秒文生图 省时省币_2038518587316506625.json、图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `CR Prompt Text` —— 3/10 个有
- `Int` —— 3/10 个有
- `easy seed` —— 3/10 个有
- `HAIGC_SaveImagesToZip` —— 2/10 个有
- `CustomAddLabel` —— 1/10 个有
- `DuckHideNode` —— 1/10 个有
- `LamSwitcherCase` —— 1/10 个有
- `ZML_ImageEncryption` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1920 | 10 | 69% |
| 高度 | 1504 | 1024 - 1920 | 10 | 77% |
| 采样步数 | 10 | 8 - 20 | 10 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1920，10 个样本
- 高度 中位数 1504，观测区间 1024 - 1920，10 个样本
- 采样步数 中位数 10，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
