---
name: text_to_image_sampler_clip_vae
type: Text To Image
frequency: 27
level: weak
coverage: 0.963704
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json, 图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json, 图片生成/文生图/boogu_image_turbo_2067441416753737730.json, 图片生成/文生图/boogu_turbo-文生图极速-人像真实感_2070712427402055682.json, 图片生成/文生图/boogu_turbo_2067856663108997122.json, 图片生成/文生图/boogu_turbo_example_2068872865654599681.json, 图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词_2069069696166612994.json, 图片生成/文生图/boogu_turbo_文生图_2068263819142590465.json, 图片生成/文生图/boogu_turbo_文生图_2068962805402923010.json, 图片生成/文生图/boogu_turbo_文生图_2069223329772429313.json, 图片生成/文生图/boogu_turbo_文生图_2069231725925978114.json, 图片生成/文生图/boogu_turbo_文生图_2071491115995455489.json, 图片生成/文生图/boogu_turbo工作流_2067417417038516225.json, 图片生成/文生图/boogu_turbo工作流含提示词_2067780518917271554.json, 图片生成/文生图/boogu_turbo文生图_2068941150962147330.json, 图片生成/文生图/boogu_turbo文生图工作流_2069287215741624322.json, 图片生成/文生图/boogu模型快速出图_2069078655669727234.json, 图片生成/文生图/ideogram4_2062708650468265986.json, 图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json, 图片生成/文生图/krea2基础文生图_2098922890111574018.json, 图片生成/文生图/krea2基础文生图_2098981510849327105.json, 图片生成/文生图/krea2基础文生图_2099657569232056322.json, 图片生成/文生图/z-image文生图工作流_2099060664231874562.json, 图片生成/文生图/z-image文生图工作流｜轻量出图响应快，日常配图随手就能出_2099545132960935937.json, 图片生成/文生图/全能图片G-image-2.5文生图高品质版｜一句话出好图，细节给足_2099479665718153217.json, 图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json, 图片生成/文生图/文生图ZImage工作流｜多段提示词同时出图神器_2100813214991863810.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json、图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json、图片生成/文生图/boogu_image_turbo_2067441416753737730.json、图片生成/文生图/boogu_turbo-文生图极速-人像真实感_2070712427402055682.json、图片生成/文生图/boogu_turbo_2067856663108997122.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 26/27 个有
- `ConditioningZeroOut` —— 22/27 个有
- `PreviewImage` —— 10/27 个有
- `LoraLoaderModelOnly` —— 8/27 个有
- `EmptyImage` —— 7/27 个有
- `JjkText` —— 4/27 个有
- `solarL_SaveImagesToZip` —— 4/27 个有
- `孤海注释` —— 4/27 个有
- `EnhancedLoadDiffusionModel` —— 1/27 个有
- `Label (rgthree)` —— 1/27 个有
- `LayerUtility: PurgeVRAM V2` —— 1/27 个有
- `ModelSamplingAuraFlow` —— 1/27 个有
- `PromptBatchQueue` —— 1/27 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 27 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 27 | 9% |
| 采样算法 | lcm | - | 27 | 52% |
| 调度器 | sgm_uniform | - | 27 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 1024 | 80 - 1536 | 27 | 59% |
| 高度 | 1280 | 80 - 2048 | 27 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，27 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，27 个样本，取值分散，一致性仅 9%
- 采样算法 最常用 lcm，27 个样本，一致性 52%
- 调度器 最常用 sgm_uniform，27 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1536，27 个样本
- 高度 中位数 1280，观测区间 80 - 2048，27 个样本
- 高发问题（23/27 个样本）：Steps较低可能导致细节不足
