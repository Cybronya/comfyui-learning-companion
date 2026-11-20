---
name: text_to_image_lora_sampler_clip_261
type: Text To Image
frequency: 8
level: strong
coverage: 0.919625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CropWithPadInfo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511图生图实测｜千问编辑模型改图日常够用版_2112887736368721922.json, 图片生成/图生图/qwen2511开源最强换装流｜衣服款式随便换，布料褶皱都自然_2099553702960001025.json, 图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2094901420628729858.json, 图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2095331598903369730.json, 图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2095435592648708098.json, 图片生成/图生图/一键换装增强版-完美替换衣物人物一致性图生图高清放大_2087376719513743361.json, 图片生成/图生图/开源最强换装生成｜qwen2511美少女图生图处理_2092745444328820737.json, 图片生成/图生图/最强换装｜qwen图生图人像写真一键换衣_2093815297118654466.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_261

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen2511图生图实测｜千问编辑模型改图日常够用版_2112887736368721922.json、图片生成/图生图/qwen2511开源最强换装流｜衣服款式随便换，布料褶皱都自然_2099553702960001025.json、图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2094901420628729858.json、图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2095331598903369730.json、图片生成/图生图/qwen2511开源最强换装｜局部重绘图生图生成_2095435592648708098.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 7/8 个有
- `孤海注释` —— 6/8 个有
- `CR Text` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SeedVR2BlockSwap` —— 1/8 个有
- `SeedVR2ExtraArgs` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（16/8 个样本）：Steps较低可能导致细节不足
