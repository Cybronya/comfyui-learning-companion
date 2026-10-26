---
name: unknown_workflow_video_lora_sampler_186
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.560091
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json, 视频生成/图生视频/KJ版+动作迁移_2046783552133533698.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json, 视频生成/图生视频/Wan 2.2 Animate 人物角色动作迁移_2040732393052573697.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2035583580633571330.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2038260225177817089.json, 视频生成/图生视频/人物跳舞_动作迁移-原图背景_2032081877015728130.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2095534621269254145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_186

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json、视频生成/图生视频/KJ版+动作迁移_2046783552133533698.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 11 个 workflow 都包含：
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
- `GetNode` —— 10/11 个有
- `ImageBatch` —— 10/11 个有
- `ImageFromBatch` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `SimpleMath+` —— 10/11 个有
- `WanVideoContextOptions` —— 10/11 个有
- `WanVideoLoraSelect` —— 10/11 个有
- `BatchCount+` —— 9/11 个有
- `CR Text` —— 9/11 个有
- `ImpactInt` —— 9/11 个有
- `PurgeVRAM_UTK` —— 9/11 个有
- `RepeatImageBatch` —— 9/11 个有
- `Seed (rgthree)` —— 9/11 个有
- `VHS_VideoInfo` —— 9/11 个有
- `easy convertAnything` —— 9/11 个有
- `easy int` —— 9/11 个有
- `easy mathInt` —— 9/11 个有
- `GetImageSizeAndCount` —— 2/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `Float` —— 1/11 个有
- `FloatConstant` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `Int` —— 1/11 个有
- `MemoryCleaner` —— 1/11 个有
- `PreviewAny` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
