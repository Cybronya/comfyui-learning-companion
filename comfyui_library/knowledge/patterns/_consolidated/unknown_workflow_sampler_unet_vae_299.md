---
name: unknown_workflow_sampler_unet_vae_299
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81075
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, LoadImage, PrimitiveInt, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json, 图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json, 平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json, 平台全量/人物换装&换背景&图像编辑_2112724441338834946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_299

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json、图片生成/文生图/图片换人丨Qwen Image 2.1丨双图替换·保留姿态_2112093115338280962.json、平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json、平台全量/人物换装&换背景&图像编辑_2112724441338834946.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `PrimitiveInt`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy imageConcat` —— 3/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `SplitImageWithAlpha` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 992 | 960 - 1024 | 4 | 97% |
| 高度 | 1152 | 1024 - 1280 | 4 | 89% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 992，观测区间 960 - 1024，4 个样本，取值集中（一致性 97%）
- 高度 中位数 1152，观测区间 1024 - 1280，4 个样本，取值集中（一致性 89%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
