---
name: unknown_workflow_sampler_unet_vae_228
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854667
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json, 图片生成/图生图/Qwen2.1_漫转真_2108743375179567106.json, 图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json, "图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json", 图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json, 图片生成/图生图/洗图-文字海报 qwen image2.1_2113887500438687746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_228

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen2.1 高清修复放大 + 全能图片G脏图修复_2116089249094266882.json、图片生成/图生图/Qwen2.1_漫转真_2108743375179567106.json、图片生成/图生图/Qwen2.1_漫转真_2110186652676222978.json、图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json、图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `JjkText` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `QwenImage21Cache` —— 3/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `ImageBlur` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `RHLLMChatNode` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32.5 | 8 - 40 | 6 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1080 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 32.5，观测区间 8 - 40，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
