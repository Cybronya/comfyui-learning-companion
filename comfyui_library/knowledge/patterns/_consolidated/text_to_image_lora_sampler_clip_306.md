---
name: text_to_image_lora_sampler_clip_306
type: Text To Image
frequency: 7
level: weak
coverage: 0.892143
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS文生图-4步出图-VOSR高清放大_2112043829208641537.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2113461455063441409.json, 图片生成/文生图/MOSS文生图加VOSR放大组合｜文生黑马出图再超分一步到位_2113522691427880962.json, 图片生成/文生图/MOSS文生图黑马VOSR放大 8步极速图像生成工具_2113703027365470209.json, 图片生成/文生图/火影人气角色雏田文生图｜一键生成动漫美少女立绘_2107648182992850946.json, 图片生成/文生图/背景图批量出图神器｜文生图一句提示词直出，场景背景素材随心换_2100476653272129538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_306

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/MOSS文生图-4步出图-VOSR高清放大_2112043829208641537.json、图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json、图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2113461455063441409.json、图片生成/文生图/MOSS文生图加VOSR放大组合｜文生黑马出图再超分一步到位_2113522691427880962.json、图片生成/文生图/MOSS文生图黑马VOSR放大 8步极速图像生成工具_2113703027365470209.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `VAELoader` —— 6/7 个有
- `VOSR2ModelLoader` —— 6/7 个有
- `VOSR2Upscale` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `MuyeTextEditOutput` —— 5/7 个有
- `SkipLayerGuidanceDiTSimple` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `孤海注释` —— 3/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `EmptyImage` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1024 | 7 | 4% |
| 高度 | 80 | 80 - 1024 | 7 | 4% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 0.6 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
