---
name: text_to_image_lora_sampler_clip_178
type: Text To Image
frequency: 5
level: strong
coverage: 0.9036
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json, 图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json, 图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json, 图片生成/文生图/随地大小拍手机摄影v3｜文生图出大片 手机随手拍质感拉满_2104084816416305153.json, 数字人/数字人/图像高清放大工作流｜Vosr2数字人图片画质增强_2097525104493293570.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_178

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/手机随手拍质感文生图 随地大小拍v3模拟生活化摄影_2104273094792802306.json、图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json、图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json、图片生成/文生图/随地大小拍手机摄影v3｜文生图出大片 手机随手拍质感拉满_2104084816416305153.json、数字人/数字人/图像高清放大工作流｜Vosr2数字人图片画质增强_2097525104493293570.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ResolutionSelector` —— 3/5 个有
- `CLIPLoaderGGUF` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `VOSR2ModelLoader` —— 2/5 个有
- `VOSR2Upscale` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
