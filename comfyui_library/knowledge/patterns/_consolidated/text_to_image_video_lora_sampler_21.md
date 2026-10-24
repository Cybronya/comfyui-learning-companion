---
name: text_to_image_video_lora_sampler_21
type: Text To Image
frequency: 25
level: strong
coverage: 0.66884
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, DrawViTPose, EmptyLatentImage, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy cleanGpuUsed, easy compare, easy float, easy imageSize, easy int, easy mathInt, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Animate V8三模式动作迁移表情手部一致性｜可多人切换_2091646547846066177.json, 图片生成/图生图/Animate V8三模式｜多人动作迁移表情手部风格迁移_2091823150039388161.json, 图片生成/图生图/Animate V9三模式动作迁移表情手部｜可多人角色一致性_2091655831526928385.json, 图片生成/图生图/Animate动作迁移V9｜自动尺寸适配视频生成_2095561386318454786.json, 图片生成/图生图/V8三模式切换多人｜Animate动作迁移表情手部一致性_2091809118070853633.json, 图片生成/图生图/V8三模式多人｜Animate动作迁移表情手部一致性生成_2091830179525120002.json, 图片生成/图生图/V9三模式多人｜Animate动作迁移表情手部角色设计_2091827390875000833.json, 图片生成/图生图/V9动作迁移表情手部一致性Animate｜三模式切换可多人压缩版_2091654530839703554.json, 图片生成/图生图/V9多人动作迁移表情手部一致性｜Animate风格迁移角色_2091653205376716801.json, 图片生成/图生图/Wan2.2 Animate动作迁移V7｜自动尺寸同步运镜24G显存优化_2106963428257652737.json, 图片生成/图生图/多人V9一致性｜动作迁移表情手部风格迁移生成_2091820492125724673.json, 图片生成/图生图/自动尺寸动作迁移V9｜Animate风格迁移一键生成_2095806524168957953.json, 视频生成/图生视频/Animate V8三种模式随意切换｜多人动作迁移图生视频，表情手部一致性全保住_2100448012416933890.json, 视频生成/图生视频/Animate V9 动作迁移+表情+手部一致｜三模式切换支持多人_2096863458942873602.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2100208341262884866.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2101877076700778498.json, 视频生成/图生视频/Animate动作迁移V9｜自动尺寸视频图生视频直出_2091247920522817538.json, 视频生成/图生视频/Animate动作迁移_表情与手部细节全保持一致_2108738466895978498.json, 视频生成/图生视频/Animate动作迁移极速版复刻跳舞自动尺寸 动作复刻视频生成_2105417262227345410.json, 视频生成/图生视频/Coze Drive动作迁移V9固定版｜608x1088分辨率_2094521961572552705.json, 视频生成/图生视频/Scail-2.0_2094686124764655617.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101214216253435906.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101451540824412162.json, 视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json, 视频生成/图生视频/三模式切换多人｜Animate动作迁移表情手部一致性图生视频_2091819115777454082.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Animate V8三模式动作迁移表情手部一致性｜可多人切换_2091646547846066177.json、图片生成/图生图/Animate V8三模式｜多人动作迁移表情手部风格迁移_2091823150039388161.json、图片生成/图生图/Animate V9三模式动作迁移表情手部｜可多人角色一致性_2091655831526928385.json、图片生成/图生图/Animate动作迁移V9｜自动尺寸适配视频生成_2095561386318454786.json、图片生成/图生图/V8三模式切换多人｜Animate动作迁移表情手部一致性_2091809118070853633.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 25 个 workflow 都包含：
- `BatchCount+`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DrawViTPose`
- `EmptyLatentImage`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LazySwitch2way`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy compare`
- `easy float`
- `easy imageSize`
- `easy int`
- `easy mathInt`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 24/25 个有
- `CheckpointLoaderSimple` —— 24/25 个有
- `CompressImages` —— 24/25 个有
- `ImageScaleToTotalPixels` —— 24/25 个有
- `ImpactSwitch` —— 24/25 个有
- `SDPoseDrawKeypoints` —— 24/25 个有
- `SDPoseKeypointExtractor` —— 24/25 个有
- `VideoCombineNode` —— 24/25 个有
- `WanVideoBlockSwap` —— 24/25 个有
- `WanVideoEncode` —— 24/25 个有
- `WanVideoSetBlockSwap` —— 24/25 个有
- `WanVideoUni3C_ControlnetLoader` —— 24/25 个有
- `WanVideoUni3C_embeds` —— 24/25 个有
- `YOLOModelLoader` —— 24/25 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 24/25 个有
- `easy anythingIndexSwitch` —— 24/25 个有
- `BodyRatioMapperProportionTransfer` —— 23/25 个有
- `BodyRatioMapperSDPoseRender` —— 23/25 个有
- `Bool` —— 19/25 个有
- `孤海注释` —— 19/25 个有
- `LayerUtility: ColorImage V2` —— 15/25 个有
- `SimpleMath+` —— 14/25 个有
- `PreviewImage` —— 12/25 个有
- `easy showAnything` —— 9/25 个有
- `EmptyImage` —— 4/25 个有
- `AnyBooleanSwitch` —— 3/25 个有
- `PrimitiveBoolean` —— 3/25 个有
- `SaveImage` —— 3/25 个有
- `DownloadAndLoadNLFModel` —— 1/25 个有
- `NLFPredict` —— 1/25 个有
- `PoseDetectionVitPoseToDWPose` —— 1/25 个有
- `RenderNLFPoses` —— 1/25 个有
- `TT_img_enc` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（26/25 个样本）：Steps较低可能导致细节不足
