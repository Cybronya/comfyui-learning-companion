---
name: image_to_image_sampler_vae_19
type: Image To Image
frequency: 9
level: strong
coverage: 0.949667
common_nodes: [ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/线稿图转3d_1955066406536712194.json, 图片生成/图生图/🦖恶搞之家风格_1947202982187311106.json, 图片生成/文生图/KontextDEV女孩坐沙发_1938830456097792001.json, 图片生成/文生图/KontextDEV抱着黑猫的女孩_1938509637782011905.json, 图片生成/文生图/KontextDev转绘赛璐珞日漫风_1938493107786964994.json, 平台全量/Kontext Dev产品迁移-一句话改图时代开启_1939852220722487298.json, 平台全量/Kontext Dev单图模式-一句话改图时代开启_1938975352062726145.json, 平台全量/kontext Dev 女孩拿香水坐沙发+提示词反推_1939846539177332738.json, 平台全量/kontext nunchaku Dev 女孩拿香水坐沙发_1939838535958761474.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/线稿图转3d_1955066406536712194.json、图片生成/图生图/🦖恶搞之家风格_1947202982187311106.json、图片生成/文生图/KontextDEV女孩坐沙发_1938830456097792001.json、图片生成/文生图/KontextDEV抱着黑猫的女孩_1938509637782011905.json、图片生成/文生图/KontextDev转绘赛璐珞日漫风_1938493107786964994.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 8/9 个有
- `FluxGuidance` —— 8/9 个有
- `FluxKontextImageScale` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `RH_Translator` —— 7/9 个有
- `ImageConcanate` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `ConstrainImage|pysssss` —— 3/9 个有
- `ImageResize+` —— 3/9 个有
- `LayerUtility: CropByMask V2` —— 2/9 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/9 个有
- `RMBG` —— 2/9 个有
- `SUPIR_Upscale` —— 2/9 个有
- `CLIPTextEncodeFlux` —— 1/9 个有
- `EmptyLatentImage` —— 1/9 个有
- `ImageStitch` —— 1/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/9 个有
- `ModelSamplingFlux` —— 1/9 个有
- `NunchakuFluxDiTLoader` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 9 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
