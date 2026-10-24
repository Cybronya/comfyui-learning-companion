---
name: text_to_image_lora_sampler_clip_132
type: Text To Image
frequency: 11
level: strong
coverage: 0.812727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 PE提示词强化｜官方优化版｜短句也能写出大片感_2102588489098424321.json, 图片生成/图生图/Qwen Image 2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2102817681568256001.json, 图片生成/图生图/RH全能图片PRO官方稳定版｜图生图不出幺蛾子，海报制作靠得住_2099536861491453954.json, 图片生成/图生图/SeedVR2 7B分块渲染8K放大｜无损高清增强_2098764691500785665.json, 图片生成/图生图/image2自用稳定版_2085450601940480001.json, 图片生成/图生图/九宫格角色多动作生成｜三视图参考角色表演图生图_2095588740323438593.json, 图片生成/图生图/九宫格角色部件生成｜三视图参考角色设计图生图_2095585736509714434.json, 图片生成/图生图/头像特写角色多表情九宫格｜三视图参考角色设计_2095590124624109570.json, 图片生成/图生图/宠物+坐骑生成器九宫格｜带参考图角色设计_2095254229475745794.json, 图片生成/图生图/角色多动作九宫格｜带角色图参考动作设计生成_2095249943421345794.json, 图片生成/图生图/角色部件九宫格生成｜带角色图参考三视图可用_2095247137901731842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 PE提示词强化｜官方优化版｜短句也能写出大片感_2102588489098424321.json、图片生成/图生图/Qwen Image 2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2102817681568256001.json、图片生成/图生图/RH全能图片PRO官方稳定版｜图生图不出幺蛾子，海报制作靠得住_2099536861491453954.json、图片生成/图生图/SeedVR2 7B分块渲染8K放大｜无损高清增强_2098764691500785665.json、图片生成/图生图/image2自用稳定版_2085450601940480001.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `SaveImage` —— 9/11 个有
- `PreviewAny` —— 8/11 个有
- `RH_RhartImageG2OfficialImageToImage` —— 7/11 个有
- `1hew_ImageGridSplit` —— 6/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `RHLLMChatNode` —— 6/11 个有
- `PreviewImage` —— 2/11 个有
- `QwenPECanvasT8` —— 2/11 个有
- `QwenPERewriteT8` —— 2/11 个有
- `SaveText` —— 2/11 个有
- `PrimitiveInt` —— 1/11 个有
- `RH_RhartImageNProOfficialEdit` —— 1/11 个有
- `SeedVR2TilingUpscaler` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
