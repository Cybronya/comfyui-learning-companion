---
name: unknown_workflow_video_lora_sampler_32
type: Unknown Workflow
frequency: 31
level: moderate
coverage: 0.494935
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageSize, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy seed]
problems: []
missing: []
members: [图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json, 平台全量/004.Wan视频之源006.Wan2.2表情+动作迁移、模仿V5优化版.json_2035415489949732866.json, 平台全量/004.Wan视频之源006.图+视频跳舞-视频背景_2035564090961174530.json, 平台全量/Wan animate视频编辑（角色替换）_1997627030193811457.json, 平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json, 平台全量/WanAnimate视频编辑&动作迁移&视频转换风格_2031013531558092802.json, 平台全量/WanAnimate视频编辑&动作迁移_2008791073337905153.json, 平台全量/Wan视频编辑-替换单人（参考图片替换视频中的人物和背景）_2007263349347721218.json, 平台全量/Wan视频编辑替换_2013984654969278466.json, 平台全量/人物替换_1974127792839372801.json, 平台全量/人物替换what can i say？_2026342543331430401.json, 数字人/数字人/Wan2.2 Animate 人物替换 精准替换_2009975614958211074.json, 数字人/数字人/Wan视频编辑V5-简易-替换单人-最新V2版模型_1971148713966112769.json, 数字人/数字人/[众馨]V5角色替换_1978724316718239745.json, 数字人/数字人/[众馨]v5.1长视频_1997938569148817409.json, 数字人/数字人/动作模仿_1995104342615240706.json, 视频生成/图生视频/12月Wan替换单人-_2004125013651431425.json, 视频生成/图生视频/Wan2.2 单人角色一键替换_2004191183524032514.json, 视频生成/图生视频/Wan2.2-Animate-视频换人-视频编辑_1967603530557263873.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2083504711071784961.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2083527439560560641.json, 视频生成/图生视频/Wan视频编辑 替换人物 最极速版_2091491947067305986.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_1986747671119605761.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_1997959528341733378.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_2011440893659713538.json, 视频生成/图生视频/Wan视频编辑V5-简易-替换单人-最新V2版模型_2044050920656343042.json, 视频生成/图生视频/Wan视频编辑简易-替换单人-最极速版_2083053571100205058.json, 视频生成/图生视频/【简便版】Wan2.2 图生视频 人物动作迁移 复制姿态_1976803129901699073.json, 视频生成/图生视频/人替换（6g显存可用_2026602744257187841.json, 视频生成/图生视频/浮云 —视频换人（人物尽量选择全身照）_1993617615450996738.json, 视频生成/图生视频/🦖Wan视频替换单人v5_1979090579290230785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json、平台全量/004.Wan视频之源006.Wan2.2表情+动作迁移、模仿V5优化版.json_2035415489949732866.json、平台全量/004.Wan视频之源006.图+视频跳舞-视频背景_2035564090961174530.json、平台全量/Wan animate视频编辑（角色替换）_1997627030193811457.json、平台全量/Wan2.2表情+动作迁移、模仿V5优化版_1998815533208363010.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 31 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 30/31 个有
- `DownloadAndLoadSAM2Model` —— 30/31 个有
- `DrawMaskOnImage` —— 30/31 个有
- `GetImageSize+` —— 30/31 个有
- `GrowMask` —— 30/31 个有
- `ImageFromBatch` —— 30/31 个有
- `PreviewAny` —— 30/31 个有
- `PrimitiveString` —— 30/31 个有
- `PrimitiveStringMultiline` —— 30/31 个有
- `ResizeMask` —— 30/31 个有
- `Sam2Segmentation` —— 30/31 个有
- `StringConcatenate` —— 30/31 个有
- `VHS_VideoCombine` —— 30/31 个有
- `easy cleanGpuUsed` —— 30/31 个有
- `easy clearCacheAll` —— 30/31 个有
- `easy int` —— 29/31 个有
- `Mute / Bypass Relay (rgthree)` —— 25/31 个有
- `Mute / Bypass Repeater (rgthree)` —— 25/31 个有
- `Fast Groups Bypasser (rgthree)` —— 22/31 个有
- `Label (rgthree)` —— 21/31 个有
- `Bookmark (rgthree)` —— 19/31 个有
- `ImageResizeKJ` —— 10/31 个有
- `Note Plus (mtb)` —— 8/31 个有
- `GetImageRangeFromBatch` —— 7/31 个有
- `Int` —— 4/31 个有
- `SimpleMath+` —— 3/31 个有
- `Any Switch (rgthree)` —— 2/31 个有
- `AudioSeparation` —— 2/31 个有
- `Bjornulf_ShowFloat` —— 2/31 个有
- `Bjornulf_ShowInt` —— 2/31 个有
- `DownloadAndLoadWav2VecModel` —— 2/31 个有
- `Fast Groups Muter (rgthree)` —— 2/31 个有
- `ImageCompositeMasked` —— 2/31 个有
- `ImageResize+` —— 2/31 个有
- `ImageToMask` —— 2/31 个有
- `InvertMask` —— 2/31 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/31 个有
- `MaskToImage` —— 2/31 个有
- `MultiTalkWav2VecEmbeds` —— 2/31 个有
- `PointsEditor` —— 2/31 个有
- `CreateVideo` —— 1/31 个有
- `SaveVideo` —— 1/31 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
