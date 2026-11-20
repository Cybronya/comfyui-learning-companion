---
name: unknown_workflow_video_lora_sampler_63
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.577652
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate 最强动作迁移，解决强制绑定参考视频骨骼的问题_2003700640893288450.json, 视频生成/图生视频/WanAnimate动作迁移-修复版_2049893204031488002.json, 视频生成/图生视频/animate版后裔摇_2070049005316435969.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2061344115643736066.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2099776395709861890.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2100036331069075458.json, 视频生成/图生视频/人物舞蹈动作模仿_2079228691137257473.json, 视频生成/图生视频/全能人物模仿_2081019730562998274.json, 视频生成/图生视频/动作模仿舞蹈迁移_2072605420753084417.json, 视频生成/图生视频/叮叮的鼓点咚咚咚_2083830136331399170.json, 视频生成/图生视频/女生舞蹈复刻_2098325811605622786.json, 视频生成/图生视频/抖音后裔摇_2070541183562113025.json, 视频生成/图生视频/抖音拿破仑_2070540177809952769.json, 视频生成/图生视频/最新版animate 动作迁移_舞蹈模仿1漫剧电商服装分镜真人_2071997191392157697.json, 视频生成/图生视频/最新版animate动作_舞蹈模仿2漫剧电商服装分镜真人_2073410541107896321.json, "视频生成/图生视频/本地开源免费,舞蹈迁移_2061344099260784641.json", 视频生成/图生视频/本地开源免费.the dance of catch catch_2060930629302312961.json, 视频生成/图生视频/本地开源免费，巴西FUNK摇流_2055559300801679362.json, 视频生成/图生视频/舞蹈动作复刻_2086688476229095425.json, 视频生成/图生视频/舞蹈动作模仿2_2101567862912671746.json, 视频生成/图生视频/舞蹈动作模仿_2084254634042023937.json, 视频生成/图生视频/舞蹈动作迁移_2080278150566735874.json, 视频生成/图生视频/舞蹈复刻_2079046607487725569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/WanAnimate 最强动作迁移，解决强制绑定参考视频骨骼的问题_2003700640893288450.json、视频生成/图生视频/WanAnimate动作迁移-修复版_2049893204031488002.json、视频生成/图生视频/animate版后裔摇_2070049005316435969.json、视频生成/图生视频/animate舞蹈迁移摇一摇_2061344115643736066.json、视频生成/图生视频/animate舞蹈迁移摇一摇_2099776395709861890.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 22/23 个有
- `SetNode` —— 22/23 个有
- `WanVideoLoraSelectMulti` —— 22/23 个有
- `easy showAnything` —— 22/23 个有
- `CR Prompt Text` —— 21/23 个有
- `JWInteger` —— 21/23 个有
- `VHS_VideoInfoSource` —— 21/23 个有
- `WanVideoTorchCompileSettings` —— 17/23 个有
- `easy mathInt` —— 12/23 个有
- `LayerUtility: PurgeVRAM V2` —— 11/23 个有
- `WanVideoBlockSwap` —— 11/23 个有
- `ImageConcatenate_UTK` —— 9/23 个有
- `WanAnimatePlus BlockSwap` —— 5/23 个有
- `GetImageSizeAndCount` —— 2/23 个有
- `INTConstant` —— 2/23 个有
- `ImageConcatMulti` —— 2/23 个有
- `Bjornulf_ShowInt` —— 1/23 个有
- `GradientImage` —— 1/23 个有
- `ImageFromBatch+` —— 1/23 个有
- `ImagePadKJ` —— 1/23 个有
- `RHHiddenNodes` —— 1/23 个有
- `VHS_GetImageCount` —— 1/23 个有
- `VHS_SelectImages` —— 1/23 个有
- `WanVideoContextOptions` —— 1/23 个有
- `easy indexAnything` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
