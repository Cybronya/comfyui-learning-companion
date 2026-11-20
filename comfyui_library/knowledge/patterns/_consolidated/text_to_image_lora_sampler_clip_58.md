---
name: text_to_image_lora_sampler_clip_58
type: Text To Image
frequency: 18
level: strong
coverage: 0.921889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097150470786736129.json, 图片生成/反推提示词/Krea 2 Turbo高美学文生图｜提示词反推风格生成_2097094295093334018.json, 图片生成/反推提示词/Qwenimage2.1便捷多功能 文生图多图编辑处理工具_2113374691258888193.json, 图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json, 图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109180598479835138.json, 图片生成/图生图/Qwen Image 2.1图片清晰度增强与细节修复V2 画质提升方案_2109778326498926594.json, 图片生成/图生图/Qwen Image 2.1图生图三套夏装工作流，图生图服装展示处理工具_2108281083262488578.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工作流_2102089735173926914.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102091301226369025.json, 图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110251910526754817.json, 图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110366228245204993.json, 图片生成/图生图/Qwen-Image-2.1一键抠图｜电商产品照透明背景自动生成_2105114072894238722.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097508758569181185.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097516972694138882.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097522180136460290.json, 图片生成/文生图/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097528893510082561.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098928781699407874.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/反推提示词/Krea 2 Turbo高美学文生图｜出图质感直接拉满_2097150470786736129.json、图片生成/反推提示词/Krea 2 Turbo高美学文生图｜提示词反推风格生成_2097094295093334018.json、图片生成/反推提示词/Qwenimage2.1便捷多功能 文生图多图编辑处理工具_2113374691258888193.json、图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json、图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
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
- `CR Text` —— 16/18 个有
- `孤海注释` —— 14/18 个有
- `LoadImage` —— 10/18 个有
- `QwenImage21Cache` —— 10/18 个有
- `TextEncodeQwenImage21` —— 10/18 个有
- `ModelSamplingAuraFlow` —— 7/18 个有
- `PathchSageAttentionKJ` —— 7/18 个有
- `easy loraStack` —— 7/18 个有
- `easy loraStackApply` —— 7/18 个有
- `Image Comparer (rgthree)` —— 5/18 个有
- `SeedNode` —— 5/18 个有
- `SplitImageWithAlpha` —— 5/18 个有
- `DapaoImagePadDirectionNode` —— 1/18 个有
- `EmptyImage` —— 1/18 个有
- `LiaoQwenImage21Studio` —— 1/18 个有
- `PreviewImage` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（30/18 个样本）：Steps较低可能导致细节不足
