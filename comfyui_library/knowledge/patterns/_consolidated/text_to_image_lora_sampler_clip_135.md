---
name: text_to_image_lora_sampler_clip_135
type: Text To Image
frequency: 11
level: strong
coverage: 0.851636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/拼接参考工作流，配合分镜流使用的多图参考拼接图生图工具_2103538070481096706.json, 图片生成/图生图/漫剧分镜工作流｜全能图片2角色一致四格出图｜AI漫剧分镜一步成_2099135891058024450.json, 图片生成/文生图/Cc-MJ影视柔光｜Krea2文生图一键生成工作流_2094792236109221890.json, 图片生成/文生图/Krea2建构文生图｜创意图像一键生成直出_2091593303815970818.json, 图片生成/文生图/Krea2美感画质V2文生图处理生成工作流_2101784111047340033.json, 图片生成/文生图/Krea2美感画质双提升V2｜宋画电影感文生图工作流_2097774802739220481.json, 图片生成/文生图/Krea2美感画质双提升V2｜文生图质感升级_2097972474452467713.json, 图片生成/文生图/东方美学制作流｜中国风场景特效文生图出片_2100824969306533890.json, 图片生成/文生图/东方美学风格文生图艺术处理生成工作流工具包_2101014716817690626.json, 图片生成/文生图/巨构大场面一键生成｜Krea2文生图创作利器_2091764677775814658.json, 图片生成/文生图/画质美感双提升｜Krea2文生图一键优化_2093733215847665666.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/拼接参考工作流，配合分镜流使用的多图参考拼接图生图工具_2103538070481096706.json、图片生成/图生图/漫剧分镜工作流｜全能图片2角色一致四格出图｜AI漫剧分镜一步成_2099135891058024450.json、图片生成/文生图/Cc-MJ影视柔光｜Krea2文生图一键生成工作流_2094792236109221890.json、图片生成/文生图/Krea2建构文生图｜创意图像一键生成直出_2091593303815970818.json、图片生成/文生图/Krea2美感画质V2文生图处理生成工作流_2101784111047340033.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `ConditioningKrea2Rebalance` —— 8/11 个有
- `KSamplerAdvanced` —— 8/11 个有
- `Lora Loader Stack (rgthree)` —— 8/11 个有
- `ResolutionSelector` —— 4/11 个有
- `LoadImage` —— 3/11 个有
- `PrimitiveFloat` —— 3/11 个有
- `LatentUpscaleBy` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `RH_Nano_Banana2_Image2Image_Batch` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
