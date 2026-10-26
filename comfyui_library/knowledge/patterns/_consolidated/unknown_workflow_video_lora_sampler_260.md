---
name: unknown_workflow_video_lora_sampler_260
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.885667
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageSizeAndCount, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json, 视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092804435218092034.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092862953073758209.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864004770324481.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864044922396674.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864075528237057.json, 视频生成/图生视频/动作迁移优化版_2087223386203312129.json, 视频生成/图生视频/灵活分段生视频 4段变装+动作迁移+服装替换+人脸替换+ 灵活分段版_2089231514004447234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_260

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json、视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json、视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092804435218092034.json、视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092862953073758209.json、视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864004770324481.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `GetNode` —— 8/9 个有
- `ImageResizeKJv2` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `WanVideoLoraSelect` —— 8/9 个有
- `Float` —— 7/9 个有
- `ImageBatch` —— 6/9 个有
- `ImageFromBatch` —— 6/9 个有
- `MemoryCleaner` —— 6/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `CM_IntToFloat` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ImageScale` —— 1/9 个有
- `String` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
