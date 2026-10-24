---
name: unknown_workflow_sampler_unet_vae_81
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.599818
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json, 图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json, 图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json, 图片生成/图生图/qwen2.1 漫剧角色三视图生成_2110530131713421314.json, 图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json, 图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2108373842572959745.json, 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json, 图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json, 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_81

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json、图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json、图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json、图片生成/图生图/qwen2.1 漫剧角色三视图生成_2110530131713421314.json、图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 10/11 个有
- `ComfySwitchNode` —— 7/11 个有
- `CR Prompt Text` —— 6/11 个有
- `GetNode` —— 6/11 个有
- `SetNode` —— 6/11 个有
- `Text` —— 5/11 个有
- `TextGenerateLTX2Prompt` —— 4/11 个有
- `忽略多组孤海` —— 4/11 个有
- `Anything Everywhere3` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `Seed (rgthree)` —— 2/11 个有
- `BatchImagesNode` —— 1/11 个有
- `Int` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 25 - 40 | 11 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 32% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1024 | 992 - 1024 | 11 | 99% |
| 高度 | 1024 | 1024 - 1024 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 25 - 40，11 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 992 - 1024，11 个样本，取值集中（一致性 99%）
- 高度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
