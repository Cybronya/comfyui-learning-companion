---
name: unknown_workflow_video_lora_sampler_18
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.503967
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, GetNode, ImageBatch, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/动作迁移自用_2035382692145012738.json, 数字人/数字人/dnf_scail.json_2084463626911567874.json, 数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json, 视频生成/图生视频/0205发布版：动作迁移（香蜜花园专用）_2020056736631103489.json, 视频生成/图生视频/1_1复刻高精细动作模仿+动作迁移plus_2084239980217585666.json, 视频生成/图生视频/1_1复刻高精细的 动作模仿 动作迁移_2084238815014772737.json, 视频生成/图生视频/1_1复刻高精细的 动作模仿 动作迁移_2085327890069155841.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移222_2047170050724990977.json, 视频生成/图生视频/Wan2.2 Animate动作迁移V4.1加上胸部臀部抖动控制2.0_2027347559571791874.json, 视频生成/图生视频/Wan2.2 Animate动作迁移_2017981139054501890.json, 视频生成/图生视频/Wan2.2 Animate动作迁移_2045053744475283458.json, 视频生成/图生视频/Wan2.2 Animate动作迁移_内部使用_2031632243076112386.json, 视频生成/图生视频/Wan2.2 Animate动作迁移最终版_2044762823896604674.json, 视频生成/图生视频/Wan2.2 Animate动作迁移（可调整汝窑参数）_2030587689145212930.json, "视频生成/图生视频/Wan2.2+Animate动作迁移3月完善版,提高一致性和稳定性_2033769307414470657.json", 视频生成/图生视频/Wan22舞蹈完美动作细节迁移，动作高仿一致性好_2062344581278158849.json, 视频生成/图生视频/Wan_Animate图+视频跳舞_2071251010294734850.json, 视频生成/图生视频/wan2.2-Animate-动作迁移长视频_2044091136876224513.json, 视频生成/图生视频/【最推荐，动作迁移高动态】WanAnimate动作迁移_2035636525664309249.json, 视频生成/图生视频/动作迁移5，横版竖版_2035886366013267970.json, 视频生成/图生视频/动作迁移V6.1+抖动版（表情、动作到位）_2040370994539405314.json, 视频生成/图生视频/动作迁移_2039702221989875713.json, 视频生成/图生视频/地表最强动作迁移工作流_2038516912669335553.json, 视频生成/图生视频/复刻美女跳舞_2056283340306735106.json, 视频生成/图生视频/小陆动作迁移工作流V9_2075410824641990657.json, 视频生成/图生视频/带货视频，动作模仿，动作迁移_2051928447810846722.json, 视频生成/图生视频/模仿跳舞_2045493013840928770.json, 视频生成/图生视频/模式二测试_2052770687701528577.json, 视频生成/图生视频/热门图片跳舞动作迁移（自动尺寸，自动时长）_2060202203054432257.json, 视频生成/图生视频/绿幕数字人口播V1_2081637987401687042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/动作迁移自用_2035382692145012738.json、数字人/数字人/dnf_scail.json_2084463626911567874.json、数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json、视频生成/图生视频/0205发布版：动作迁移（香蜜花园专用）_2020056736631103489.json、视频生成/图生视频/1_1复刻高精细动作模仿+动作迁移plus_2084239980217585666.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 30 个 workflow 都包含：
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 29/30 个有
- `VHS_VideoCombine` —— 29/30 个有
- `WanVideoContextOptions` —— 29/30 个有
- `easy float` —— 28/30 个有
- `PreviewImage` —— 27/30 个有
- `VRAMReserver` —— 22/30 个有
- `easy cleanGpuUsed` —— 19/30 个有
- `YOLOModelLoader` —— 18/30 个有
- `LazySwitch1way` —— 17/30 个有
- `MemoryCleaner` —— 17/30 个有
- `easy anythingIndexSwitch` —— 17/30 个有
- `easy boolean` —— 17/30 个有
- `easy int` —— 17/30 个有
- `DownloadAndLoadNLFModel` —— 15/30 个有
- `NLFPredict` —— 15/30 个有
- `PoseDetectionVitPoseToDWPose` —— 15/30 个有
- `RenderNLFPoses` —— 15/30 个有
- `Int` —— 13/30 个有
- `CR Text` —— 12/30 个有
- `ImpactSwitch` —— 11/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/30 个有
- `easy compare` —— 11/30 个有
- `easy imageSize` —— 11/30 个有
- `SDPoseOODLoader` —— 10/30 个有
- `SDPoseOODProcessor` —— 10/30 个有
- `WanVideoLoraSelect` —— 10/30 个有
- `BBoxYOLO` —— 8/30 个有
- `CheckpointLoaderSimple` —— 8/30 个有
- `LazySwitch2way` —— 8/30 个有
- `SDPoseDrawKeypoints` —— 8/30 个有
- `SDPoseKeypointExtractor` —— 8/30 个有
- `easy showAnything` —— 8/30 个有
- `CompressImages` —— 7/30 个有
- `VideoCombineNode` —— 7/30 个有
- `WanVideoEncode` —— 6/30 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/30 个有
- `WanVideoUni3C_embeds` —— 6/30 个有
- `ZML_AnyTypeSwitchFiveBoolean` —— 6/30 个有
- `Bool` —— 5/30 个有
- `BodyRatioMapperProportionTransfer` —— 2/30 个有
- `BodyRatioMapperSDPoseRender` —— 2/30 个有
- `ImageScaleToTotalPixels` —— 2/30 个有
- `Bjornulf_ShowText` —— 1/30 个有
- `Display Any (rgthree)` —— 1/30 个有
- `ImageConcatMulti` —— 1/30 个有
- `LayerUtility: ColorImage V2` —— 1/30 个有
- `Text` —— 1/30 个有
- `easy imageColorMatch` —— 1/30 个有
- `孤海注释` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
