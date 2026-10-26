---
name: unknown_workflow_lora_sampler_unet_12
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.868071
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换装FireRed+SD高清_2059969177762484226.json, 图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2078462867568943105.json, 图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2084532894797750273.json, 图片生成/图生图/一键高清换衣不戴帽子6.0电商服装_2065882472541417474.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080744788332204033.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2081674109632729089.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082729493181063170.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2083960130487545857.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087104573520564226.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087596248923721730.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088141337731358722.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088154044366934017.json, 图片生成/图生图/换装 换衣  电商服装展示V2.0_2062750173624889346.json, 图片生成/图生图/换装 换衣 电商服装展示（上传照片即可）_2067164508631683073.json, 图片生成/图生图/换装+换衣++一键换衣+电商服装展示+_2070195377646694402.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++ (1)_2071497221908029441.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++_2064884842726248449.json, 图片生成/图生图/换装+电商服装展示+FireRed-Image-Edit_2078106380417978370.json, 图片生成/图生图/换装_2075461922253795330.json, 图片生成/图生图/换装换衣电商服装展示FireRedImageEdit小红书_2065944485196029953.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2077814423313539074.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2083519274223759361.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2084893307200692226.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2087573793047928833.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2089231222269636609.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2089235233601318913.json, 图片生成/图生图/服装换装换衣电商服装展示_2064979791010418689.json, 图片生成/图生图/高清一键换装换衣服电商模特速度快_2064302988105175041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/一键换装FireRed+SD高清_2059969177762484226.json、图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2078462867568943105.json、图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2084532894797750273.json、图片生成/图生图/一键高清换衣不戴帽子6.0电商服装_2065882472541417474.json、图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080744788332204033.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 27/28 个有
- `PreviewImage` —— 27/28 个有
- `LayerUtility: ImageReel` —— 25/28 个有
- `LayerUtility: ImageReelComposit` —— 25/28 个有
- `SeedVR2LoadDiTModel` —— 11/28 个有
- `SeedVR2LoadVAEModel` —— 11/28 个有
- `SeedVR2VideoUpscaler` —— 11/28 个有
- `ImageConcanate` —— 6/28 个有
- `TT_img_enc` —— 3/28 个有
- `CR Prompt Text` —— 1/28 个有
- `ZML_AnyTypeSwitch` —— 1/28 个有
- `easy boolean` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 28 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，28 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
