---
name: text_to_image_video_upscale_lora
type: Text To Image
frequency: 9
level: strong
coverage: 0.881111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/VOSR视频修复放大工作流，视频超分高清增强处理工具_2103942017024880641.json, 图片生成/图生图/VOSR高清修复放大工作流｜图片视频文字修复通用处理_2097535348892069889.json, 图片生成/图生图/Vosr 2 视频高清化｜级联2K超分 还能顺手移除视频杂物_2097557813684953090.json, 图片生成/图生图/Vosr视频修复放大 分辨率提升画质增强_2105383201425416193.json, 图片生成/图生图/Vosr视频修复放大神器｜老片模糊画质一键视频超分重生_2103656804768116738.json, 数字人/数字人/Vosr2视频超分2K工作流｜数字人视频画质增强处理_2097528025284964353.json, 数字人/数字人/Vosr2视频高清放大工作流｜1K-2K数字人画质超分增强_2097494230590648321.json, 数字人/数字人/视频超分Vosr2 DLSS 2K高清增强 数字人视频清晰度提升_2098660110603214849.json, 视频生成/图生视频/minimax H3超分修复2K工作流｜Vosr2.0视频画质增强_2097786426866880514.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/VOSR视频修复放大工作流，视频超分高清增强处理工具_2103942017024880641.json、图片生成/图生图/VOSR高清修复放大工作流｜图片视频文字修复通用处理_2097535348892069889.json、图片生成/图生图/Vosr 2 视频高清化｜级联2K超分 还能顺手移除视频杂物_2097557813684953090.json、图片生成/图生图/Vosr视频修复放大 分辨率提升画质增强_2105383201425416193.json、图片生成/图生图/Vosr视频修复放大神器｜老片模糊画质一键视频超分重生_2103656804768116738.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/9 个有
- `VHS_VideoInfo` —— 6/9 个有
- `Int` —— 5/9 个有
- `PDIMAGE_LongerSize` —— 5/9 个有
- `RTXVideoSuperResolution` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `SimpleMath+` —— 4/9 个有
- `LayerFilter: GaussianBlur` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 3/9 个有
- `PreviewAny` —— 3/9 个有
- `VHS_VideoInfoSource` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `JindouyunShowAnything` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `RH_DLSS5Enhance` —— 1/9 个有
- `easy mathInt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
