---
name: text_to_image_upscale_lora_sampler_65
type: Text To Image
frequency: 4
level: strong
coverage: 0.7735
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一张图搞定四视图｜图生图工作流 正面侧面背面全都有_2097527695096766465.json, 图片生成/图生图/短剧人物三视图｜参考图生成正侧背角色设定图_2089309758296780801.json, 图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json, 图片生成/文生图/短剧最佳拍档画布功能，支持场景角色文生视频_2111550122223038466.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一张图搞定四视图｜图生图工作流 正面侧面背面全都有_2097527695096766465.json、图片生成/图生图/短剧人物三视图｜参考图生成正侧背角色设定图_2089309758296780801.json、图片生成/文生图/短剧最佳拍档AI创客训练营｜画布功能支持场景角色创作_2106237793725931522.json、图片生成/文生图/短剧最佳拍档画布功能，支持场景角色文生视频_2111550122223038466.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RH_RhartImageG2ImageToImage` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LayerUtility: TextJoin` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `easy imageSizeBySide` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
