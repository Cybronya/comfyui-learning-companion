---
name: image_to_image_sampler_unet_vae_37
type: Image To Image
frequency: 5
level: strong
coverage: 1
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/线稿图转3d_1955066406536712194.json, 图片生成/图生图/🦖恶搞之家风格_1947202982187311106.json, 图片生成/文生图/KontextDEV女孩坐沙发_1938830456097792001.json, 图片生成/文生图/KontextDEV抱着黑猫的女孩_1938509637782011905.json, 图片生成/文生图/KontextDev转绘赛璐珞日漫风_1938493107786964994.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/线稿图转3d_1955066406536712194.json、图片生成/图生图/🦖恶搞之家风格_1947202982187311106.json、图片生成/文生图/KontextDEV女孩坐沙发_1938830456097792001.json、图片生成/文生图/KontextDEV抱着黑猫的女孩_1938509637782011905.json、图片生成/文生图/KontextDev转绘赛璐珞日漫风_1938493107786964994.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `RH_Translator` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageStitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
