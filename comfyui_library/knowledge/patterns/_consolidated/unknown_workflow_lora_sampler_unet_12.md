---
name: unknown_workflow_lora_sampler_unet_12
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.860556
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/不受限制，一间换装（不明白的注意看里面的提示）_2042499757460955138.json, 图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json, 图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json, 图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json, 图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084911205348634625.json, 图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084913910007816194.json, 图片生成/图生图/小红书FireRed-Image-Edit单图编辑_2060599465312079874.json, 图片生成/图生图/小红书FireRed-Image-Edit多图编辑_2059878171373301762.json, 图片生成/图生图/小红书FireRed-Image-Edit自定义上妆_2060607135624552450.json, 图片生成/图生图/小红书FireRed-Image-Edit自定义封面效果_2060614703394672641.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2080744788332204033.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2081674109632729089.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2082729493181063170.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2083960130487545857.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087104573520564226.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2087596248923721730.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088141337731358722.json, 图片生成/图生图/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2088154044366934017.json, 图片生成/图生图/换装 换衣  电商服装展示V2.0_2062750173624889346.json, 图片生成/图生图/换装 换衣 电商服装展示（上传照片即可）_2067164508631683073.json, 图片生成/图生图/换装+换衣++一键换衣+电商服装展示+_2070195377646694402.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++ (1)_2071497221908029441.json, 图片生成/图生图/换装+换衣++电商服装展示+FireRed-Image-Edit+小红书++_2064884842726248449.json, 图片生成/图生图/换装+电商服装展示+FireRed-Image-Edit_2078106380417978370.json, 图片生成/图生图/换装_2075461922253795330.json, 图片生成/图生图/换装换衣电商服装展示FireRedImageEdit小红书_2065944485196029953.json, 图片生成/图生图/服装迁移 无痕保留细节 真实自然 FireRed-Edit 超强图片编辑_2070020059367559170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/不受限制，一间换装（不明白的注意看里面的提示）_2042499757460955138.json、图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json、图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json、图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json、图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084911205348634625.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 27 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 26/27 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 25/27 个有
- `LayerUtility: ImageReel` —— 23/27 个有
- `LayerUtility: ImageReelComposit` —— 23/27 个有
- `PreviewImage` —— 20/27 个有
- `CR Text` —— 9/27 个有
- `Anything Everywhere3` —— 7/27 个有
- `Fast Groups Bypasser (rgthree)` —— 2/27 个有
- `CR Prompt Text` —— 1/27 个有
- `DuckHideNode` —— 1/27 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/27 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 27 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 27 | 100% |
| 采样算法 | euler | - | 27 | 89% |
| 调度器 | simple | - | 27 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，27 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，27 个样本，一致性 89%
- 调度器 最常用 simple，27 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 高发问题（27/27 个样本）：Steps较低可能导致细节不足
