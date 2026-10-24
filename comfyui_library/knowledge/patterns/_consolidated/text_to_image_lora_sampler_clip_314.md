---
name: text_to_image_lora_sampler_clip_314
type: Text To Image
frequency: 6
level: strong
coverage: 0.781667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物换脸1.0.1版｜高质量图生图脸部替换生成_2095935921358204930.json, 图片生成/图生图/全能图片 G-Image-2.0｜人物面部三视图高清直出｜图生图_2096889065525309441.json, 图片生成/图生图/全能图片2.0_2k高清版｜图生图画质细节双在线_2105254608422658050.json, 图片生成/图生图/全能图片2.0工作流，图生图高质量图像处理方案_2107521089378283521.json, 图片生成/图生图/全能图片G-2.0图生图低价渠道高性价比出图方案_2104821488074444802.json, 图片生成/图生图/美女换装1.0.1版｜RH2服装替换图生图生成_2096334228534419457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_314

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/人物换脸1.0.1版｜高质量图生图脸部替换生成_2095935921358204930.json、图片生成/图生图/全能图片 G-Image-2.0｜人物面部三视图高清直出｜图生图_2096889065525309441.json、图片生成/图生图/全能图片2.0_2k高清版｜图生图画质细节双在线_2105254608422658050.json、图片生成/图生图/全能图片2.0工作流，图生图高质量图像处理方案_2107521089378283521.json、图片生成/图生图/全能图片G-2.0图生图低价渠道高性价比出图方案_2104821488074444802.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

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
- `PreviewImage` —— 4/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 4/6 个有
- `RH_RhartImageG2ImageToImage` —— 4/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `DF_Text_Box` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `忽略多组孤海` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ttN text` —— 1/6 个有

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
