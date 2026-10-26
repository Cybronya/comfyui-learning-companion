---
name: text_to_image_video_lora_sampler_8
type: Text To Image
frequency: 35
level: strong
coverage: 0.675686
common_nodes: [BatchCount+, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, DrawViTPose, EmptyLatentImage, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LazySwitch2way, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy cleanGpuUsed, easy compare, easy float, easy imageSize, easy int, easy mathInt, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Animate V8三模式动作迁移表情手部一致性｜可多人切换_2091646547846066177.json, 图片生成/图生图/Animate V8三模式｜多人动作迁移表情手部风格迁移_2091823150039388161.json, 图片生成/图生图/Animate V9三模式动作迁移 1080P压缩多人视频处理工具_2113324292657213441.json, 图片生成/图生图/Animate V9三模式动作迁移表情手部｜可多人角色一致性_2091655831526928385.json, 图片生成/图生图/AnimateV8三模式动作迁移｜表情手部一致性可多人切换｜角色稳定_2113099407443976194.json, 图片生成/图生图/AnimateV9双引擎动作迁移｜表情手部一致性三模式任切｜支持多人_2113097580589703169.json, 图片生成/图生图/Animate动作迁移V9｜自动尺寸适配视频生成_2095561386318454786.json, 图片生成/图生图/V8三模式切换多人｜Animate动作迁移表情手部一致性_2091809118070853633.json, 图片生成/图生图/V8三模式多人｜Animate动作迁移表情手部一致性生成_2091830179525120002.json, 图片生成/图生图/V8动作迁移可多人版｜表情手部一致性三模式切换｜风格迁移稳定_2113105242505170945.json, 图片生成/图生图/V9三模式多人｜Animate动作迁移表情手部角色设计_2091827390875000833.json, 图片生成/图生图/V9动作迁移三模式切换 手部一致性压缩视频生成工具_2113328977724141570.json, 图片生成/图生图/V9动作迁移表情手部一致性Animate｜三模式切换可多人压缩版_2091654530839703554.json, 图片生成/图生图/V9可多人动作迁移｜表情手部一致性同步还原｜角色一致性输出_2113094921577123841.json, 图片生成/图生图/V9多人动作迁移 手部一致性表情风格迁移处理工具_2113322739984588802.json, 图片生成/图生图/V9多人动作迁移表情手部一致性｜Animate风格迁移角色_2091653205376716801.json, 图片生成/图生图/Wan2.2 Animate动作迁移V7｜自动尺寸同步运镜24G显存优化_2106963428257652737.json, 图片生成/图生图/动作迁移V9表情手部全一致｜三种模式自由切换支持多人共创_2113103193264709633.json, 图片生成/图生图/多人V9一致性｜动作迁移表情手部风格迁移生成_2091820492125724673.json, 图片生成/图生图/自动尺寸动作迁移V9｜Animate风格迁移一键生成_2095806524168957953.json, 视频生成/图生视频/Animate V8三种模式随意切换｜多人动作迁移图生视频，表情手部一致性全保住_2100448012416933890.json, 视频生成/图生视频/Animate V9 动作迁移+表情+手部一致｜三模式切换支持多人_2096863458942873602.json, 视频生成/图生视频/AnimateV9人物动作模仿 风格迁移动作复刻处理工具_2113414118127521793.json, 视频生成/图生视频/AnimateV9动作模仿复刻｜人物动作迁移一步到位｜图生视频风格保持_2113089416687341570.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2100208341262884866.json, 视频生成/图生视频/Animate_V8三种模式随意切换_多人动作迁移保持表情手部一致_2101877076700778498.json, 视频生成/图生视频/Animate动作迁移V9｜自动尺寸视频图生视频直出_2091247920522817538.json, 视频生成/图生视频/Animate动作迁移_表情与手部细节全保持一致_2108738466895978498.json, 视频生成/图生视频/Animate动作迁移极速版复刻跳舞自动尺寸 动作复刻视频生成_2105417262227345410.json, 视频生成/图生视频/Coze Drive动作迁移V9固定版｜608x1088分辨率_2094521961572552705.json, 视频生成/图生视频/Scail-2.0_2094686124764655617.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101214216253435906.json, 视频生成/图生视频/V9自动尺寸版_Animate视频动作迁移免调参数_2101451540824412162.json, 视频生成/图生视频/Wan 2.2 Animate动作迁移图生视频处理生成工具_2102530563642052610.json, 视频生成/图生视频/三模式切换多人｜Animate动作迁移表情手部一致性图生视频_2091819115777454082.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 35 个 workflow 归纳得出（图片生成/图生图/Animate V8三模式动作迁移表情手部一致性｜可多人切换_2091646547846066177.json、图片生成/图生图/Animate V8三模式｜多人动作迁移表情手部风格迁移_2091823150039388161.json、图片生成/图生图/Animate V9三模式动作迁移 1080P压缩多人视频处理工具_2113324292657213441.json、图片生成/图生图/Animate V9三模式动作迁移表情手部｜可多人角色一致性_2091655831526928385.json、图片生成/图生图/AnimateV8三模式动作迁移｜表情手部一致性可多人切换｜角色稳定_2113099407443976194.json…）

- **类型**：Text To Image
- **样本数**：35
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 35 个 workflow 都包含：
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
- `BBoxYOLO` —— 34/35 个有
- `CheckpointLoaderSimple` —— 34/35 个有
- `CompressImages` —— 34/35 个有
- `ImageScaleToTotalPixels` —— 34/35 个有
- `ImpactSwitch` —— 34/35 个有
- `SDPoseDrawKeypoints` —— 34/35 个有
- `SDPoseKeypointExtractor` —— 34/35 个有
- `VideoCombineNode` —— 34/35 个有
- `WanVideoBlockSwap` —— 34/35 个有
- `WanVideoEncode` —— 34/35 个有
- `WanVideoSetBlockSwap` —— 34/35 个有
- `WanVideoUni3C_ControlnetLoader` —— 34/35 个有
- `WanVideoUni3C_embeds` —— 34/35 个有
- `YOLOModelLoader` —— 34/35 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 34/35 个有
- `easy anythingIndexSwitch` —— 34/35 个有
- `BodyRatioMapperProportionTransfer` —— 33/35 个有
- `BodyRatioMapperSDPoseRender` —— 33/35 个有
- `孤海注释` —— 29/35 个有
- `Bool` —— 27/35 个有
- `LayerUtility: ColorImage V2` —— 23/35 个有
- `SimpleMath+` —— 20/35 个有
- `easy showAnything` —— 15/35 个有
- `PreviewImage` —— 14/35 个有
- `SaveImage` —— 7/35 个有
- `EmptyImage` —— 4/35 个有
- `AnyBooleanSwitch` —— 3/35 个有
- `PrimitiveBoolean` —— 3/35 个有
- `DownloadAndLoadNLFModel` —— 1/35 个有
- `NLFPredict` —— 1/35 个有
- `PoseDetectionVitPoseToDWPose` —— 1/35 个有
- `RenderNLFPoses` —— 1/35 个有
- `TT_img_enc` —— 1/35 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 35 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 35 | 100% |
| 采样算法 | er_sde | - | 35 | 100% |
| 调度器 | beta | - | 35 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 35 | 100% |
| 宽度 | 80 | 80 - 80 | 35 | 100% |
| 高度 | 80 | 80 - 80 | 35 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/35 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，35 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，35 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，35 个样本，一致性 100%
- 调度器 最常用 beta，35 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，35 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，35 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，35 个样本，取值集中（一致性 100%）
- 高发问题（36/35 个样本）：Steps较低可能导致细节不足
