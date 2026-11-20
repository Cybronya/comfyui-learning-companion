---
name: unknown_workflow_video_lora_sampler_615
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6926
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json, 视频生成/图生视频/Wan2.2+Animate动作迁移-动作模仿-效果好_1993922923654217730.json, 视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json, 视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json, 视频生成/图生视频/动作迁移优化版_2087223386203312129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_615

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json、视频生成/图生视频/Wan2.2+Animate动作迁移-动作模仿-效果好_1993922923654217730.json、视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json、视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json、视频生成/图生视频/动作迁移优化版_2087223386203312129.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `ImageResizeKJv2` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `Int` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CM_IntToFloat` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `easy int` —— 2/5 个有
- `ttN float` —— 2/5 个有
- `Float` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `String` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
