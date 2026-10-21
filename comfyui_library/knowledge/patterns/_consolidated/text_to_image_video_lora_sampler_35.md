---
name: text_to_image_video_lora_sampler_35
type: Text To Image
frequency: 15
level: strong
coverage: 0.6708
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, DrawViTPose, EmptyLatentImage, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, ImageScaleToTotalPixels, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy cleanGpuUsed, easy compare, easy float, easy imageSize, easy int, easy mathInt, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Animate V8三种模式随意切换｜多人动作迁移图生视频，表情手部一致性全保住_2100448012416933890.json, 视频生成/图生视频/Animate V9 动作迁移+表情+手部一致｜三模式切换支持多人_2096863458942873602.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2100208341262884866.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2101877076700778498.json, 视频生成/图生视频/Animate动作迁移V9｜自动尺寸视频图生视频直出_2091247920522817538.json, 视频生成/图生视频/Animate动作迁移_表情与手部细节全保持一致_2108738466895978498.json, 视频生成/图生视频/Animate动作迁移极速版复刻跳舞自动尺寸 动作复刻视频生成_2105417262227345410.json, 视频生成/图生视频/Animate动作迁移极速版｜自动尺寸一键复刻跳舞视频_2105129829493465090.json, 视频生成/图生视频/Animate极速动作迁移｜复刻跳舞自动适配视频尺寸_2105224763630243842.json, 视频生成/图生视频/Coze Drive动作迁移V9固定版｜608x1088分辨率_2094521961572552705.json, 视频生成/图生视频/Scail-2.0_2094686124764655617.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101214216253435906.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101451540824412162.json, 视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json, 视频生成/图生视频/三模式切换多人｜Animate动作迁移表情手部一致性图生视频_2091819115777454082.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Animate V8三种模式随意切换｜多人动作迁移图生视频，表情手部一致性全保住_2100448012416933890.json、视频生成/图生视频/Animate V9 动作迁移+表情+手部一致｜三模式切换支持多人_2096863458942873602.json、视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2100208341262884866.json、视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2101877076700778498.json、视频生成/图生视频/Animate动作迁移V9｜自动尺寸视频图生视频直出_2091247920522817538.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
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
- `ImageScaleToTotalPixels`
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
- `BBoxYOLO` —— 12/15 个有
- `BodyRatioMapperProportionTransfer` —— 12/15 个有
- `BodyRatioMapperSDPoseRender` —— 12/15 个有
- `CheckpointLoaderSimple` —— 12/15 个有
- `CompressImages` —— 12/15 个有
- `ImpactSwitch` —— 12/15 个有
- `SDPoseDrawKeypoints` —— 12/15 个有
- `SDPoseKeypointExtractor` —— 12/15 个有
- `VideoCombineNode` —— 12/15 个有
- `WanVideoBlockSwap` —— 12/15 个有
- `WanVideoEncode` —— 12/15 个有
- `WanVideoSetBlockSwap` —— 12/15 个有
- `WanVideoUni3C_ControlnetLoader` —— 12/15 个有
- `WanVideoUni3C_embeds` —— 12/15 个有
- `YOLOModelLoader` —— 12/15 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 12/15 个有
- `easy anythingIndexSwitch` —— 12/15 个有
- `LayerUtility: ColorImage V2` —— 10/15 个有
- `Bool` —— 9/15 个有
- `孤海注释` —— 9/15 个有
- `PreviewImage` —— 7/15 个有
- `SimpleMath+` —— 6/15 个有
- `EmptyImage` —— 4/15 个有
- `easy showAnything` —— 4/15 个有
- `AnyBooleanSwitch` —— 3/15 个有
- `PrimitiveBoolean` —— 3/15 个有
- `SaveImage` —— 3/15 个有
- `TT_img_enc` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
