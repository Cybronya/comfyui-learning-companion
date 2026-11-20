---
name: image_to_image_upscale_lora_sampler_25
type: Image To Image
frequency: 6
level: strong
coverage: 0.747333
common_nodes: [Any Switch (rgthree), CLIPLoader, EmptySD3LatentImage, GetNode, ImpactInt, KSampler, KepStringLiteral, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2099389898447998978.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2100600056696107010.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2110580172410933249.json, 图片生成/图生图/Krea2+角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2+高清放大_2102745930830270466.json, 图片生成/图生图/空白工作流四视图 Character (Animated + Live-Action) Assets_2112344315598036993.json, 图片生成/图生图/角色(漫剧+真人)资产四视图一键生成Krea2_2106402373739569154.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2099389898447998978.json、图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2100600056696107010.json、图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2 高清放大_2110580172410933249.json、图片生成/图生图/Krea2+角色(漫剧+真人)资产四视图一键生成｜4步加速版｜SeedVR2+高清放大_2102745930830270466.json、图片生成/图生图/空白工作流四视图 Character (Animated + Live-Action) Assets_2112344315598036993.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `ImpactInt`
- `KSampler`
- `KepStringLiteral`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
