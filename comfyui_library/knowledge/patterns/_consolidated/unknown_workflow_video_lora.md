---
name: unknown_workflow_video_lora
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.574444
common_nodes: [DrawViTPose, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader]
problems: []
missing: []
members: [平台全量/真人动作迁移工作流_2094023690349531137.json, 数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json, 视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流_2027391675978485762.json, 视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流搭建-初级篇_2050899529087635457.json, 视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json, 视频生成/图生视频/【阡陌】Wan2.2 Animate KJ版人物动作表情迁移_1980910878105227266.json, 视频生成/图生视频/万能动作表情_姿势迁移唱歌跳舞加长版_2020345629322518529.json, 视频生成/图生视频/人物动作偏移工作流进阶版_2070126355764830210.json, 视频生成/图生视频/姿势参考_1980236223493136385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/真人动作迁移工作流_2094023690349531137.json、数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json、视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流_2027391675978485762.json、视频生成/图生视频/Wan2.2 Animate人物动作迁移工作流搭建-初级篇_2050899529087635457.json、视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 9 个 workflow 都包含：
- `DrawViTPose`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `ImageFromBatch` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `CLIPVisionLoader` —— 6/9 个有
- `ImageResize+` —— 6/9 个有
- `WanVideoAnimateEmbeds` —— 6/9 个有
- `WanVideoClipVisionEncode` —— 6/9 个有
- `WanVideoSampler` —— 6/9 个有
- `WanVideoTextEncodeCached` —— 6/9 个有
- `WanVideoVAELoader` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `WanVideoSetBlockSwap` —— 3/9 个有
- `WanVideoSetLoRAs` —— 3/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `ImpactInt` —— 2/9 个有
- `Int` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `Textbox` —— 2/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `ImageConcanate` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `WanVideoContextOptions` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
