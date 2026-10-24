---
name: text_to_image_lora_sampler_clip_152
type: Text To Image
frequency: 10
level: strong
coverage: 0.8504
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/13-尺码图生图工作流｜尺码类目专用微调，服装图出图更合身_2099550025155178497.json, 图片生成/图生图/2.0）EG-ImageNG分镜图（分镜生成出图图生图其它电商产品_2087120486856740865.json, 图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json, 图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json, 图片生成/图生图/全能图像G image2.0三图编辑 三张参考图输入改图_2105124015596728322.json, 图片生成/图生图/全能图像G image2.0多图编辑｜四到十图低价版_2095583907658944513.json, 图片生成/图生图/全能图片V2图生图｜低价渠道版海报图片处理_2095575437979246594.json, 图片生成/图生图/图生图低价渠道版｜全能图片V2海报制作处理_2095824943010369537.json, 图片生成/图生图/姿势迁移加P模特工作流，人体姿态迁移图生图电商模特方案_2103252702456279042.json, 图片生成/图生图/涂装模型车设计稿｜换装妆容风格迁移生成_2089428508715081729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/13-尺码图生图工作流｜尺码类目专用微调，服装图出图更合身_2099550025155178497.json、图片生成/图生图/2.0）EG-ImageNG分镜图（分镜生成出图图生图其它电商产品_2087120486856740865.json、图片生成/图生图/G-Image 2.0分镜图｜分镜生成出图图生图电商产品_2090100494999048194.json、图片生成/图生图/image2.0多图编辑低价版｜全能图像G四至十图处理_2095833243844169730.json、图片生成/图生图/全能图像G image2.0三图编辑 三张参考图输入改图_2105124015596728322.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
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
- `CR Text` —— 9/10 个有
- `RH_RhartImageG2ImageToImage` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `RH_LLMAPI_Pro_Node` —— 4/10 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `RH_Nano_Banana2_Image2Image` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `CR Text Replace` —— 2/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `HAIGC_SavePSD` —— 1/10 个有
- `ImageAndMaskPreview` —— 1/10 个有
- `LayerUtility: TextJoin` —— 1/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `easy imageScaleDownToSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
