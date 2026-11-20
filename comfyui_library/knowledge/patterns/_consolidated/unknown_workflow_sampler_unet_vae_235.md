---
name: unknown_workflow_sampler_unet_vae_235
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.62825
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json, 图片生成/图生图/qwen image 2.1 编辑_2101987550209593345.json, 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_235

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json、图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json、图片生成/图生图/qwen image 2.1 编辑_2101987550209593345.json、图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `PreviewAny` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 50 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1600 | 4 | 79% |
| 高度 | 1024 | 1024 - 2400 | 4 | 56% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1600，4 个样本
- 高度 中位数 1024，观测区间 1024 - 2400，4 个样本
