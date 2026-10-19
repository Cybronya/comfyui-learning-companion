---
name: image_to_image_lora_sampler_unet_24
type: Image To Image
frequency: 2
level: weak
coverage: 0.714
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetNode, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释]
problems: []
missing: []
members: [数字人/数字人/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2099860117662560257.json, 视频生成/图生视频/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100042152431669249.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2099860117662560257.json、视频生成/图生视频/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100042152431669249.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
