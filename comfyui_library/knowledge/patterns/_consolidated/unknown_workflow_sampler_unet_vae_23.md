---
name: unknown_workflow_sampler_unet_vae_23
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.77787
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json, 图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json, 图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json, 图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json, 图片生成/图生图/Qwen_image_2.1_图生_2101865996205248513.json, 图片生成/图生图/Qwen_人物四视图生成_2111240527051051009.json, 图片生成/图生图/qwen-image-1图_2102593163918667778.json, 图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json, 图片生成/图生图/qwen-image-2图_2102599002511462402.json, 图片生成/图生图/qwen-image-3图_2102665111365316610.json, 图片生成/图生图/qwen2.1 漫剧角色三视图生成_2110530131713421314.json, 图片生成/图生图/qwen2.1_漫剧角色三视图生成_2114273135901110273.json, 图片生成/图生图/qwen2.1_漫剧角色三视图生成_2115293968417247233.json, 图片生成/图生图/qwen2.1漫剧角色三视图生成｜漫剧人设资料卡一键出图_2114765300842450946.json, 图片生成/图生图/千问2.1节日表情包_2104578062582108162.json, 图片生成/图生图/千问2.1！ 多图像编辑！ 提示词自动优化！_2103396759899828226.json, 图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json, 图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json, 数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json, 数字人/数字人/千问2.1！ 多图像编辑！ 提示词自动优化！_2101851811295612929.json, 视频生成/图生视频/抠图，透明背景，Qwen2.1！_2104061025187356673.json, 视频生成/图生视频/透明背景抠图！Qwen2.1_2104454506997174273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_23

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json、图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json、图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json、图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 21/23 个有
- `ResolutionSelector` —— 21/23 个有
- `QwenImage21Cache` —— 16/23 个有
- `PreviewImage` —— 14/23 个有
- `ComfySwitchNode` —— 12/23 个有
- `CR Prompt Text` —— 9/23 个有
- `FastGroupsBypassSwitch` —— 8/23 个有
- `GetNode` —— 7/23 个有
- `JjkText` —— 7/23 个有
- `SetNode` —— 7/23 个有
- `easy showAnything` —— 7/23 个有
- `Fast Groups Bypasser (rgthree)` —— 6/23 个有
- `QwenPERewriteT8` —— 4/23 个有
- `TextCombinerTwo` —— 4/23 个有
- `GH_ImageVideoComparer` —— 3/23 个有
- `YK_LoadImageFromURL` —— 3/23 个有
- `BatchImagesNode` —— 2/23 个有
- `EmptyImage` —— 2/23 个有
- `JjkShowText` —— 1/23 个有
- `StringConcatenate` —— 1/23 个有
- `WujiUpscaler2` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 23 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 1024 | 1024 - 1560 | 21 | 89% |
| 高度 | 1024 | 904 - 1024 | 21 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，23 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1560，21 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 904 - 1024，21 个样本，取值集中（一致性 97%）
