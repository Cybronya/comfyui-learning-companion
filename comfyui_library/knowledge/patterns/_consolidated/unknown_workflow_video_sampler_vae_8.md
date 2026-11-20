---
name: unknown_workflow_video_sampler_vae_8
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.47536
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LazySwitch1way, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, RHHiddenNodes, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, easy compare, easy mathInt]
problems: []
missing: []
members: [平台全量/Wan2.2 Animate 循环长视频+人物替换_1984228382630166530.json, 平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json, 平台全量/Wan2.2 Animate 循环长视频+人物替换_2040249915670011906.json, 平台全量/Wan2.2 Animate人物替换V2_2004845105641127938.json, 平台全量/Wan2.2 Animate人物替换V2_2011980686403575809.json, 平台全量/Wan2.2 Animate人物替换V2_2024346799351271426.json, 平台全量/Wan2.2 Animate人物替换V2_2035195754951741441.json, 平台全量/Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593.json, 平台全量/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641.json, 平台全量/东京漂移人物替换第一段_2065409532746092545.json, 平台全量/东京漂移人物替换第二段_2066451344239714306.json, 平台全量/人物替换Animate速度优化_2000853174938370050.json, 平台全量/人物替换最新玩法Animate再次优化_1984581797700911105.json, 平台全量/换脸视频 硕阳_1992442528156766210.json, 视频生成/图生视频/1_1视频人物换脸_2007621094634688513.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2061113125402927106.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062092554732138498.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062097231444013057.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2066792734605791233.json, 视频生成/图生视频/Wan2.2 Animate循环长视频（动作迁移稳定版）_1987919174796292097.json, 视频生成/图生视频/Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json, 视频生成/图生视频/人物替换4_2054046238735118337.json, 视频生成/图生视频/视频人物替换3（多人）_2046063454615769090.json, 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041059568435863554.json, 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041230644306513921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（平台全量/Wan2.2 Animate 循环长视频+人物替换_1984228382630166530.json、平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json、平台全量/Wan2.2 Animate 循环长视频+人物替换_2040249915670011906.json、平台全量/Wan2.2 Animate人物替换V2_2004845105641127938.json、平台全量/Wan2.2 Animate人物替换V2_2011980686403575809.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 25 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LazySwitch1way`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy compare`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 18/25 个有
- `DrawMaskOnImage` —— 18/25 个有
- `GrowMask` —— 18/25 个有
- `Image Blank` —— 18/25 个有
- `LayerUtility: ImageBlend` —— 18/25 个有
- `PointsEditor` —— 18/25 个有
- `SeCModelLoader` —— 18/25 个有
- `SeCVideoSegmentation` —— 18/25 个有
- `VHS_VideoInfo` —— 18/25 个有
- `CM_FloatToInt` —— 17/25 个有
- `ImageBatchMulti` —— 17/25 个有
- `easy batchAnything` —— 17/25 个有
- `easy forLoopEnd` —— 17/25 个有
- `easy forLoopStart` —— 17/25 个有
- `easy showAnything` —— 17/25 个有
- `easy cleanGpuUsed` —— 16/25 个有
- `WanVideoSetLoRAs` —— 15/25 个有
- `easy int` —— 15/25 个有
- `CoordinatePlotter` —— 10/25 个有
- `ImpactInt` —— 10/25 个有
- `LayerUtility: ImageBlendAdvance` —— 10/25 个有
- `PrimitiveInt` —— 10/25 个有
- `Bookmark (rgthree)` —— 8/25 个有
- `VHS_VideoInfoLoaded` —— 8/25 个有
- `WanVideoLoraSelectMulti` —— 8/25 个有
- `WanVideoModelLoader` —— 8/25 个有
- `CM_IntToFloat` —— 7/25 个有
- `INTConstant` —— 4/25 个有
- `LayerUtility: PurgeVRAM` —— 4/25 个有
- `WanVideoLoraSelect` —— 2/25 个有
- `Int` —— 1/25 个有
- `SimpleMath+` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
