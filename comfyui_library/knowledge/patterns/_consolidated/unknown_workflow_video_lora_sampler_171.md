---
name: unknown_workflow_video_lora_sampler_171
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.602364
common_nodes: [CLIPVisionLoader, DrawViTPose, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/动作迁移优化版_2087223386203312129.json, 视频生成/图生视频/1974720060226973697.json, 视频生成/图生视频/2051347806027296770.json, 视频生成/图生视频/2070541183562113025.json, 视频生成/图生视频/2070540177809952769.json, 视频生成/图生视频/2061344099260784641.json, 视频生成/图生视频/2060930629302312961.json, 视频生成/图生视频/2055559300801679362.json, 视频生成/图生视频/本地开源免费，巴西funk摇僵尸版_2055572704480243714.json, 视频生成/图生视频/2056626842236440577.json, 视频生成/图生视频/2069226848269201409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_171

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/动作迁移优化版_2087223386203312129.json、视频生成/图生视频/1974720060226973697.json、视频生成/图生视频/2051347806027296770.json、视频生成/图生视频/2070541183562113025.json、视频生成/图生视频/2070540177809952769.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
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
- `CR Prompt Text` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `ImageResizeKJv2` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `easy showAnything` —— 10/11 个有
- `JWInteger` —— 9/11 个有
- `PreviewImage` —— 9/11 个有
- `WanVideoTorchCompileSettings` —— 9/11 个有
- `VHS_VideoInfoSource` —— 8/11 个有
- `GetImageSizeAndCount` —— 2/11 个有
- `ImageScale` —— 2/11 个有
- `Int` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `Float` —— 1/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `PoseRetargetPromptHelper` —— 1/11 个有
- `String` —— 1/11 个有
- `VHS_VideoInfoLoaded` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy imageCount` —— 1/11 个有
- `easy indexAnything` —— 1/11 个有
- `ttN float` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
