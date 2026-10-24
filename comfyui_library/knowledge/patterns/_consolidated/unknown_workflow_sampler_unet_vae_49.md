---
name: unknown_workflow_sampler_unet_vae_49
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.848857
common_nodes: [CLIPLoader, ComfySwitchNode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json, 图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json, 图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json, 图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json, 图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json, 图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json, 图片生成/图生图/Qwen image 2.1 人物替换 _ 姿势复刻_2109882087112269826.json, 图片生成/图生图/Qwen image 2.1 换装_2109875920243871745.json, 图片生成/图生图/Qwen-Image-2.1-Turbo 多图像编辑（8步快速出图）_2108954948208775169.json, 图片生成/文生图/Qwen 2.1 文生图（4步加速）_2102704314325225473.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102235294379630593.json, 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2102793929358929921.json, 图片生成/文生图/Qwen Image 2.1 文生图-PE版_2104456492933013506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/QWEN-IMAGE-2.1多参考图生成图片_2110329648222662657.json、图片生成/图生图/QWEN2.1_图像编辑工作流_2102050374931804161.json、图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json、图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json、图片生成/图生图/Qwen Image 2.1 Turbo 人物角色替换_2108901380495859713.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `KSampler`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `SaveImage` —— 13/14 个有
- `LoadImage` —— 9/14 个有
- `easy showAnything` —— 8/14 个有
- `CR Prompt Text` —— 7/14 个有
- `QwenPERewriteT8` —— 7/14 个有
- `easy cleanGpuUsed` —— 7/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `Image Comparer (rgthree)` —— 5/14 个有
- `CR Text` —— 4/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/14 个有
- `ImageConcanate` —— 3/14 个有
- `Latent Switch (JPS)` —— 3/14 个有
- `EmptySD3LatentImage` —— 1/14 个有
- `QwenImagePromptOptimizer` —— 1/14 个有
- `easy imageSave` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 40 | 14 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1024 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 40，14 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
