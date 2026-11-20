---
name: text_to_image_lora_sampler_clip_353
type: Text To Image
frequency: 6
level: strong
coverage: 0.875833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/小红书抖音种草唯美照片 AI创意摄影集成升级_2098111917645713410.json, 图片生成/文生图/抖音小红书种草专用｜唯美照片文生图V2.0_2090528858159271937.json, 图片生成/文生图/抖音小红书种草专用｜文生图V2.0唯美照片创作_2090823875012685825.json, 图片生成/文生图/抖音小红书种草专用｜文生图V2.0唯美照片生成_2094309486575050753.json, 图片生成/文生图/生图模型天花板｜谷歌🍌2文生图图生图双修_2096619590288756738.json, 图片生成/文生图/谷歌最强生图模型2｜文生图图生图双模式生成_2096366087892979714.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_353

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/小红书抖音种草唯美照片 AI创意摄影集成升级_2098111917645713410.json、图片生成/文生图/抖音小红书种草专用｜唯美照片文生图V2.0_2090528858159271937.json、图片生成/文生图/抖音小红书种草专用｜文生图V2.0唯美照片创作_2090823875012685825.json、图片生成/文生图/抖音小红书种草专用｜文生图V2.0唯美照片生成_2094309486575050753.json、图片生成/文生图/生图模型天花板｜谷歌🍌2文生图图生图双修_2096619590288756738.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `DF_Text_Box` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `workflow>儿童AI摄影` —— 4/6 个有
- `workflow>创意图片处理` —— 4/6 个有
- `workflow>宠物守护神AI摄影` —— 4/6 个有
- `workflow>真实照片处理` —— 4/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
