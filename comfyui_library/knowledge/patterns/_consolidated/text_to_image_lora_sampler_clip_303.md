---
name: text_to_image_lora_sampler_clip_303
type: Text To Image
frequency: 7
level: strong
coverage: 0.873857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4o平替UNO多图参考一致性方案 多张输入角色一致性更强_2108710999837724674.json, 图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json, 图片生成/文生图/G-image 2文生图低价渠道版｜省钱出图照样高清_2111828809048743938.json, 图片生成/文生图/全能图片2.0文生图｜实用文字生成图片工具_2090819768029896706.json, 图片生成/文生图/全能图片G-2.0文生图｜低价渠道API专用快速出图_2096294843915005953.json, 图片生成/文生图/全能图片G2.5文生图 最强生图模型图片生成_2099905456335572994.json, 图片生成/文生图/海报分镜低成本｜全能图片G-2.0文生图API专用版_2096552763491704833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_303

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/4o平替UNO多图参考一致性方案 多张输入角色一致性更强_2108710999837724674.json、图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json、图片生成/文生图/G-image 2文生图低价渠道版｜省钱出图照样高清_2111828809048743938.json、图片生成/文生图/全能图片2.0文生图｜实用文字生成图片工具_2090819768029896706.json、图片生成/文生图/全能图片G-2.0文生图｜低价渠道API专用快速出图_2096294843915005953.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RH_RhartImageG2TextToImage` —— 6/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `easy XYInputs: Lora` —— 1/7 个有
- `easy XYInputs: PromptSR` —— 1/7 个有
- `easy XYPlotAdvanced` —— 1/7 个有
- `easy fluxLoader` —— 1/7 个有
- `easy fullkSampler` —— 1/7 个有
- `easy imageSave` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
