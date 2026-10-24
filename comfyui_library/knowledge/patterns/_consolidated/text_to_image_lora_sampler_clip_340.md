---
name: text_to_image_lora_sampler_clip_340
type: Text To Image
frequency: 5
level: strong
coverage: 0.9106
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein一键风格迁移｜真人转动漫高清修复放大图生图_2110704131907346433.json, 图片生成/图生图/Flux2-Klein真人转动漫神器｜风格迁移图生图高清放大修复_2110713762478125057.json, 图片生成/图生图/Krea2洗图流无需反推，图生图其它图片处理_2111602503593844737.json, 图片生成/图生图/一键无脑反推｜krea2美少女图生图提示词生成_2090227922404724738.json, 图片生成/图生图/无需反推洗图处理｜krea2图生图摄影图片优化_2095514803900084226.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_340

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein一键风格迁移｜真人转动漫高清修复放大图生图_2110704131907346433.json、图片生成/图生图/Flux2-Klein真人转动漫神器｜风格迁移图生图高清放大修复_2110713762478125057.json、图片生成/图生图/Krea2洗图流无需反推，图生图其它图片处理_2111602503593844737.json、图片生成/图生图/一键无脑反推｜krea2美少女图生图提示词生成_2090227922404724738.json、图片生成/图生图/无需反推洗图处理｜krea2图生图摄影图片优化_2095514803900084226.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/5 个有
- `MuyeTextEditOutput` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `PainterFluxImageEdit` —— 2/5 个有
- `TextEncodeKrea2OstrisEdit` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy textIndexSwitch` —— 2/5 个有
- `workflow>自定义采样器` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `String Literal` —— 1/5 个有
- `StringMergeNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
