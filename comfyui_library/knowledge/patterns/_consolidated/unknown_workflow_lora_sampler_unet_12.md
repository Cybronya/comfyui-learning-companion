---
name: unknown_workflow_lora_sampler_unet_12
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.854679
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2101599676305854466.json, 图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2110816443343396866.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2075457433375428609.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2076533225496862722.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2076924751913771009.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2079492729381408769.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080547652789424129.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080950328421347329.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2081735465606148098.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082544098346627074.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082911442872913922.json, 图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2084166560939339777.json, 图片生成/图生图/一键换装_+换衣_+_电商服装展示_FireRed-Image-Edit_2059910298127126529.json, 图片生成/图生图/一键换装_+换衣_+_电商服装展示_FireRed-Image-Edit_2060170775730151425.json, 图片生成/图生图/一键换装_电商服装展示_2060292641534861314.json, 图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2078462867568943105.json, 图片生成/图生图/一键换装新版本2.0  服饰展示 换装 换衣  电商服装展示_2084532894797750273.json, 图片生成/图生图/一键高清换衣不戴帽子6.0电商服装_2065882472541417474.json, 图片生成/图生图/修图 改图  换装 换衣  电商服装展示_2095215433443012610.json, 图片生成/图生图/去除水印工作流_2078477762511327234.json, 图片生成/图生图/双图服装试 穿电商换装_2100599874197737474.json, 图片生成/图生图/多图编辑替换神器FireRed-Image-Edit+1.1_2034432725708447746.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2077814423313539074.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2083519274223759361.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2084893307200692226.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2087573793047928833.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2089231222269636609.json, 图片生成/图生图/服装展示  服饰展示  快速换装   一键换衣  电商服装展示_2089235233601318913.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2101599676305854466.json、图片生成/图生图/一键换装 换衣  电商服装展示  小红书  FireRed-Image-Edit_2110816443343396866.json、图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2075457433375428609.json、图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2076533225496862722.json、图片生成/图生图/一键换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2076924751913771009.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 24/28 个有
- `LayerUtility: ImageReel` —— 24/28 个有
- `LayerUtility: ImageReelComposit` —— 24/28 个有
- `PIP_图像联结` —— 9/28 个有
- `SeedVR2LoadDiTModel` —— 9/28 个有
- `SeedVR2LoadVAEModel` —— 9/28 个有
- `SeedVR2VideoUpscaler` —— 9/28 个有
- `ImageConcanate` —— 6/28 个有
- `Anything Everywhere3` —— 1/28 个有
- `Fast Groups Bypasser (rgthree)` —— 1/28 个有
- `TT_img_enc` —— 1/28 个有
- `Text` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 28 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，28 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
