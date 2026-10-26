---
name: unknown_workflow_video_lora
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.516375
common_nodes: [DrawViTPose, GetNode, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader]
problems: []
missing: []
members: [数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json, 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json, 视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json, 视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流_2027391675978485762.json, 视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json, 视频生成/图生视频/Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json, 视频生成/图生视频/Wan2.2+Animate动作迁移-动作模仿-效果好_1993922923654217730.json, 视频生成/图生视频/YJ_APP_WanAnimate_动作迁移v2.5_2034884568989310978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json、视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_1976593221134454786.json、视频生成/图生视频/Wan2.2 Animate V2版-视频转绘动作迁移_2000375060164640769.json、视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流_2027391675978485762.json、视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 8 个 workflow 都包含：
- `DrawViTPose`
- `GetNode`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `CLIPVisionLoader` —— 6/8 个有
- `ImageFromBatch` —— 6/8 个有
- `WanVideoAnimateEmbeds` —— 6/8 个有
- `WanVideoClipVisionEncode` —— 6/8 个有
- `WanVideoSampler` —— 6/8 个有
- `WanVideoTextEncodeCached` —— 6/8 个有
- `WanVideoVAELoader` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `ImageResize+` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `WanVideoSetBlockSwap` —— 5/8 个有
- `WanVideoSetLoRAs` —— 5/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `RH_Nano_Banana_Image2Image` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `String Literal` —— 2/8 个有
- `ttN float` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `easy compare` —— 1/8 个有
- `easy float` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
