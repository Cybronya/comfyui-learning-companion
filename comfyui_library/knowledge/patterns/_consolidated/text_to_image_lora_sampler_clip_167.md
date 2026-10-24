---
name: text_to_image_lora_sampler_clip_167
type: Text To Image
frequency: 10
level: weak
coverage: 0.8934
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json, 图片生成/文生图/MJ风格工作流V2.0｜美学一键复刻_2112481146184486913.json, 图片生成/文生图/Qwen Image 2.1 透明素材生成｜文生图直出透明PNG_2112462903986180098.json, 图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json, 图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json, 图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json, 图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102103619591036930.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE工作流，文生图高质量文本到图像_2107569921352884226.json, 图片生成/文生图/Qwen_Image_2.1文生图工作流｜零门槛直出创意画面_2110761065725382658.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/MJ风格工作流V2.0_2112169962583445506.json、图片生成/文生图/MJ风格工作流V2.0｜美学一键复刻_2112481146184486913.json、图片生成/文生图/Qwen Image 2.1 透明素材生成｜文生图直出透明PNG_2112462903986180098.json、图片生成/文生图/Qwen Image 2.1一体化文生图工作流，7B模型2K高清RGBA透明直出方案_2103624543020601346.json、图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 9/10 个有
- `solarL_SaveImagesToZip` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `TextEncodeQwenImage21` —— 8/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `SaveImageAdvanced` —— 5/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ConditioningKrea2Rebalance` —— 2/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MaskToImage` —— 1/10 个有
- `SplitImageWithAlpha` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 10 | 0% |
| 高度 | 80 | 80 - 1024 | 10 | 0% |
| 采样步数 | 4 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 10 | 75% |
| 采样算法 | er_sde | - | 10 | 90% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 90%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
