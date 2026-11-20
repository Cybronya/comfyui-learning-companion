---
name: unknown_workflow_video_lora_sampler_819
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.482
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RepeatImageBatch, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [平台全量/wan animate动作迁移-基础工作流V1_2052003743067062273.json, 数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json, 视频生成/图生视频/Wan2.2 Animate动作迁移（操作方便）_2019075587062636545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_819

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/wan animate动作迁移-基础工作流V1_2052003743067062273.json、数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json、视频生成/图生视频/Wan2.2 Animate动作迁移（操作方便）_2019075587062636545.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RepeatImageBatch`
- `SetNode`
- `VHS_LoadVideo`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 2/3 个有
- `ImageBatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `WanVideoEasyCache` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
