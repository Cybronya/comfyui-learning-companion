---
name: unknown_workflow_sampler_unet_vae_94
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8748
common_nodes: [CLIPLoader, CR Prompt Text, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2109541250159435778.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112365438872154113.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 汉服美学_2110739133755912194.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_7步_亚洲人像文生图_2114257373773778946.json, 图片生成/文生图/Qwen-Image-2.1-Turbo_汉服美学_2114258449633726466.json, 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json, 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json, 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_94

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Fix修复图像编辑_2103711535771250690.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2109541250159435778.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112360202447187970.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步 亚洲人像文生图_2112365438872154113.json、图片生成/文生图/Qwen-Image-2.1-Turbo 汉服美学_2110739133755912194.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `QwenImage21Cache` —— 9/10 个有
- `QwenPERewriteT8` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `Color Grading JK` —— 6/10 个有
- `LoadImage` —— 6/10 个有
- `PreviewImage` —— 4/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `EmptyImage` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `APG` —— 1/10 个有
- `FreSca` —— 1/10 个有
- `JWDatetimeString` —— 1/10 个有
- `Lora Loader Stack (rgthree)` —— 1/10 个有
- `SeedNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1200 | 10 | 95% |
| 高度 | 1024 | 1024 - 1600 | 10 | 84% |
| 采样步数 | 8 | 7 - 40 | 10 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 10 | 50% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1200，10 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1600，10 个样本，取值集中（一致性 84%）
- 采样步数 中位数 8，观测区间 7 - 40，10 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
