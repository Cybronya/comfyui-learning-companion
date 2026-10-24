---
name: unknown_workflow_sampler_unet_vae_74
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.859917
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json, 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json, 图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json, 图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json, 图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json, 图片生成/图生图/qwen-image-1图_2102593163918667778.json, 图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json, 图片生成/图生图/qwen-image-2图_2102599002511462402.json, 图片生成/图生图/qwen-image-3图_2102665111365316610.json, 图片生成/图生图/qwen_image_2_1_图像编辑_2101844068895641601.json, 图片生成/图生图/qwen_image_2_1_移除背景_2102572577544818689.json, 图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_74

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json、图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json、图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json、图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json、图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 10/12 个有
- `QwenImage21Cache` —— 9/12 个有
- `ResolutionSelector` —— 8/12 个有
- `ComfySwitchNode` —— 7/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `YK_LoadImageFromURL` —— 3/12 个有
- `ImageCompare` —— 2/12 个有
- `WujiCleaner` —— 2/12 个有
- `WujiUpscaler2` —— 2/12 个有
- `QwenImage21SageAttentionT8` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 12 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 1024 - 1280 | 10 | 93% |
| 高度 | 1024 | 720 - 1024 | 10 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1280，10 个样本，取值集中（一致性 93%）
- 高度 中位数 1024，观测区间 720 - 1024，10 个样本，取值集中（一致性 91%）
