---
name: unknown_workflow_sampler_unet_vae_120
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.756125
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, Seed (rgthree), Text Multiline, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XinbaoImageStandardizer]
problems: []
missing: []
members: [图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json, 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json, 图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json, 图片生成/图生图/Qwen Image2.1，精准抠图，移除遮挡_2104438752583184386.json, 图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105585484234838018.json, 图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2108372055283560450.json, 图片生成/图生图/qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810.json, 图片生成/图生图/千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_120

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json、图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡_2104462379441549314.json、图片生成/图生图/Qwen Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2104044741108260865.json、图片生成/图生图/Qwen Image2.1，精准抠图，移除遮挡_2104438752583184386.json、图片生成/图生图/Qwen_Image2.1强化抠图，精准抠图，移除遮挡，完美PNG通道_2105585484234838018.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XinbaoImageStandardizer`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `QwenPERewriteT8` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `忽略多组孤海` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `StringToAnyNode` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `easy boolean` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1024 | 1024 - 1024 | 8 | 100% |
| 采样步数 | 25 | 25 - 25 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
