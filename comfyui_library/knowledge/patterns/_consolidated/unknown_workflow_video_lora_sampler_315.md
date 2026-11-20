---
name: unknown_workflow_video_lora_sampler_315
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.52075
common_nodes: [CLIPVisionLoader, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Seed (rgthree), VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/qy-简化_2035638502787911682.json, 视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json, 视频生成/图生视频/图生视频-【丝滑变装】-【动作迁移】-【人物替换】Wan2.2 Animate 分段队列_2063193185219858434.json, 视频生成/图生视频/美女穿搭一键换衣 变装 +动作迁移 +动作模仿_2066425187536564226.json, 视频生成/图生视频/顶级视频换人（变装跳舞专用）_2099576921075052545.json, 视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻  无加密节点_2109231949574402050.json, 视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻 9月15日 无加密节点_2099712198623981570.json, 视频生成/文生视频/【丝滑变装】&【动作迁移】&【人物替换】_2100616978972102658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_315

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/qy-简化_2035638502787911682.json、视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json、视频生成/图生视频/图生视频-【丝滑变装】-【动作迁移】-【人物替换】Wan2.2 Animate 分段队列_2063193185219858434.json、视频生成/图生视频/美女穿搭一键换衣 变装 +动作迁移 +动作模仿_2066425187536564226.json、视频生成/图生视频/顶级视频换人（变装跳舞专用）_2099576921075052545.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Seed (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BodyRatioMapperSDPoseRender` —— 7/8 个有
- `CheckpointLoaderSimple` —— 7/8 个有
- `SDPoseKeypointExtractor` —— 7/8 个有
- `WanVideoContextOptions` —— 7/8 个有
- `BlockifyMask` —— 6/8 个有
- `CLIPTextEncode` —— 6/8 个有
- `DrawMaskOnImage` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `GrowMaskWithBlur` —— 6/8 个有
- `PlaySound|pysssss` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `SAM3_Detect` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `BBoxYOLO` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `SegmentQueueRunner` —— 5/8 个有
- `YOLOModelLoader` —— 5/8 个有
- `ImageBlend` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `MaskToImage` —— 4/8 个有
- `WanVideoEncode` —— 4/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/8 个有
- `WanVideoUni3C_embeds` —— 4/8 个有
- `Primitive integer [Crystools]` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `CR Text` —— 1/8 个有
- `FastUnsharpSharpen` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `SDPoseOODLoader` —— 1/8 个有
- `SDPoseOODProcessor` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
