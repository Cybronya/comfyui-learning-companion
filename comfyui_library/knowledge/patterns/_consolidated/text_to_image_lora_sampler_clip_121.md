---
name: text_to_image_lora_sampler_clip_121
type: Text To Image
frequency: 12
level: strong
coverage: 0.88825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json, 图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json, 图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101365555285544962.json, 图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101755378726948865.json, 图片生成/文生图/G-image 2文生图低价渠道版｜省钱出图照样高清_2111828809048743938.json, 图片生成/文生图/G-image-2.5文生图极速API版｜秒级出图效率拉满_2098732116275195905.json, 图片生成/文生图/G-image2全能真实人像文生图｜2K输出摄影级写实人像写真_2088691697495662593.json, 图片生成/文生图/G2 文生图低价版｜省币跑图更划算的文生图选择_2096890572521951233.json, 图片生成/文生图/flux3_klein文生图方案，高质量创意出图轻松搞定_2111539683925774338.json, 图片生成/文生图/flux3_klein文生图极简版｜简洁流出一手好图_2111317480894455809.json, 图片生成/文生图/真实人像2K输出｜全能图片G-image2文生图人像写真_2093778848361046017.json, 图片生成/文生图/遇见AI Moss image 文生图｜8步加速基础流省时_2112458024404209665.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json、图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json、图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101365555285544962.json、图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101755378726948865.json、图片生成/文生图/G-image 2文生图低价渠道版｜省钱出图照样高清_2111828809048743938.json…）

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2TextToImage` —— 7/12 个有
- `EmptyFlux2LatentImage` —— 4/12 个有
- `PIP_StringConcatenation` —— 4/12 个有
- `ResolutionSelector` —— 4/12 个有
- `easy positive` —— 4/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 1/12 个有
- `Seed (rgthree)` —— 1/12 个有
- `SkipLayerGuidanceDiTSimple` —— 1/12 个有
- `TextInput` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
