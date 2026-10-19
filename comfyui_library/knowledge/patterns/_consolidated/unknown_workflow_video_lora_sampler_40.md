---
name: unknown_workflow_video_lora_sampler_40
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.492636
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy mathInt]
problems: []
missing: []
members: [数字人/数字人/dnf_scail.json_2084463626911567874.json, 数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json, 视频生成/图生视频/2020056736631103489.json, 视频生成/图生视频/1_1复刻高精细动作模仿+动作迁移plus_2084239980217585666.json, 视频生成/图生视频/1_1复刻高精细的 动作模仿 动作迁移_2084238815014772737.json, 视频生成/图生视频/1_1复刻高精细的 动作模仿 动作迁移_2085327890069155841.json, 视频生成/图生视频/2047170050724990977.json, 视频生成/图生视频/2027347559571791874.json, 视频生成/图生视频/2017981139054501890.json, 视频生成/图生视频/2045053744475283458.json, 视频生成/图生视频/2031632243076112386.json, 视频生成/图生视频/2044762823896604674.json, 视频生成/图生视频/2030587689145212930.json, 视频生成/图生视频/2033769307414470657.json, 视频生成/图生视频/2054844641391980546.json, 视频生成/图生视频/2071251010294734850.json, 视频生成/图生视频/2044091136876224513.json, 视频生成/图生视频/【最推荐，动作迁移高动态】WanAnimate动作迁移_2035636525664309249.json, 视频生成/图生视频/2035886366013267970.json, 视频生成/图生视频/2039702221989875713.json, 视频生成/图生视频/2038516912669335553.json, 视频生成/图生视频/2035706111285792769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（数字人/数字人/dnf_scail.json_2084463626911567874.json、数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json、视频生成/图生视频/2020056736631103489.json、视频生成/图生视频/1_1复刻高精细动作模仿+动作迁移plus_2084239980217585666.json、视频生成/图生视频/1_1复刻高精细的 动作模仿 动作迁移_2084238815014772737.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 22 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RepeatImageBatch`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 21/22 个有
- `RHHiddenNodes` —— 21/22 个有
- `VRAMReserver` —— 21/22 个有
- `WanVideoContextOptions` —— 21/22 个有
- `WanVideoLoraSelectMulti` —— 21/22 个有
- `easy float` —— 19/22 个有
- `MemoryCleaner` —— 15/22 个有
- `SDPoseOODLoader` —— 12/22 个有
- `SDPoseOODProcessor` —— 12/22 个有
- `YOLOModelLoader` —— 12/22 个有
- `easy cleanGpuUsed` —— 12/22 个有
- `DownloadAndLoadNLFModel` —— 11/22 个有
- `Int` —— 11/22 个有
- `LazySwitch1way` —— 11/22 个有
- `NLFPredict` —— 11/22 个有
- `PoseDetectionVitPoseToDWPose` —— 11/22 个有
- `RenderNLFPoses` —— 11/22 个有
- `easy anythingIndexSwitch` —— 11/22 个有
- `easy boolean` —— 11/22 个有
- `easy int` —— 11/22 个有
- `WanVideoLoraSelect` —— 8/22 个有
- `easy showAnything` —— 6/22 个有
- `CR Text` —— 5/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/22 个有
- `easy compare` —— 4/22 个有
- `easy imageSize` —— 4/22 个有
- `ImpactSwitch` —— 3/22 个有
- `Bjornulf_ShowText` —— 1/22 个有
- `Display Any (rgthree)` —— 1/22 个有
- `ImageConcatMulti` —— 1/22 个有
- `LazySwitch2way` —— 1/22 个有
- `PreviewAny` —— 1/22 个有
- `PrimitiveFloat` —— 1/22 个有
- `RunningHub Deepcleaner` —— 1/22 个有
- `Text` —— 1/22 个有
- `WanVideoEncode` —— 1/22 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/22 个有
- `WanVideoUni3C_embeds` —— 1/22 个有
- `easy imageColorMatch` —— 1/22 个有
- `孤海注释` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
