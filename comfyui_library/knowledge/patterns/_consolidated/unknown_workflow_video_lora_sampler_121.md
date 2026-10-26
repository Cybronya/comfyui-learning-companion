---
name: unknown_workflow_video_lora_sampler_121
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.574133
common_nodes: [CLIPVisionLoader, CR Prompt Text, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/定制专用-动作迁移工作流（Wan采样器版）-单路 ViTPose+Draw ViT Pose标准方案_2051347806027296770.json, 视频生成/图生视频/抖音后裔摇_2070541183562113025.json, 视频生成/图生视频/抖音拿破仑_2070540177809952769.json, 视频生成/图生视频/最新版animate 动作迁移_舞蹈模仿1漫剧电商服装分镜真人_2071997191392157697.json, 视频生成/图生视频/最新版animate动作_舞蹈模仿2漫剧电商服装分镜真人_2073410541107896321.json, "视频生成/图生视频/本地开源免费,舞蹈迁移_2061344099260784641.json", 视频生成/图生视频/本地开源免费.the dance of catch catch_2060930629302312961.json, 视频生成/图生视频/本地开源免费，巴西FUNK摇流_2055559300801679362.json, 视频生成/图生视频/本地开源免费，巴西funk摇僵尸版_2055572704480243714.json, 视频生成/图生视频/本地开源免费，拿破仑进行曲_2056626842236440577.json, 视频生成/图生视频/漫剧图生视频remixv1_2069226848269201409.json, 视频生成/图生视频/舞蹈动作复刻_2086688476229095425.json, 视频生成/图生视频/舞蹈动作模仿2_2101567862912671746.json, 视频生成/图生视频/舞蹈动作模仿_2084254634042023937.json, 视频生成/图生视频/舞蹈复刻_2079046607487725569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_121

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/定制专用-动作迁移工作流（Wan采样器版）-单路 ViTPose+Draw ViT Pose标准方案_2051347806027296770.json、视频生成/图生视频/抖音后裔摇_2070541183562113025.json、视频生成/图生视频/抖音拿破仑_2070540177809952769.json、视频生成/图生视频/最新版animate 动作迁移_舞蹈模仿1漫剧电商服装分镜真人_2071997191392157697.json、视频生成/图生视频/最新版animate动作_舞蹈模仿2漫剧电商服装分镜真人_2073410541107896321.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DrawViTPose`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `JWInteger` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `VHS_VideoInfoSource` —— 14/15 个有
- `WanVideoTorchCompileSettings` —— 12/15 个有
- `WanVideoBlockSwap` —— 9/15 个有
- `easy mathInt` —— 6/15 个有
- `ImageConcatenate_UTK` —— 5/15 个有
- `LayerUtility: PurgeVRAM V2` —— 5/15 个有
- `WanAnimatePlus BlockSwap` —— 3/15 个有
- `GetImageRangeFromBatch` —— 1/15 个有
- `GradientImage` —— 1/15 个有
- `ImageScale` —— 1/15 个有
- `Int` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `MathExpression|pysssss` —— 1/15 个有
- `VHS_VideoInfoLoaded` —— 1/15 个有
- `easy imageCount` —— 1/15 个有
- `easy indexAnything` —— 1/15 个有
- `ttN float` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
