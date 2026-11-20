---
name: text_to_image_lora_sampler_clip_420
type: Text To Image
frequency: 5
level: strong
coverage: 0.898
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/宫崎骏风格一键转换｜Qwen-Image-Edit文生图动漫_2095509841522544642.json, 图片生成/文生图/生图模型天花板｜谷歌🍌2文生图图生图双修_2096619590288756738.json, 图片生成/文生图/谷歌最强生图模型2｜文生图图生图双模式生成_2096366087892979714.json, 平台全量/分镜生成器｜赛博玄幻修仙者系列，中国风动漫分镜自动出_2099930833380528130.json, 平台全量/文生图图生图双修｜赛博玄幻修仙者，中国风CG幻想大片_2099927123455733761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_420

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/宫崎骏风格一键转换｜Qwen-Image-Edit文生图动漫_2095509841522544642.json、图片生成/文生图/生图模型天花板｜谷歌🍌2文生图图生图双修_2096619590288756738.json、图片生成/文生图/谷歌最强生图模型2｜文生图图生图双模式生成_2096366087892979714.json、平台全量/分镜生成器｜赛博玄幻修仙者系列，中国风动漫分镜自动出_2099930833380528130.json、平台全量/文生图图生图双修｜赛博玄幻修仙者，中国风CG幻想大片_2099927123455733761.json）

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
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `TextEncodeQwenImageEdit` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
