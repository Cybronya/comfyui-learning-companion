---
name: text_to_image_lora_sampler_clip_154
type: Text To Image
frequency: 6
level: strong
coverage: 0.869
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json, 图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json, 数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099178316405239810.json, 数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099546664741720066.json, 数字人/数字人/全能图像Pro玩法宝典｜提示词合集一次拿全，电商主图详情页直接复刻_2099504783659986945.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/服装模特姿势复刻全能PRO官方稳定版工作流，服装展示图生图工具_2107203791136321538.json、图片生成/图生图/服装模特换装多图融合官方稳定版工作流，服装展示图生图处理工具_2107211199963295745.json、图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json、数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099178316405239810.json、数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099546664741720066.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `GetImageSize+` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `RH_Nano_Banana2_Image2Image` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_RhartImageNProOfficialEdit` —— 2/6 个有
- `OpenposePreprocessor` —— 1/6 个有
- `RH_RhartImageG25SunburstTextToImage` —— 1/6 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/6 个有

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
