---
name: text_to_image_sampler_clip_unet_60
type: Text To Image
frequency: 10
level: weak
coverage: 0.9658
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/10texttoimagefast_2049395761896493057.json, 图片生成/反推提示词/10wutdydiylf_2059686073575497730.json, 图片生成/图生图/Boogu图生图标准版_2068947798048989186.json, 图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json, 图片生成/图生图/Flux2文生图_1993664157952180226.json, 图片生成/图生图/Klein 9B-动漫上色+室内风格迁移_2071151331997474818.json, 图片生成/图生图/Klein-9B-姿势控制按参考图生成_2071965968569552898.json, 图片生成/图生图/Klein-9B-法线按参考图生成_2071952516740370433.json, 图片生成/图生图/Klein-9B-深度控制按参考图生成_2071964572617105410.json, 图片生成/图生图/Klein-9B-线稿按参考图生成_2071927150692880385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/10texttoimagefast_2049395761896493057.json、图片生成/反推提示词/10wutdydiylf_2059686073575497730.json、图片生成/图生图/Boogu图生图标准版_2068947798048989186.json、图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json、图片生成/图生图/Flux2文生图_1993664157952180226.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/10 个有
- `ReferenceLatent` —— 6/10 个有
- `VAEEncode` —— 6/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `Int` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `RTXVideoSuperResolution` —— 2/10 个有
- `CannyEdgePreprocessor` —— 1/10 个有
- `DSINE-NormalMapPreprocessor` —— 1/10 个有
- `DWPreprocessor` —— 1/10 个有
- `DepthAnythingV2Preprocessor` —— 1/10 个有
- `FluxGuidance` —— 1/10 个有
- `ShellAgentPluginOutputText` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 10 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 31% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 768 | 512 - 1080 | 10 | 65% |
| 高度 | 768 | 512 - 1920 | 10 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，10 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1080，10 个样本
- 高度 中位数 768，观测区间 512 - 1920，10 个样本，取值分散，一致性仅 41%
- 高发问题（5/10 个样本）：Steps较低可能导致细节不足
