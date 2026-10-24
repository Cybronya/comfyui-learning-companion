---
name: unknown_workflow_video_lora_sampler_525
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.613
common_nodes: [BatchCount+, CLIPVisionLoader, DrawViTPose, ImageBatch, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, RepeatImageBatch, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy float, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json, 视频生成/图生视频/动作迁移_2045891229149302786.json, 视频生成/图生视频/啊癫 最新 动作迁移，高清Wan2.2 Animate动作迁移V44-1_2032851375377354753.json, 视频生成/图生视频/新版Wan2.2 Animate动作迁移-跳舞视频专用工作流V5_2035706111285792769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_525

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/【动作迁移】wan22animate_单人版_2098717884812976129.json、视频生成/图生视频/动作迁移_2045891229149302786.json、视频生成/图生视频/啊癫 最新 动作迁移，高清Wan2.2 Animate动作迁移V44-1_2032851375377354753.json、视频生成/图生视频/新版Wan2.2 Animate动作迁移-跳舞视频专用工作流V5_2035706111285792769.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `RepeatImageBatch`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy float`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VRAMReserver` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `easy int` —— 3/4 个有
- `MemoryCleaner` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `SDPoseOODLoader` —— 2/4 个有
- `SDPoseOODProcessor` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `VHS_LoadVideoFFmpeg` —— 2/4 个有
- `CM_FloatToInt` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `DownloadAndLoadNLFModel` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `Int` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LazySwitch1way` —— 1/4 个有
- `NLFPredict` —— 1/4 个有
- `PoseDetectionVitPoseToDWPose` —— 1/4 个有
- `RenderNLFPoses` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `YOLOModelLoader` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
