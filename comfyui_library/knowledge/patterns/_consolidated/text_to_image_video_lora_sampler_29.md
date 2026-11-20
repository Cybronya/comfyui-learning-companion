---
name: text_to_image_video_lora_sampler_29
type: Text To Image
frequency: 20
level: strong
coverage: 0.74565
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DrawViTPose, EmptyLatentImage, ImageBatch, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动作迁移动作一致性加强版｜表情手部抖动全需要plus_2112938055853240322.json, 图片生成/图生图/动作高仿一键迁移｜高显存角色一致性风格迁移生成_2091825884121616386.json, 图片生成/图生图/高仿级动作迁移复刻神器｜动作细节高度还原｜高显存配置直出_2113101434249105410.json, 平台全量/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2092552295023202306.json, 平台全量/舞蹈复刻4段变装｜动作迁移视频换脸视频生视频_2089022185728987138.json, 平台全量/高级强化版 人物细节级高质量动作迁移输出_2096747903225257986.json, 视频生成/图生视频/1_1复刻高精细动作模仿｜动作迁移角色一致性图生视频_2091661066261590018.json, 视频生成/图生视频/1_1高精细动作模仿复刻｜plus增强动作迁移｜视频风格转换输出_2113107225316257793.json, 视频生成/图生视频/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2110585129834991617.json, 视频生成/图生视频/Animate动作迁移极速版｜自动尺寸一键复刻跳舞视频_2105129829493465090.json, 视频生成/图生视频/Animate极速动作迁移｜复刻跳舞自动适配视频尺寸_2105224763630243842.json, 视频生成/图生视频/WanAnimate升级版 动作迁移全程画面不变色_2096743688486612993.json, 视频生成/图生视频/动作迁移可抖X版｜爆款视频动作轻松搬运复用_2098714470225899522.json, 视频生成/图生视频/动作迁移四段变装神器｜服装灵活分段自由切换｜图生视频换装_2113087631218274306.json, 视频生成/图生视频/动作迁移支持抖音平台 图生视频人物动态精准跟随_2098474317028880385.json, 视频生成/图生视频/动作高仿一键迁移｜高显存风格迁移图生视频生成_2091807774530424833.json, 视频生成/图生视频/口哨舞动作迁移工作流，视频换脸动作迁移图生视频处理工具_2107540897608069122.json, 视频生成/图生视频/口哨舞动作迁移｜跟着节奏吹口哨跳舞，视频换脸动作两合一_2107349970042056706.json, 视频生成/图生视频/口哨舞手势舞换衣加动作迁移加抖X加最长30秒工作流，动作迁移图生视频_2107542399965810689.json, 视频生成/图生视频/口哨舞手势舞换衣动作迁移抖X版｜最长30秒，换装跳舞一气呵成_2107356106170392577.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/动作迁移动作一致性加强版｜表情手部抖动全需要plus_2112938055853240322.json、图片生成/图生图/动作高仿一键迁移｜高显存角色一致性风格迁移生成_2091825884121616386.json、图片生成/图生图/高仿级动作迁移复刻神器｜动作细节高度还原｜高显存配置直出_2113101434249105410.json、平台全量/4段变装灵活分段动作迁移 服装替换人脸替换视频换脸神器_2092552295023202306.json、平台全量/舞蹈复刻4段变装｜动作迁移视频换脸视频生视频_2089022185728987138.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `EmptyLatentImage`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 19/20 个有
- `Int` —— 18/20 个有
- `WanVideoBlockSwap` —— 18/20 个有
- `WanVideoLoraSelect` —— 18/20 个有
- `WanVideoSetBlockSwap` —— 18/20 个有
- `WanVideoContextOptions` —— 17/20 个有
- `BatchCount+` —— 16/20 个有
- `RepeatImageBatch` —— 16/20 个有
- `VHS_VideoInfo` —— 16/20 个有
- `easy cleanGpuUsed` —— 16/20 个有
- `easy mathInt` —— 16/20 个有
- `MemoryCleaner` —— 15/20 个有
- `easy float` —— 15/20 个有
- `PreviewImage` —— 14/20 个有
- `GetNode` —— 13/20 个有
- `SetNode` —— 13/20 个有
- `RHHiddenNodes` —— 12/20 个有
- `VRAMReserver` —— 10/20 个有
- `easy showAnything` —— 10/20 个有
- `SimpleMath+` —— 7/20 个有
- `easy int` —— 6/20 个有
- `ComfyMathExpression` —— 4/20 个有
- `Float` —— 3/20 个有
- `GetImageSizeAndCount` —— 3/20 个有
- `Primitive integer [Crystools]` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `CR Text` —— 2/20 个有
- `CropWithPadInfo` —— 2/20 个有
- `Fast Groups Muter (rgthree)` —— 2/20 个有
- `Image Comparer (rgthree)` —— 2/20 个有
- `ImageScaleToTotalPixels` —— 2/20 个有
- `LayerUtility: ColorImage V2` —— 2/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `LazySwitch1way` —— 2/20 个有
- `LazySwitch2way` —— 2/20 个有
- `PrimitiveStringMultiline` —— 2/20 个有
- `QwenEditConfigPreparer` —— 2/20 个有
- `QwenEditOutputExtractor` —— 2/20 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/20 个有
- `easy boolean` —— 2/20 个有
- `easy compare` —— 2/20 个有
- `easy imageRemBg` —— 2/20 个有
- `easy imageSize` —— 2/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（22/20 个样本）：Steps较低可能导致细节不足
