---
name: text_to_image_sampler_clip_unet_147
type: Text To Image
frequency: 4
level: strong
coverage: 0.8755
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json, 图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json, 图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json, 图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json、图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json、图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json、图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `CR Prompt Text` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `Int` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 720 - 1024 | 4 | 88% |
| 高度 | 1280 | 1280 - 1280 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 720 - 1024，4 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1280 - 1280，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
