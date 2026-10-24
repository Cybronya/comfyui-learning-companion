---
name: unknown_workflow_lora_sampler_unet_13
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.881538
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键精准人物替换 二创必备_2033184455149494273.json, 图片生成/图生图/产品图换装Clothes_swap_2055459015823511553.json, 图片生成/图生图/产品图的换装Clothes_swap_2055110104705454081.json, 图片生成/图生图/产品贴标_2049328622414073857.json, 图片生成/图生图/千问人物表情编辑_2026155357369798658.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080744788332204033.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2081674109632729089.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082729493181063170.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2083960130487545857.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087104573520564226.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087596248923721730.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088141337731358722.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088154044366934017.json, 图片生成/图生图/换装 换衣  电商服装展示V2.0_2062750173624889346.json, 图片生成/图生图/换装 换衣 电商服装展示（上传照片即可）_2067164508631683073.json, 图片生成/图生图/换装+换衣++一键换衣+电商服装展示+_2070195377646694402.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++ (1)_2071497221908029441.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++_2064884842726248449.json, 图片生成/图生图/换装+电商服装展示+FireRed-Image-Edit_2078106380417978370.json, 图片生成/图生图/换装_2075461922253795330.json, 图片生成/图生图/换装换衣电商服装展示FireRedImageEdit小红书_2065944485196029953.json, 图片生成/图生图/最新qwen image 2511单图编辑工作流x_2013208112680931329.json, 图片生成/图生图/最新qwen image 2511单图编辑工作流x_2070752054544527361.json, 图片生成/图生图/规划用地图生成城市设计方案图v1.0_1985273198331764738.json, 图片生成/图生图/规划用地图生成城市设计方案图v1.0_1986632623231561730.json, 图片生成/图生图/规划用地图生成城市设计方案图v2.0_1986788983076286465.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/一键精准人物替换 二创必备_2033184455149494273.json、图片生成/图生图/产品图换装Clothes_swap_2055459015823511553.json、图片生成/图生图/产品图的换装Clothes_swap_2055110104705454081.json、图片生成/图生图/产品贴标_2049328622414073857.json、图片生成/图生图/千问人物表情编辑_2026155357369798658.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 25/26 个有
- `LayerUtility: ImageReelComposit` —— 25/26 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 25/26 个有
- `Image Comparer (rgthree)` —— 19/26 个有
- `PreviewImage` —— 19/26 个有
- `FluxKontextImageScale` —— 6/26 个有
- `Text Multiline` —— 5/26 个有
- `EmptyLatentImage` —— 4/26 个有
- `Any Switch (rgthree)` —— 2/26 个有
- `Fast Groups Muter (rgthree)` —— 2/26 个有
- `Int` —— 2/26 个有
- `JjkText` —— 2/26 个有
- `CR Prompt Text` —— 1/26 个有
- `Fast Muter (rgthree)` —— 1/26 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/26 个有
- `easy promptList` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 26 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 26 | 29% |
| 采样算法 | euler | - | 26 | 100% |
| 调度器 | simple | - | 26 | 81% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 1392 | 1200 - 1504 | 4 | 90% |
| 高度 | 1240 | 1200 - 1504 | 4 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，26 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，26 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，26 个样本，一致性 100%
- 调度器 最常用 simple，26 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 1392，观测区间 1200 - 1504，4 个样本，取值集中（一致性 90%）
- 高度 中位数 1240，观测区间 1200 - 1504，4 个样本，取值集中（一致性 90%）
- 高发问题（22/26 个样本）：Steps较低可能导致细节不足
