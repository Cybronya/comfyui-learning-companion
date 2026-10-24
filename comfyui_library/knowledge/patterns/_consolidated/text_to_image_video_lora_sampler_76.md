---
name: text_to_image_video_lora_sampler_76
type: Text To Image
frequency: 9
level: strong
coverage: 0.66
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CR Text, DWPreprocessor, DrawMaskOnImage, EmptyLatentImage, FaceMaskFromPoseKeypoints, Fast Groups Bypasser (rgthree), GetNode, GrowMask, ImageCropByMaskAndResize, ImageCropper, ImageResizeKJv2, Int, JWInteger, JjkText, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PixelPerfectResolution, PrimitiveInt, RHHiddenNodes, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, workflow>WanVideo, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2094030228560633857.json, 图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2102545997426679809.json, 图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2107981906280271873.json, 图片生成/图生图/换脸换发自定时长｜高清数字人动作迁移视频_2096565300929056770.json, 图片生成/图生图/自定时长高清换脸换发型 人物动作迁移自然真实的数字人视频_2095071159820840961.json, 图片生成/图生图/自定时长高清换脸换发型 人物动作迁移自然真实的数字人视频_2099279494757572609.json, 图片生成/图生图/高清视频换脸换发型自定时长人物动作迁移处理工具_2101529243921502210.json, 图片生成/图生图/高清视频换脸换发型｜自定时长动作迁移数字人生成_2096300769615106049.json, 图片生成/图生图/高清视频换脸换发型｜自定时长真实自然动作迁移数字人_2101139909175238658.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2094030228560633857.json、图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2102545997426679809.json、图片生成/图生图/人物动作迁移数字人 高清视频换脸换发型自定时长真实自然方案_2107981906280271873.json、图片生成/图生图/换脸换发自定时长｜高清数字人动作迁移视频_2096565300929056770.json、图片生成/图生图/自定时长高清换脸换发型 人物动作迁移自然真实的数字人视频_2095071159820840961.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 9 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageCropper`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `JjkText`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `workflow>WanVideo`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
