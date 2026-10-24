---
name: image_to_image_lora_sampler_unet_10
type: Image To Image
frequency: 25
level: strong
coverage: 0.88832
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI漫剧参考图生四视图工作流_2097324354634862593.json, 图片生成/图生图/FZ-MinimaxH3-krea2参考图生成四视图_2096847232858415105.json, 图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流_2086448288496177153.json, 图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流【短剧必备】_2088923554007048194.json, 图片生成/图生图/KREA-2-EDIT-Two-image- 多图参考生新图V2_2102619986266251266.json, 图片生成/图生图/KREA-2-EDIT-Two-image- 多图编辑工作流_2079959470469378049.json, 图片生成/图生图/Krea2 角色设定表（四视图）-zip_2086873606709145602.json, 图片生成/图生图/Krea2 角色设定表（四视图）_2083733558660780033.json, 图片生成/图生图/Krea2 角色资产一致性生图（四视图）_2084820992232345602.json, 图片生成/图生图/Krea2 角色（四视图）_2089596718005444609.json, 图片生成/图生图/Krea2 角色（四视图）_2100871748366462977.json, 图片生成/图生图/Krea2 角色（四视图）_2103015116215242753.json, 图片生成/图生图/Krea2 资产库角色（三视图_新版）_解决远景脸崩坏_2095060849907036162.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2083808615709892610.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2093933329925103618.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2094677282794332162.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2094699092713754626.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2095072638539493378.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2096838930321723393.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2098207233946509314.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2105196770774052865.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2110253402931421186.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2112439275240386561.json, 图片生成/图生图/Krea2 资产库角色（四视图）_2112727576572686338.json, 图片生成/图生图/Krea2_角色设定表四视图_2087388265870614530.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/AI漫剧参考图生四视图工作流_2097324354634862593.json、图片生成/图生图/FZ-MinimaxH3-krea2参考图生成四视图_2096847232858415105.json、图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流_2086448288496177153.json、图片生成/图生图/KREA-2-EDIT-One-image-V2 单图编辑工作流【短剧必备】_2088923554007048194.json、图片生成/图生图/KREA-2-EDIT-Two-image- 多图参考生新图V2_2102619986266251266.json…）

- **类型**：Image To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
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

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 23/25 个有
- `ImageResizeKJv2` —— 21/25 个有
- `PreviewImage` —— 21/25 个有
- `AddLabel` —— 19/25 个有
- `ImageConcatMulti` —— 19/25 个有
- `ImageScaleBy` —— 4/25 个有
- `ResizeImageMaskNode` —— 4/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `Textbox` —— 2/25 个有
- `HAIGC_SaveImagesToZip` —— 1/25 个有
- `JjkText` —— 1/25 个有
- `solarL_SaveImagesToZip` —— 1/25 个有
- `孤海注释` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 25 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 100% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，25 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 100%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
