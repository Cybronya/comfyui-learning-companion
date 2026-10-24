---
name: unknown_workflow_sampler_checkpoint_vae_15
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.969667
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像编辑-Qwen-Edit-AIO加速多合一_1977715091086921729.json, 图片生成/图生图/图像编辑-Qwen-Edit-AIO加速多合一_2074762908281692162.json, 图片生成/图生图/手办创建_2111833298065514498.json, 图片生成/图生图/手办创建图生图_2112861789900853249.json, 图片生成/图生图/手办创建图生图_2112878742635900929.json, 图片生成/图生图/换装 人物换装 一键换装 女装带货  超清放大修复 电商模特换装_2051513484009066497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图像编辑-Qwen-Edit-AIO加速多合一_1977715091086921729.json、图片生成/图生图/图像编辑-Qwen-Edit-AIO加速多合一_2074762908281692162.json、图片生成/图生图/手办创建_2111833298065514498.json、图片生成/图生图/手办创建图生图_2112861789900853249.json、图片生成/图生图/手办创建图生图_2112878742635900929.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 50% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 744 | 720 - 768 | 6 | 97% |
| 高度 | 1024 | 768 - 1280 | 6 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 744，观测区间 720 - 768，6 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 768 - 1280，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
