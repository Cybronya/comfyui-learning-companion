---
name: unknown_workflow_video_lora_sampler_155
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.897643
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/动作迁移 4段变装 服装替换 人脸替换 （灵活分段版）_2080965544827772930.json, 平台全量/动作迁移 4段变装 舞蹈复刻_2080324763305730049.json, 平台全量/动作迁移 多图2段转场变装_2084197474503319554.json, 平台全量/动作迁移 多图4段转场变装_2082404662292078594.json, 平台全量/动作迁移+117 172 229 286专门卡点_2085623168382885890.json, 视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json, 视频生成/图生视频/KJ版+动作迁移_2046783552133533698.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092804435218092034.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092862953073758209.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864004770324481.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864044922396674.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864075528237057.json, 视频生成/图生视频/灵活分段生视频 4段变装+动作迁移+服装替换+人脸替换+ 灵活分段版_2089231514004447234.json, 视频生成/图生视频/美女跳舞动作迁移-高质量无偏色无劣化长视频-优化显存不足问题_2018217919682973698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_155

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/动作迁移 4段变装 服装替换 人脸替换 （灵活分段版）_2080965544827772930.json、平台全量/动作迁移 4段变装 舞蹈复刻_2080324763305730049.json、平台全量/动作迁移 多图2段转场变装_2084197474503319554.json、平台全量/动作迁移 多图4段转场变装_2082404662292078594.json、平台全量/动作迁移+117 172 229 286专门卡点_2085623168382885890.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageResizeKJv2`
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
- `GetImageSizeAndCount` —— 13/14 个有
- `WanVideoLoraSelect` —— 13/14 个有
- `ImageBatch` —— 12/14 个有
- `ImageFromBatch` —— 12/14 个有
- `Int` —— 12/14 个有
- `MemoryCleaner` —— 12/14 个有
- `SimpleMath+` —— 11/14 个有
- `Float` —— 10/14 个有
- `GetNode` —— 7/14 个有
- `SetNode` —— 7/14 个有
- `Display Int (rgthree)` —— 3/14 个有
- `WanVideoContextOptions` —— 3/14 个有
- `INTConstant` —— 2/14 个有
- `FloatConstant` —— 1/14 个有
- `PreviewAny` —— 1/14 个有
- `WanVideoTorchCompileSettings` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
