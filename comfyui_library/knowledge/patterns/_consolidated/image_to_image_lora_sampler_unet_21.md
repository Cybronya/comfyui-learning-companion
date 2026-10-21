---
name: image_to_image_lora_sampler_unet_21
type: Image To Image
frequency: 5
level: strong
coverage: 0.8018
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json, 数字人/数字人/Krea2 人物定妆照_2092034511797309441.json, 数字人/数字人/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2099860117662560257.json, 数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json, 视频生成/图生视频/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100042152431669249.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json、数字人/数字人/Krea2 人物定妆照_2092034511797309441.json、数字人/数字人/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2099860117662560257.json、数字人/数字人/MiniMaxH3辅助四视图生成-k2_2094815406618927106.json、视频生成/图生视频/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100042152431669249.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
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
- `PreviewImage` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
