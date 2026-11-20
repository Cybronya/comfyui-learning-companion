---
name: unknown_workflow_sampler_unet_vae_154
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.535
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json, 图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json, 图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json, 图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2108373842572959745.json, 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_154

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json、图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json、图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json、图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json、图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `Text` —— 4/7 个有
- `忽略多组孤海` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `BatchImagesNode` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 30 - 40 | 7 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 992 - 1024 | 7 | 99% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 30 - 40，7 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 992 - 1024，7 个样本，取值集中（一致性 99%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
