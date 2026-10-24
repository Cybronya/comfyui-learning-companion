---
name: unknown_workflow_unet_vae_7
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.770125
common_nodes: [CLIPLoader, EmptyLatentImage, LoadImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json, 图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json, 图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json, 图片生成/图生图/QWen2.1图像编辑_2102423497988460545.json, 图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json, 图片生成/图生图/Qwen Image 2.1-PE-图像编辑-加速版_2108817312836055042.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json、图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json、图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `KSampler` —— 7/8 个有
- `ResolutionSelector` —— 6/8 个有
- `TextGenerate` —— 6/8 个有
- `BatchImagesNode` —— 5/8 个有
- `PreviewAny` —— 4/8 个有
- `SaveImageAdvanced` —— 4/8 个有
- `ImageCompare` —— 3/8 个有
- `JjkText` —— 3/8 个有
- `CFGGuider` —— 2/8 个有
- `KSamplerSelect` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `RandomNoise` —— 2/8 个有
- `SamplerCustomAdvanced` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `RH_QwenImagePromptEnhancer` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 8 | 97% |
| 高度 | 1024 | 1024 - 1920 | 8 | 69% |
| 采样步数 | 25 | 8 - 50 | 7 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，8 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 25，观测区间 8 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
