---
name: unknown_workflow_sampler_unet_vae_145
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6964
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json, 图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json, 图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json, 图片生成/文生图/QWen2.1文生图_2102420206202216450.json, 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_145

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json、图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json、图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json、图片生成/文生图/QWen2.1文生图_2102420206202216450.json、图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `SaveImageAdvanced` —— 3/5 个有
- `BatchImagesNode` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageCompare` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 5 | 98% |
| 高度 | 1024 | 1024 - 1920 | 5 | 70% |
| 采样步数 | 25 | 25 - 50 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 25，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
