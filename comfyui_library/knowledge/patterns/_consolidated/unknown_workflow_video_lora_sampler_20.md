---
name: unknown_workflow_video_lora_sampler_20
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.614517
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json, 视频生成/图生视频/KJ版+动作迁移_2046783552133533698.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json, 视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json, 视频生成/图生视频/Wan 2.2 Animate 人物角色动作迁移_2040732393052573697.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2035583580633571330.json, 视频生成/图生视频/Wan 2.2 Animate 动作迁移_2038260225177817089.json, 视频生成/图生视频/人物跳舞_动作迁移-原图背景_2032081877015728130.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092804435218092034.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092862953073758209.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864004770324481.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864044922396674.json, 视频生成/图生视频/动作迁移 服装变换 4段变装（灵活分段版）_2092864075528237057.json, 视频生成/图生视频/口哨舞_1890311094009835522.json, 视频生成/图生视频/跑高精细的用这个动作迁移，动作高仿，需要高显存跑_2056901108127330305.json, 视频生成/图生视频/跑高精细的用这个动作迁移，还是这个版本动作模仿的好_2074305725089804289.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2078408880727609346.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2078464035640668161.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099818962723889154.json, 视频生成/图生视频/高精动作模仿 只模仿动作跳舞模仿 1：1复刻动作_2099839308415979522.json, 视频生成/图生视频/高精动作模仿_2080183256737210370.json, 视频生成/图生视频/高精动作模仿，只模仿动作，1：1复刻动作_2077952800755118081.json, 视频生成/图生视频/高精动作模仿，只模仿动作，1：1复刻动作_2078675405703307266.json, 视频生成/图生视频/高精细1_1复刻动作迁移，动作模仿plus版_2084239498350776322.json, 视频生成/图生视频/高精细1：1复刻动作模仿，动作迁移_2078075351011520514.json, 视频生成/图生视频/高质量动作迁移人物精细 高级强化版_2083007472301858818.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2026837951593844738.json, 视频生成/图生视频/🤷Wan 2.2 Animate 人物动作迁移优化版🤷_2095534621269254145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/4段变装+动作迁移+服装替换+人脸替换+（灵活分段版）_2087418361050390530.json、视频生成/图生视频/KJ版+动作迁移_2046783552133533698.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108866123113525249.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2108896219048271874.json、视频生成/图生视频/WAN 2.2 Animate动作迁移 动作模仿_2109578513186643969.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 29 个 workflow 都包含：
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
- `ImageBatch` —— 28/29 个有
- `ImageFromBatch` —— 28/29 个有
- `WanVideoLoraSelect` —— 28/29 个有
- `GetNode` —— 27/29 个有
- `SetNode` —— 27/29 个有
- `WanVideoContextOptions` —— 23/29 个有
- `BatchCount+` —— 22/29 个有
- `RepeatImageBatch` —— 22/29 个有
- `VHS_VideoInfo` —— 22/29 个有
- `easy mathInt` —— 22/29 个有
- `Int` —— 19/29 个有
- `MemoryCleaner` —— 19/29 个有
- `SimpleMath+` —— 15/29 个有
- `PreviewImage` —— 13/29 个有
- `easy cleanGpuUsed` —— 13/29 个有
- `RHHiddenNodes` —— 12/29 个有
- `VRAMReserver` —— 12/29 个有
- `easy float` —— 12/29 个有
- `easy showAnything` —— 12/29 个有
- `CR Text` —— 9/29 个有
- `ImpactInt` —— 9/29 个有
- `PurgeVRAM_UTK` —— 9/29 个有
- `Seed (rgthree)` —— 9/29 个有
- `easy convertAnything` —— 9/29 个有
- `easy int` —— 9/29 个有
- `GetImageSizeAndCount` —— 7/29 个有
- `Float` —— 6/29 个有
- `Note Plus (mtb)` —— 2/29 个有
- `ComfyMathExpression` —— 1/29 个有
- `FloatConstant` —— 1/29 个有
- `GoohaiUniversalSlider` —— 1/29 个有
- `INTConstant` —— 1/29 个有
- `PreviewAny` —— 1/29 个有
- `孤海注释` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
