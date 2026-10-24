---
name: text_to_image_lora_sampler_clip_293
type: Text To Image
frequency: 6
level: strong
coverage: 0.5965
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, JoinStringMulti, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, RHHiddenNodes, RH_RhartImageG2ImageToImage, RH_RhartImageG2OfficialImageToImage, SaveImage, ShowText|pysssss, TextSplitByDelimiterEnhanced, UNETLoader, VAEDecode, VAELoader, easy int, easy promptConcat, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json, 图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json, 图片生成/图生图/一键生成电商主图｜平面设计图生图商品展示直出_2092344213185851393.json, 图片生成/图生图/电商主图一键生成 AI产品图快速制作批量出图神器_2098285412715417601.json, 图片生成/图生图/电商主图一键生成｜图生图平面设计电商产品出图_2092595881425063937.json, 视频生成/图生视频/短剧漫剧人物一致分镜衔接｜Minimax H3长视频导演台_2092708059238977537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_293

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/G-image-2.5产品图一键生成电商详情页_2098279391313883138.json、图片生成/图生图/G-image-2.5详情页出图，电商图生图排版利器_2112338628948094977.json、图片生成/图生图/一键生成电商主图｜平面设计图生图商品展示直出_2092344213185851393.json、图片生成/图生图/电商主图一键生成 AI产品图快速制作批量出图神器_2098285412715417601.json、图片生成/图生图/电商主图一键生成｜图生图平面设计电商产品出图_2092595881425063937.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `ShowText|pysssss`
- `TextSplitByDelimiterEnhanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy promptConcat`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RHLLMChatNode` —— 4/6 个有
- `RH_RhartImageG25FlareImageToImage` —— 3/6 个有
- `RH_RhartImageG25SunburstImageToImage` —— 3/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有

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
