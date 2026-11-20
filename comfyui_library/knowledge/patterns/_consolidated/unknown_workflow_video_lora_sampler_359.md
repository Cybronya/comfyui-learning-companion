---
name: unknown_workflow_video_lora_sampler_359
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.712375
common_nodes: [CLIPLoader, CLIPTextEncode, DWPreprocessor, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json, 平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json, 平台全量/角色替换_1983725374326644738.json, 视频生成/图生视频/Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json, 视频生成/图生视频/Wan2.2-Animate-图生视频（人物替换+长视频）_1975191732172230658.json, 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+前后视角一致性）_1991499381406908418.json, 视频生成/图生视频/Wan2.2-Animate_V2模型-图生视频（人物替换+长视频）_1975411032183148546.json, 视频生成/图生视频/Wan2.2-Animate_V2模型-图生视频（自动检测+人物替换+长视频）_1988553294480064514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_359

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json、平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json、平台全量/角色替换_1983725374326644738.json、视频生成/图生视频/Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json、视频生成/图生视频/Wan2.2-Animate-图生视频（人物替换+长视频）_1975191732172230658.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 7/8 个有
- `CLIPVisionLoader` —— 7/8 个有
- `DrawMaskOnImage` —— 7/8 个有
- `FaceMaskFromPoseKeypoints` —— 7/8 个有
- `GrowMask` —— 7/8 个有
- `ImageCropByMaskAndResize` —— 7/8 个有
- `BlockifyMask` —— 6/8 个有
- `DownloadAndLoadSAM2Model` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `PointsEditor` —— 6/8 个有
- `Sam2Segmentation` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `CM_IntToFloat` —— 5/8 个有
- `GetImageRangeFromBatch` —— 5/8 个有
- `ImageBatchMulti` —— 5/8 个有
- `Int` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `RHHiddenNodes` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `VHS_GetImageCount` —— 5/8 个有
- `VHS_VideoInfoLoaded` —— 5/8 个有
- `easy seed` —— 5/8 个有
- `INTConstant` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `CreateVideo` —— 1/8 个有
- `ImageAndMaskPreview` —— 1/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/8 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/8 个有
- `LayerMask: SegformerUltraV2` —— 1/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/8 个有
- `SaveVideo` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有
- `VantageWanBlockSwap` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 8 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，8 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（18/8 个样本）：Steps较低可能导致细节不足
