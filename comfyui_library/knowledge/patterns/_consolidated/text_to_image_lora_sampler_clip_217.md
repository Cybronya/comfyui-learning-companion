---
name: text_to_image_lora_sampler_clip_217
type: Text To Image
frequency: 9
level: strong
coverage: 0.900667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/角色三视图Qwen Image 2.1工作流，图生图角色设计处理工具_2107934196995018753.json, 图片生成/图生图/越南饰品海报快速生成｜图生图东南亚风格电商海报一步到位_2099162981023182849.json, 图片生成/图生图/软装搭配分析工作流 室内设计方案辅助生成_2105427749509881858.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json, 图片生成/文生图/BF16精度Qwen Image 2.1文生图，小字不崩高质量文字渲染工作流_2102872573246791681.json, 图片生成/文生图/BF16精度Qwen_Image_2.1文生图，小字不崩高质量文字渲染工作流_2105503929613250561.json, 图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json, 图片生成/文生图/MossImage文生分镜图V1.0｜短剧漫画分镜批量出图神器_2112906492759334914.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_217

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/角色三视图Qwen Image 2.1工作流，图生图角色设计处理工具_2107934196995018753.json、图片生成/图生图/越南饰品海报快速生成｜图生图东南亚风格电商海报一步到位_2099162981023182849.json、图片生成/图生图/软装搭配分析工作流 室内设计方案辅助生成_2105427749509881858.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `LoadImage` —— 5/9 个有
- `RH_RhartImageG2ImageToImage` —— 4/9 个有
- `ResolutionSelector` —— 4/9 个有
- `ImageStitch` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `SaveImageAdvanced` —— 3/9 个有
- `TextEncodeQwenImage21` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `MOSSImagePromptEnhancerT8` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `QwenImage21Cache` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
