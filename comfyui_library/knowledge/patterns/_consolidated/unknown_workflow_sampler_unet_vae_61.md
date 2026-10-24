---
name: unknown_workflow_sampler_unet_vae_61
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.573846
common_nodes: [Any Switch (rgthree), CLIPLoader, CR Prompt Text, EmptyLatentImage, KSampler, LoadImage, PathchSageAttentionKJ, PixaromaGroupSwitch, QwenImage21Cache, QwenPERewriteT8, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json, 图片生成/反推提示词/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json, 图片生成/图生图/Qwen Image 2.1 图像编辑工作流V1.0（2026开源最强模型）_2107740009477533698.json, 图片生成/图生图/Qwen Image 2.1 图像编辑（2026开源最强模型）V1.0_2107721379499036673.json, 图片生成/图生图/Qwen Image 2.1 图像编辑（2026开源最强模型）_2107721422918475777.json, 图片生成/图生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754.json, 图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流V1.0_2110537442909581314.json, 图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2110645691214286849.json, 图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218.json, 图片生成/图生图/多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057.json, 图片生成/文生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流_2108147300043419649.json, 图片生成/文生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流_2108160778015698945.json, 图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_61

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json、图片生成/反推提示词/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json、图片生成/图生图/Qwen Image 2.1 图像编辑工作流V1.0（2026开源最强模型）_2107740009477533698.json、图片生成/图生图/Qwen Image 2.1 图像编辑（2026开源最强模型）V1.0_2107721379499036673.json、图片生成/图生图/Qwen Image 2.1 图像编辑（2026开源最强模型）_2107721422918475777.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 13 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PixaromaGroupSwitch`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 12/13 个有
- `Fast Bypasser (rgthree)` —— 12/13 个有
- `GetNode` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/13 个有
- `LoraLoaderModelOnly` —— 12/13 个有
- `Mute / Bypass Repeater (rgthree)` —— 12/13 个有
- `ResolutionSelector` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `ShowText|pysssss` —— 12/13 个有
- `Fast Groups Muter (rgthree)` —— 11/13 个有
- `PixaromaLabel` —— 11/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `PixaromaResolution` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `VRAM_Debug` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 13 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1024 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
