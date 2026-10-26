---
name: text_to_image_lora_sampler_clip_203
type: Text To Image
frequency: 9
level: strong
coverage: 0.897444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, Image Comparer (rgthree), JjkText, KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2+Klein9B单图工作流｜图生图精修细节保留_2110758202563448834.json, 图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json, 图片生成/图生图/Klein 9B一键光影重塑专用LoRA｜图生图打光电商产品_2090096264871501826.json, 图片生成/图生图/Klein 9B专用LoRA光影重塑｜图生图打光质感重塑_2108066679426207745.json, 图片生成/图生图/Klein 9B光影重塑专用LoRA图生图｜一键打光氛围拉满_2108043104434610178.json, 图片生成/图生图/Klein 9B光影重塑｜专用LoRA图生图一键重打光_2101558105770389505.json, 图片生成/图生图/klein打光小助手｜图生图一键专业布光提升质感_2105249876488581121.json, 图片生成/图生图/一键光影重塑｜Klein 9B专用LoRA图生图打光_2089805836540538881.json, 图片生成/图生图/图生图｜Klein_9B一键溶图，双图融合测试效果实测_2099856179072692225.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX.2+Klein9B单图工作流｜图生图精修细节保留_2110758202563448834.json、图片生成/图生图/FLUX.2加Klein9B单图处理，图生图质感细节拉满_2110849332793659393.json、图片生成/图生图/Klein 9B一键光影重塑专用LoRA｜图生图打光电商产品_2090096264871501826.json、图片生成/图生图/Klein 9B专用LoRA光影重塑｜图生图打光质感重塑_2108066679426207745.json、图片生成/图生图/Klein 9B光影重塑专用LoRA图生图｜一键打光氛围拉满_2108043104434610178.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/9 个有
- `ResizeImagesByLongerEdge` —— 7/9 个有
- `AILab_ColorInput` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `ConstrainImage|pysssss` —— 2/9 个有
- `ImageLoader` —— 2/9 个有
- `JoinStrings` —— 2/9 个有
- `RMBG` —— 2/9 个有
- `JjkShowText` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
