---
name: unknown_workflow_video_lora_sampler_254
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5662
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json, 图片生成/图生图/动作迁移人物替换主体替换_2115623566283730946.json, 图片生成/图生图/动作迁移人物替换主体替换_2115670232718204929.json, 平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json, 平台全量/Wan2.2-适合半身_1977190297144840194.json, 平台全量/【橘子AI】Wan animate_万能替换_1980919592434487297.json, 平台全量/动作模仿动作迁移人物替换WanAnimate2.2_1971104745878392833.json, 数字人/数字人/动作迁移人物替换WanAnimate2.2_1990379558673289217.json, 视频生成/图生视频/自用动作模仿动作迁移_2013906240371429377.json, 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_254

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json、图片生成/图生图/动作迁移人物替换主体替换_2115623566283730946.json、图片生成/图生图/动作迁移人物替换主体替换_2115670232718204929.json、平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json、平台全量/Wan2.2-适合半身_1977190297144840194.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 9/10 个有
- `GetImageSizeAndCount` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 7/10 个有
- `MathExpression|pysssss` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `CR Text` —— 4/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/10 个有
- `GIMMVFI_interpolate` —— 4/10 个有
- `INTConstant` —— 4/10 个有
- `ImageBlend` —— 4/10 个有
- `Anything Everywhere` —— 3/10 个有
- `ImageFromBatch` —— 3/10 个有
- `ImpactInt` —— 3/10 个有
- `PoseRetargetPromptHelper` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `Textbox` —— 2/10 个有
- `ClothesSegment` —— 1/10 个有
- `PointsEditor` —— 1/10 个有
- `SeCModelLoader` —— 1/10 个有
- `SeCVideoSegmentation` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
