---
name: unknown_workflow_lora_sampler_unet_10
type: Unknown Workflow
frequency: 33
level: strong
coverage: 0.863879
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/不受限制，一间换装（不明白的注意看里面的提示）_2042499757460955138.json, 图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json, 图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json, 图片生成/图生图/单图编辑-rh-Qwen-Edit-2511-模板_2013616947384029186.json, 图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084911205348634625.json, 图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084913910007816194.json, 图片生成/图生图/小红书FireRed-Image-Edit单图编辑_2060599465312079874.json, 图片生成/图生图/小红书FireRed-Image-Edit多图编辑_2059878171373301762.json, 图片生成/图生图/小红书FireRed-Image-Edit自定义上妆_2060607135624552450.json, 图片生成/图生图/小红书FireRed-Image-Edit自定义封面效果_2060614703394672641.json, 图片生成/图生图/服装  服饰   换装   换衣  一键换装   一键换衣 电商服装展示_2070831183537205249.json, 图片生成/图生图/服装  服饰  换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2075505838575411202.json, 图片生成/图生图/服装  服饰  换装 换衣  电商服装展示_2070829244292354049.json, 图片生成/图生图/服装  服饰  换装 换衣  电商服装展示_2071935435223425025.json, 图片生成/图生图/服装  服饰  换装 换衣  电商服装展示_2073680156350304258.json, 图片生成/图生图/服装 服装展示 服饰  一键换衣  换衣  电商服装展示_2071932590998769665.json, 图片生成/图生图/服装 服饰  换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2076910728660996098.json, 图片生成/图生图/服装 服饰  换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2083105556780371969.json, 图片生成/图生图/服装 服饰  换装 换衣  电商服装展示_2073503215710195714.json, 图片生成/图生图/服装 服饰 一键换装 一键换衣  电商服装展示_2075272857491427329.json, 图片生成/图生图/服装 服饰 一键换装 一键换衣  电商服装展示_2084500338706567169.json, 图片生成/图生图/服装展示  换装 换衣  电商服装展示_2075868021922549761.json, 图片生成/图生图/服装迁移 无痕保留细节 真实自然 FireRed-Edit 超强图片编辑_2070020059367559170.json, 图片生成/图生图/服饰  服装  换装 换衣  电商服装展示_2073283111575703554.json, 图片生成/图生图/服饰 服装  换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2074488902806753282.json, 图片生成/图生图/服饰 服装  换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2075487295997833217.json, 图片生成/图生图/温暖日光CCD_2075075472152682497.json, 图片生成/图生图/超好用🔥小红书-服装展示一键换衣-保持人物一致性_2047183634578284545.json, 图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json, 图片生成/文生图/FireRed-Image-Edit超强合集_2032145474236456961.json, 图片生成/文生图/一键换衣_2076039591257264130.json, 图片生成/文生图/换装  换衣  一键换衣  衣服展示_2050943553332883458.json, 视频生成/图生视频/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2073634953857953794.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（图片生成/图生图/不受限制，一间换装（不明白的注意看里面的提示）_2042499757460955138.json、图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json、图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json、图片生成/图生图/单图编辑-rh-Qwen-Edit-2511-模板_2013616947384029186.json、图片生成/图生图/小红书+电商服装展示+换装+换衣+FireRed-Image-Edit_2084911205348634625.json…）

- **类型**：Unknown Workflow
- **样本数**：33
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 33 个 workflow 都包含：
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
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 32/33 个有
- `Image Comparer (rgthree)` —— 31/33 个有
- `LayerUtility: ImageReel` —— 28/33 个有
- `LayerUtility: ImageReelComposit` —— 28/33 个有
- `PreviewImage` —— 23/33 个有
- `Anything Everywhere3` —— 10/33 个有
- `CR Text` —— 10/33 个有
- `Fast Groups Bypasser (rgthree)` —— 3/33 个有
- `DuckHideNode` —— 1/33 个有
- `EmptySD3LatentImage` —— 1/33 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 33 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 33 | 100% |
| 采样算法 | euler | - | 33 | 88% |
| 调度器 | simple | - | 33 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 33 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/33 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，33 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，33 个样本，一致性 88%
- 调度器 最常用 simple，33 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 高发问题（35/33 个样本）：Steps较低可能导致细节不足
