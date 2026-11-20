---
name: unknown_workflow_video_lora_sampler_288
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5234
common_nodes: [BatchCount+, CLIPVisionLoader, GetNode, ImageResizeKJv2, LazySwitch1way, LoadImage, RHHiddenNodes, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy compare, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Animate长视频——动作迁移稳定版_1978123000795029506.json, 视频生成/图生视频/Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json, 视频生成/图生视频/Wan2.2+Animate动作迁移 实现20秒以上视频生成 支持多人动作 脸部表情迁移高质量输出_2073705930453245954.json, 视频生成/图生视频/Wan2.2+Animate实现20秒以上视频生成，支持多人动作 脸部表情迁移高质量输出_2017135847610519553.json, 视频生成/图生视频/Wan2.2+Animate循环长视频_2003473617683922946.json, 视频生成/图生视频/Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2006380310623162369.json, 视频生成/图生视频/Wan2.2+Animate支持20秒+支持多人动作迁移高质量_2053406061868138498.json, 视频生成/图生视频/Wan2.2+Animate支持5秒+支持多人动作迁移速度慢但是高质量_2007482787619672065.json, 视频生成/图生视频/Wan2.2结合Animate实现20秒以上视频生成，支持多人动作 脸部表情迁移高质量输出_2017109030061219842.json, 视频生成/图生视频/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_2007836084251660289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_288

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate长视频——动作迁移稳定版_1978123000795029506.json、视频生成/图生视频/Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json、视频生成/图生视频/Wan2.2+Animate动作迁移 实现20秒以上视频生成 支持多人动作 脸部表情迁移高质量输出_2073705930453245954.json、视频生成/图生视频/Wan2.2+Animate实现20秒以上视频生成，支持多人动作 脸部表情迁移高质量输出_2017135847610519553.json、视频生成/图生视频/Wan2.2+Animate循环长视频_2003473617683922946.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 10 个 workflow 都包含：
- `BatchCount+`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `LazySwitch1way`
- `LoadImage`
- `RHHiddenNodes`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy compare`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 9/10 个有
- `ImageFromBatch` —— 9/10 个有
- `PoseAndFaceDetection` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `RepeatImageBatch` —— 9/10 个有
- `easy cleanGpuUsed` —— 9/10 个有
- `Int` —— 8/10 个有
- `VHS_VideoInfo` —— 7/10 个有
- `WanVideoTeaCache` —— 6/10 个有
- `DrawViTPose` —— 4/10 个有
- `OnnxDetectionModelLoader` —— 4/10 个有
- `CM_IntToFloat` —— 3/10 个有
- `easy batchAnything` —— 3/10 个有
- `easy forLoopEnd` —— 3/10 个有
- `easy forLoopStart` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `ImageBatchMulti` —— 2/10 个有
- `easy int` —— 2/10 个有
- `GemmaAPITextEncode` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `WanVideoLoraSelectMulti` —— 1/10 个有
- `WanVideoModelLoader` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
