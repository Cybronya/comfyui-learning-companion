---
name: unknown_workflow_sampler_unet_vae_106
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.601714
common_nodes: [Any Switch (rgthree), CLIPLoader, CR Prompt Text, CR Text Concatenate, EmptyLatentImage, KSampler, LoadImage, PathchSageAttentionKJ, PixaromaGroupSwitch, PixaromaLabel, QwenImage21Cache, QwenPERewriteT8, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json, 图片生成/反推提示词/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json, 图片生成/图生图/2103948614040113153.json, 图片生成/图生图/2103948729811300354.json, 图片生成/文生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流_2108147300043419649.json, 图片生成/文生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流_2108160778015698945.json, 图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_106

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json、图片生成/反推提示词/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json、图片生成/图生图/2103948614040113153.json、图片生成/图生图/2103948729811300354.json、图片生成/文生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流_2108147300043419649.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PixaromaGroupSwitch`
- `PixaromaLabel`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `Fast Groups Muter (rgthree)` —— 4/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `PixaromaResolution` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `VRAM_Debug` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 7 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Fast Bypasser (rgthree)、Mute / Bypass Repeater (rgthree)、CR Prompt Text、LayerUtility: ImageScaleByAspectRatio V2
