---
name: text_to_image_lora_sampler_clip_259
type: Text To Image
frequency: 7
level: strong
coverage: 0.829714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110251910526754817.json, 图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110366228245204993.json, 图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json, 图片生成/图生图/Qwen Image 2.1角色资产四视图极速版，4步8步加速图生图方案_2103944948725927937.json, 图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json, 图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_259

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110251910526754817.json、图片生成/图生图/Qwen Image 2.1清晰度增强V2 细节修复画质提升_2110366228245204993.json、图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json、图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json、图片生成/图生图/Qwen Image 2.1角色资产四视图极速版，4步8步加速图生图方案_2103944948725927937.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `SeedNode` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `SplitImageWithAlpha` —— 2/7 个有
- `easy int` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（13/7 个样本）：Steps较低可能导致细节不足
