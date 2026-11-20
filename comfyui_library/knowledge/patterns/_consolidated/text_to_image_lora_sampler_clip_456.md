---
name: text_to_image_lora_sampler_clip_456
type: Text To Image
frequency: 4
level: strong
coverage: 0.83425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像扩展外补不改变原图大版｜画面外扩补全场景构图_2113551762983575554.json, 图片生成/图生图/图像扩展外补不改变原图，图生图扩图大版方案_2111253172189753345.json, 图片生成/图生图/图像扩展外补大版 不改变原图扩图处理生成工具_2113714025287737346.json, 图片生成/图生图/追色图生图工作流｜色调迁移统一风格｜组图配色一步到位_2101933327929405441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_456

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图像扩展外补不改变原图大版｜画面外扩补全场景构图_2113551762983575554.json、图片生成/图生图/图像扩展外补不改变原图，图生图扩图大版方案_2111253172189753345.json、图片生成/图生图/图像扩展外补大版 不改变原图扩图处理生成工具_2113714025287737346.json、图片生成/图生图/追色图生图工作流｜色调迁移统一风格｜组图配色一步到位_2101933327929405441.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FillMaskWithColor` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `ImageScale` —— 3/4 个有
- `InpaintCrop` —— 3/4 个有
- `InpaintStitch` —— 3/4 个有
- `RH_RhartImageNNb21ImageToImage` —— 3/4 个有
- `ImitationHueNode` —— 1/4 个有

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
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
