---
name: image_to_image_lora_sampler_unet_18
type: Image To Image
frequency: 18
level: strong
coverage: 0.777833
common_nodes: [CLIPLoader, EmptySD3LatentImage, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea-2-服装转移 服装试穿_2079811923427811330.json, 图片生成/图生图/Krea2 一键人物三视图+动态表情_2101374666509209601.json, 图片生成/图生图/Krea2 一键人物三视图+动态表情_2103482978172227585.json, 图片生成/图生图/Krea2 一键角色四视图_2090402745974087682.json, 图片生成/图生图/Krea2 人物一致性编辑_2082160207756611585.json, 图片生成/图生图/Krea2 服装提取_2093739389833793538.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100031704340717570.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100145717296852994.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2108446641257795585.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2108452003608350722.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2108471820046397441.json, 图片生成/图生图/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2108473367333527553.json, 图片生成/图生图/Krea2 角色四视图_2100439894907772929.json, 图片生成/图生图/Krea2_角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100403705555283969.json, 图片生成/图生图/Krea2_角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100491753827688450.json, 图片生成/图生图/Krea2_角色(漫剧+真人)资产四视图一键生成｜4步加速版_2101079172696330242.json, 数字人/数字人/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2099860117662560257.json, 视频生成/图生视频/Krea2 角色(漫剧+真人)资产四视图一键生成｜4步加速版_2100042152431669249.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_18

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Krea-2-服装转移 服装试穿_2079811923427811330.json、图片生成/图生图/Krea2 一键人物三视图+动态表情_2101374666509209601.json、图片生成/图生图/Krea2 一键人物三视图+动态表情_2103482978172227585.json、图片生成/图生图/Krea2 一键角色四视图_2090402745974087682.json、图片生成/图生图/Krea2 人物一致性编辑_2082160207756611585.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 18 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/18 个有
- `PreviewImage` —— 13/18 个有
- `GetNode` —— 12/18 个有
- `SetNode` —— 12/18 个有
- `孤海注释` —— 12/18 个有
- `MuyeTextEditOutput` —— 2/18 个有
- `ResolutionSelector` —— 2/18 个有
- `EmptyImage` —— 1/18 个有
- `ImageResizeKJv2` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `SaveAnimatedWEBP` —— 1/18 个有
- `easy imageConcat` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 18 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 89% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，18 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 89%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
