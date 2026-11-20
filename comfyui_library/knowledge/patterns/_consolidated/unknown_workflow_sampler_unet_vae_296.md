---
name: unknown_workflow_sampler_unet_vae_296
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7465
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json, 图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json, 图片生成/文生图/QWen2.1文生图_2102420206202216450.json, 平台全量/qwen-image2.1图像编辑_2115372324064157697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_296

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/多图换装丨Qwen Image 2.1丨服饰搭配·姿态参考_2113116714740305921.json、图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json、图片生成/文生图/QWen2.1文生图_2102420206202216450.json、平台全量/qwen-image2.1图像编辑_2115372324064157697.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextInputNode` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1056 | 1024 - 1152 | 4 | 95% |
| 高度 | 1472 | 1024 - 2016 | 4 | 68% |
| 采样步数 | 32.5 | 25 - 50 | 4 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1056，观测区间 1024 - 1152，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1472，观测区间 1024 - 2016，4 个样本
- 采样步数 中位数 32.5，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
