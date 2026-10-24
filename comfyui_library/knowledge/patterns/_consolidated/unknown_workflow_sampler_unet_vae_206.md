---
name: unknown_workflow_sampler_unet_vae_206
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8896
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/真2K 白底图_1979202132073156610.json, 图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json, 图片生成/图生图/（短剧）人物3视图_2111246118960062466.json, 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json, 数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_206

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/真2K 白底图_1979202132073156610.json、图片生成/图生图/自用qwen_image_2.1_image_edit接超分放大工作流_2102129332872372226.json、图片生成/图生图/（短剧）人物3视图_2111246118960062466.json、图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json、数字人/数字人/（8步lora）Qwen Image 2.1 PE 图像编辑_2104628708102467585.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ComfySwitchNode` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `QwenPERewriteT8` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 25 | 8 - 40 | 5 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 8 - 40，5 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
