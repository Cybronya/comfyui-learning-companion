---
name: unknown_workflow_video_lora_sampler_480
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.531
common_nodes: [CLIPVisionLoader, CM_FloatToInt, ComfyMathExpression, DrawViTPose, GetNode, ImageResizeKJv2, Int, LoadImage, MinNode, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything, 图像缩放V2_孤海]
problems: []
missing: []
members: [视频生成/图生视频/Animate动作迁移-自适应最终版（支持1080P）_2067136692997414914.json, 视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067232861400428545.json, 视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067890192308072449.json, 视频生成/图生视频/动作迁移_2072250195357818881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_480

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Animate动作迁移-自适应最终版（支持1080P）_2067136692997414914.json、视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067232861400428545.json、视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067890192308072449.json、视频生成/图生视频/动作迁移_2072250195357818881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `ComfyMathExpression`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MinNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GIMMVFI_interpolate` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `InversionDemoLazySwitch` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
