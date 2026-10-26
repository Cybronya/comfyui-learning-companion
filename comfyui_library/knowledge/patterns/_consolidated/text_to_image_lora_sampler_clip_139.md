---
name: text_to_image_lora_sampler_clip_139
type: Text To Image
frequency: 12
level: strong
coverage: 0.88625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/G-image-2.5文生图极速API版｜秒级出图效率拉满_2098732116275195905.json, 图片生成/文生图/G-image-2.5文生图高品质API版｜出图质感在线_2098726914138664961.json, 图片生成/文生图/G-image-2.5文生图高品质版 文本到图像精细生成_2098294330913021954.json, 图片生成/文生图/G-image2全能真实人像文生图｜2K输出摄影级写实人像写真_2088691697495662593.json, 图片生成/文生图/G2 文生图低价版｜省币跑图更划算的文生图选择_2096890572521951233.json, 图片生成/文生图/Image-2.5九图文生图版本 批量高质量生成_2098303034546806785.json, 图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json, 图片生成/文生图/text to Image 2.0 RH性价比版全能图片G2文生图工作流_2088373457695363074.json, 图片生成/文生图/text to Image 2.0 RH性价比版文生图｜全能图片G2图片生成工作流_2088342587194302465.json, 图片生成/文生图/场景道具图单图文生图（真实感）_2106398654545358849.json, 图片生成/文生图/场景道具图批量文生图｜布景陈设素材一键出全套_2103107503109263362.json, 图片生成/文生图/真实人像2K输出｜全能图片G-image2文生图人像写真_2093778848361046017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_139

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/G-image-2.5文生图极速API版｜秒级出图效率拉满_2098732116275195905.json、图片生成/文生图/G-image-2.5文生图高品质API版｜出图质感在线_2098726914138664961.json、图片生成/文生图/G-image-2.5文生图高品质版 文本到图像精细生成_2098294330913021954.json、图片生成/文生图/G-image2全能真实人像文生图｜2K输出摄影级写实人像写真_2088691697495662593.json、图片生成/文生图/G2 文生图低价版｜省币跑图更划算的文生图选择_2096890572521951233.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `孤海注释` —— 11/12 个有
- `RH_RhartImageG2TextToImage` —— 7/12 个有
- `CR Prompt Text` —— 6/12 个有
- `PIP_StringConcatenation` —— 2/12 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 2/12 个有
- `RH_RhartImageG25SunburstTextToImage` —— 2/12 个有
- `ShowAnything|Mie` —— 2/12 个有
- `easy positive` —— 2/12 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 1/12 个有
- `TextInput` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
