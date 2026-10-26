---
name: unknown_workflow_video_sampler_vae_24
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.482385
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LazySwitch1way, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, easy compare, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/1_1视频人物换脸_2007621094634688513.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2061113125402927106.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062092554732138498.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062097231444013057.json, 视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2066792734605791233.json, 视频生成/图生视频/Wan2.2 Animate循环长视频（动作迁移稳定版）_1987919174796292097.json, 视频生成/图生视频/Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json, 视频生成/图生视频/Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json, 视频生成/图生视频/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_2007836084251660289.json, 视频生成/图生视频/人物替换4_2054046238735118337.json, 视频生成/图生视频/视频人物替换3（多人）_2046063454615769090.json, 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041059568435863554.json, 视频生成/图生视频/（可短剧）Wan2.2 Animate人物替换V2_2041230644306513921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1_1视频人物换脸_2007621094634688513.json、视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2061113125402927106.json、视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062092554732138498.json、视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2062097231444013057.json、视频生成/图生视频/Wan2.2 Animate动作迁移稳定版长视频_2066792734605791233.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 13 个 workflow 都包含：
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
- `PreviewImage` —— 12/13 个有
- `WanVideoSetLoRAs` —— 11/13 个有
- `easy int` —— 11/13 个有
- `CM_FloatToInt` —— 9/13 个有
- `ImageBatchMulti` —— 9/13 个有
- `easy batchAnything` —— 9/13 个有
- `easy forLoopEnd` —— 9/13 个有
- `easy forLoopStart` —— 9/13 个有
- `easy showAnything` —— 9/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `CM_IntToFloat` —— 7/13 个有
- `BlockifyMask` —— 6/13 个有
- `DrawMaskOnImage` —— 6/13 个有
- `GrowMask` —— 6/13 个有
- `Image Blank` —— 6/13 个有
- `LayerUtility: ImageBlend` —— 6/13 个有
- `PointsEditor` —— 6/13 个有
- `SeCModelLoader` —— 6/13 个有
- `SeCVideoSegmentation` —— 6/13 个有
- `VHS_VideoInfo` —— 6/13 个有
- `Bookmark (rgthree)` —— 4/13 个有
- `VHS_VideoInfoLoaded` —— 4/13 个有
- `WanVideoLoraSelectMulti` —— 4/13 个有
- `WanVideoModelLoader` —— 4/13 个有
- `CoordinatePlotter` —— 2/13 个有
- `ImpactInt` —— 2/13 个有
- `LayerUtility: ImageBlendAdvance` —— 2/13 个有
- `PrimitiveInt` —— 2/13 个有
- `WanVideoLoraSelect` —— 2/13 个有
- `Int` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
