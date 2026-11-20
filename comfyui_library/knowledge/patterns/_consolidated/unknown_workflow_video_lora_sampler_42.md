---
name: unknown_workflow_video_lora_sampler_42
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.52163
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/动作迁移自用_2035382692145012738.json, 图片生成/图生图/动作迁移，这个动作高仿，需要高显存跑_2114726342204944386.json, 图片生成/图生图/高精动作模仿，只模仿动作，1_1复刻动作_2115654858492702721.json, 图片生成/图生图/高精动作模仿，只模仿动作，1_1复刻动作_2115676223862042625.json, 平台全量/04动作迁移_2069766883884228609.json, 平台全量/2.2 Animate 人物动作迁移_2055917248015020034.json, 平台全量/Animate动作迁移高清全能V3版(WAN 2.2)-极致真人表情舞蹈动作模仿复刻天花板 人物场景_2075174251463794690.json, 平台全量/Animate舞蹈动作迁移(纸条版）_2058105446375968769.json, 平台全量/Animate舞蹈动作迁移_2045421548575662081.json, 平台全量/DG_(4-3)_animate-kj流-多lora-补针_2039978119695704065.json, 平台全量/DG_(4-3)_animate-kj流-多lora-补针_2041341057002115073.json, 平台全量/WAN 2.2 Animate动作迁移 动作模仿_2046161972512694274.json, 平台全量/WAN_2.2_Animate动作迁移_动作模仿_2110571969199558658.json, 平台全量/WAN_2.2_Animate动作迁移_动作模仿_2111272545948356610.json, 平台全量/Wan 2.2 Animate 动作迁移222_2120040051726966786.json, 平台全量/动作迁移_2029921889031823362.json, 平台全量/动作迁移_2047649067391524865.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json, 视频生成/图生视频/WAN_2.2_Animate动作迁移_动作模仿_2116303163421712385.json, 视频生成/图生视频/Wan 2.2 Animate 人物角色动作迁移_2040732393052573697.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2035583580633571330.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2038260225177817089.json, 视频生成/图生视频/人物跳舞_动作迁移-原图背景_2032081877015728130.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2095534621269254145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/动作迁移自用_2035382692145012738.json、图片生成/图生图/动作迁移，这个动作高仿，需要高显存跑_2114726342204944386.json、图片生成/图生图/高精动作模仿，只模仿动作，1_1复刻动作_2115654858492702721.json、图片生成/图生图/高精动作模仿，只模仿动作，1_1复刻动作_2115676223862042625.json、平台全量/04动作迁移_2069766883884228609.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 25/27 个有
- `ImageBatch` —— 25/27 个有
- `ImageFromBatch` —— 25/27 个有
- `RepeatImageBatch` —— 25/27 个有
- `WanVideoLoraSelect` —— 25/27 个有
- `easy mathInt` —— 25/27 个有
- `CR Text` —— 20/27 个有
- `SimpleMath+` —— 20/27 个有
- `ImpactInt` —— 19/27 个有
- `PurgeVRAM_UTK` —— 19/27 个有
- `easy convertAnything` —— 19/27 个有
- `easy int` —— 19/27 个有
- `Seed (rgthree)` —— 18/27 个有
- `Int` —— 9/27 个有
- `PreviewImage` —— 8/27 个有
- `RHHiddenNodes` —— 8/27 个有
- `VRAMReserver` —— 8/27 个有
- `easy cleanGpuUsed` —— 8/27 个有
- `easy float` —— 8/27 个有
- `easy showAnything` —— 7/27 个有
- `MemoryCleaner` —— 3/27 个有
- `Getter` —— 2/27 个有
- `Note Plus (mtb)` —— 2/27 个有
- `Setter` —— 2/27 个有
- `孤海注释` —— 2/27 个有
- `BlockifyMask` —— 1/27 个有
- `DrawMaskOnImage` —— 1/27 个有
- `GetImageRangeFromBatch` —— 1/27 个有
- `GrowMaskWithBlur` —— 1/27 个有
- `PointsEditor` —— 1/27 个有
- `Primitive integer [Crystools]` —— 1/27 个有
- `SeCModelLoader` —— 1/27 个有
- `SeCVideoSegmentation` —— 1/27 个有
- `Seed` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
