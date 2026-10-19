---
name: unknown_workflow_video_lora_sampler_78
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.685235
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json, 视频生成/图生视频/2046783552133533698.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json, 视频生成/图生视频/2040732393052573697.json, 视频生成/图生视频/2035583580633571330.json, 视频生成/图生视频/2038260225177817089.json, 视频生成/图生视频/2032081877015728130.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092804435218092034.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092862953073758209.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864004770324481.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864044922396674.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864075528237057.json, 视频生成/图生视频/1890311094009835522.json, 视频生成/图生视频/2026837951593844738.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2095534621269254145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json、视频生成/图生视频/2046783552133533698.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 17 个 workflow 都包含：
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
- `ImageBatch` —— 16/17 个有
- `ImageFromBatch` —— 16/17 个有
- `WanVideoLoraSelect` —— 16/17 个有
- `GetNode` —— 15/17 个有
- `SetNode` —— 15/17 个有
- `SimpleMath+` —— 15/17 个有
- `WanVideoContextOptions` —— 11/17 个有
- `BatchCount+` —— 10/17 个有
- `RepeatImageBatch` —— 10/17 个有
- `VHS_VideoInfo` —— 10/17 个有
- `easy mathInt` —— 10/17 个有
- `CR Text` —— 9/17 个有
- `ImpactInt` —— 9/17 个有
- `PurgeVRAM_UTK` —— 9/17 个有
- `Seed (rgthree)` —— 9/17 个有
- `easy convertAnything` —— 9/17 个有
- `easy int` —— 9/17 个有
- `GetImageSizeAndCount` —— 7/17 个有
- `Int` —— 7/17 个有
- `MemoryCleaner` —— 7/17 个有
- `Float` —— 6/17 个有
- `Note Plus (mtb)` —— 2/17 个有
- `ComfyMathExpression` —— 1/17 个有
- `FloatConstant` —— 1/17 个有
- `GoohaiUniversalSlider` —— 1/17 个有
- `INTConstant` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有
- `孤海注释` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
