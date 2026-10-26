---
name: image_to_image_sampler_clip_unet_47
type: Image To Image
frequency: 8
level: strong
coverage: 0.81775
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext奇技淫巧之高清放大（细节拉满效果逆天）_1940033039915421698.json, 图片生成/图生图/Kontext高清放大_1944620173674336258.json, 图片生成/图生图/flux_kontext_dev_一秒变自拍_1941803812078383105.json, 图片生成/图生图/flux_kontext_dev_一键打光，为照片增加电影光照效果_1941898475904856065.json, 图片生成/图生图/kontext开源+LLM提示词优化+8步出图—用嘴改图开源模型单图王炸全能工作流_1939280801999593473.json, 图片生成/图生图/kontext老照片修复—用嘴改图开源模型单图模式_1938786627152236545.json, 图片生成/图生图/kontext高清放大（人像专用保持人像完全一致）_1939303624373673986.json, 图片生成/图生图/🔎kontext 🔍【一键】高清修复，人像专用保持人像完全一致_1960521386806734849.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext奇技淫巧之高清放大（细节拉满效果逆天）_1940033039915421698.json、图片生成/图生图/Kontext高清放大_1944620173674336258.json、图片生成/图生图/flux_kontext_dev_一秒变自拍_1941803812078383105.json、图片生成/图生图/flux_kontext_dev_一键打光，为照片增加电影光照效果_1941898475904856065.json、图片生成/图生图/kontext开源+LLM提示词优化+8步出图—用嘴改图开源模型单图王炸全能工作流_1939280801999593473.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `RH_Translator` —— 6/8 个有
- `FluxKontextImageScale` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `Int` —— 3/8 个有
- `easy compare` —— 3/8 个有
- `easy ifElse` —— 3/8 个有
- `DF_Image_scale_to_side` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `SUPIR_Upscale` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
