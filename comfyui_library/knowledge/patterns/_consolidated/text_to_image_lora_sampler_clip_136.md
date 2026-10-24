---
name: text_to_image_lora_sampler_clip_136
type: Text To Image
frequency: 11
level: strong
coverage: 0.876545
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/角色四视图一键生成｜Krea2图生图角色设计_2090852196056387586.json, 图片生成/图生图/角色四视图一键生成｜krea2图生图设计_2095816777677758466.json, 图片生成/图生图/角色四视图辅助生成工作流｜图生图人物设计制作_2097122293725097986.json, 图片生成/图生图/角色四视图｜Krea2图生图角色一致性生成_2089833975018778626.json, 图片生成/图生图/资产库角色四视图生成｜Krea2角色一致性出图_2095502773403086849.json, 图片生成/图生图/资产库角色四视图｜Krea2分镜出图一致性生成_2095113857382567937.json, 图片生成/图生图/辅助四视图生成流｜MiniMaxH3 k2图生图角色设计_2091301465301274626.json, 数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json, 数字人/数字人/krea_quadview_i2i 四视图生图｜人物角色数字人多视角_2096909828131213314.json, 数字人/数字人/krea_quadview_i2i四视图编辑｜人物角色数字人图生图_2096703736772128769.json, 视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/角色四视图一键生成｜Krea2图生图角色设计_2090852196056387586.json、图片生成/图生图/角色四视图一键生成｜krea2图生图设计_2095816777677758466.json、图片生成/图生图/角色四视图辅助生成工作流｜图生图人物设计制作_2097122293725097986.json、图片生成/图生图/角色四视图｜Krea2图生图角色一致性生成_2089833975018778626.json、图片生成/图生图/资产库角色四视图生成｜Krea2角色一致性出图_2095502773403086849.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 10/11 个有
- `PreviewImage` —— 8/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `AddLabel` —— 5/11 个有
- `GetImageSize` —— 5/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `GetNode` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `ImagePadForOutpaint` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
