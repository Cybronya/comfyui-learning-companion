---
name: text_to_image_video_lora_sampler_81
type: Text To Image
frequency: 9
level: strong
coverage: 0.679889
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DWPreprocessor, EmptyLatentImage, FaceMaskFromPoseKeypoints, GetNode, INTConstant, ImageCropByMaskAndResize, ImageResizeKJ, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PixelPerfectResolution, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, easy anythingIndexSwitch, easy cleanGpuUsed, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/CHARM+WanAnimate 动作迁移同时保留面部表情细节_2094822876728872962.json, 视频生成/图生视频/CHARM角色替换工作流｜WanAnimate动作迁移表情生成_2097805493703102466.json, 视频生成/图生视频/WanAnimate CHARM角色替换动作迁移面部表情 图生视频人物类特效方案_2089712190046691329.json, 视频生成/图生视频/WanAnimate CHARM角色替换动作迁移面部表情 图生视频人物类特效方案_2090075393586974722.json, 视频生成/图生视频/WanAnimate+CHARM组合 面部表情细腻的角色替换与动作迁移方案_2094813264973754370.json, 视频生成/图生视频/WanAnimate动作迁移｜CHARM面部表情数字人图生视频_2092198124956766209.json, 视频生成/图生视频/WanAnimate面部表情动作迁移CHARM-角色替换_2087419478895316994.json, 视频生成/图生视频/角色替换加动作迁移加面部表情爆款复刻，图生视频一站式创作方案_2103926336380301314.json, 视频生成/图生视频/面部表情+角色替换+动作迁移｜CHARM-WanAnimate图生视频_2092141500183437314.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/CHARM+WanAnimate 动作迁移同时保留面部表情细节_2094822876728872962.json、视频生成/图生视频/CHARM角色替换工作流｜WanAnimate动作迁移表情生成_2097805493703102466.json、视频生成/图生视频/WanAnimate CHARM角色替换动作迁移面部表情 图生视频人物类特效方案_2089712190046691329.json、视频生成/图生视频/WanAnimate CHARM角色替换动作迁移面部表情 图生视频人物类特效方案_2090075393586974722.json、视频生成/图生视频/WanAnimate+CHARM组合 面部表情细腻的角色替换与动作迁移方案_2094813264973754370.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `ImageResizeKJ`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixelPerfectResolution`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/9 个有
- `ImageConcatMulti` —— 8/9 个有
- `ImpactSwitch` —— 8/9 个有
- `WanVideoContextOptions` —— 8/9 个有
- `BlockifyMask` —— 7/9 个有
- `DownloadAndLoadFlorence2Model` —— 7/9 个有
- `DownloadAndLoadSAM2Model` —— 7/9 个有
- `DrawMaskOnImage` —— 7/9 个有
- `Florence2Run` —— 7/9 个有
- `Florence2toCoordinates` —— 7/9 个有
- `GrowMask` —— 7/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `PrimitiveString` —— 7/9 个有
- `RH_Translator` —— 7/9 个有
- `RMBG` —— 7/9 个有
- `Sam2Segmentation` —— 7/9 个有
- `WanVideoSetBlockSwap` —— 7/9 个有
- `PointsEditor` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `ImageFromBatch` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `OnnxDetectionModelLoader` —— 1/9 个有
- `PoseAndFaceDetection` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `WanVideoSLG` —— 1/9 个有
- `WanVideoTeaCache` —— 1/9 个有

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
