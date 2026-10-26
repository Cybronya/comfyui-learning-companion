---
name: unknown_workflow_video_lora_sampler_50
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.49981
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GetImageSize, GetImageSize+, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, ResizeMask, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy seed]
problems: []
missing: []
members: [图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json, 数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json, 数字人/数字人/Wan视频编辑V5-简易-替换单人-最新V2版模型_1971148713966112769.json, 数字人/数字人/[众馨]V5角色替换_1978724316718239745.json, 数字人/数字人/[众馨]v5.1长视频_1997938569148817409.json, 数字人/数字人/动作模仿_1995104342615240706.json, 视频生成/图生视频/12月Wan替换单人-_2004125013651431425.json, 视频生成/图生视频/Wan2.2 单人角色一键替换_2004191183524032514.json, 视频生成/图生视频/Wan2.2-Animate-视频换人-视频编辑_1967603530557263873.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2083504711071784961.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2083527439560560641.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2091491947067305986.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_1986747671119605761.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_1997959528341733378.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_2011440893659713538.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_2044050920656343042.json, 视频生成/图生视频/Wan视频编辑简易-替换单人-最极速版_2083053571100205058.json, 视频生成/图生视频/【简便版】Wan2.2 图生视频 人物动作迁移 复制姿态_1976803129901699073.json, 视频生成/图生视频/人替换（6g显存可用_2026602744257187841.json, 视频生成/图生视频/浮云 —视频换人（人物尽量选择全身照）_1993617615450996738.json, 视频生成/图生视频/🦖Wan视频替换单人v5_1979090579290230785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json、数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json、数字人/数字人/Wan视频编辑V5-简易-替换单人-最新V2版模型_1971148713966112769.json、数字人/数字人/[众馨]V5角色替换_1978724316718239745.json、数字人/数字人/[众馨]v5.1长视频_1997938569148817409.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 21 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSize`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `ResizeMask`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 20/21 个有
- `PrimitiveString` —— 20/21 个有
- `PrimitiveStringMultiline` —— 20/21 个有
- `StringConcatenate` —— 20/21 个有
- `VHS_VideoCombine` —— 20/21 个有
- `easy int` —— 19/21 个有
- `Mute / Bypass Relay (rgthree)` —— 16/21 个有
- `Mute / Bypass Repeater (rgthree)` —— 16/21 个有
- `Bookmark (rgthree)` —— 14/21 个有
- `Fast Groups Bypasser (rgthree)` —— 14/21 个有
- `Label (rgthree)` —— 14/21 个有
- `ImageResizeKJ` —— 7/21 个有
- `GetImageRangeFromBatch` —— 6/21 个有
- `Note Plus (mtb)` —— 6/21 个有
- `Int` —— 3/21 个有
- `SimpleMath+` —— 3/21 个有
- `Bjornulf_ShowFloat` —— 2/21 个有
- `Bjornulf_ShowInt` —— 2/21 个有
- `Any Switch (rgthree)` —— 1/21 个有
- `AudioSeparation` —— 1/21 个有
- `CreateVideo` —— 1/21 个有
- `DownloadAndLoadWav2VecModel` —— 1/21 个有
- `Fast Groups Muter (rgthree)` —— 1/21 个有
- `ImageCompositeMasked` —— 1/21 个有
- `ImageToMask` —— 1/21 个有
- `InvertMask` —— 1/21 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/21 个有
- `MaskToImage` —— 1/21 个有
- `MultiTalkWav2VecEmbeds` —— 1/21 个有
- `PointsEditor` —— 1/21 个有
- `SaveVideo` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
