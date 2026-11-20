---
name: unknown_workflow_video_lora_sampler_430
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.541857
common_nodes: [CLIPVisionLoader, ComfyMathExpression, DrawViTPose, GetNode, ImageResizeKJv2, Int, LoadImage, MinNode, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything, 图像缩放V2_孤海]
problems: []
missing: []
members: [平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json, 数字人/数字人/动作迁移 后背摇专用Lite版 低显存可用_2067544740731641857.json, 数字人/数字人/动作迁移 后背摇专用pro版 丝滑长视频_2067780097234526209.json, 视频生成/图生视频/Animate动作迁移-自适应最终版（支持1080P）_2067136692997414914.json, 视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067232861400428545.json, 视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067890192308072449.json, 视频生成/图生视频/动作迁移_2072250195357818881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_430

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/动作迁移Animate2.0Fast  15s稳定版  低显存可用_2066846449693974530.json、数字人/数字人/动作迁移 后背摇专用Lite版 低显存可用_2067544740731641857.json、数字人/数字人/动作迁移 后背摇专用pro版 丝滑长视频_2067780097234526209.json、视频生成/图生视频/Animate动作迁移-自适应最终版（支持1080P）_2067136692997414914.json、视频生成/图生视频/一键动作迁移_一键跳舞_抖音_2067232861400428545.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `DownloadAndLoadGIMMVFIModel` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `GIMMVFI_interpolate` —— 5/7 个有
- `ImpactSwitch` —— 5/7 个有
- `InversionDemoLazySwitch` —— 5/7 个有
- `PrimitiveBoolean` —— 5/7 个有
- `WanVideoLoraSelect` —— 5/7 个有
- `easy anythingIndexSwitch` —— 5/7 个有
- `CM_FloatToInt` —— 4/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
