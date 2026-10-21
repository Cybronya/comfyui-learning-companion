---
name: unknown_workflow_video_lora_sampler_46
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.616571
common_nodes: [ControlNextGetPoses, GetImageSizeAndCount, GetNode, ImageResizeKJ, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], SetNode, SimpleMath+, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [Primitive float [Crystools], Primitive integer [Crystools], SimpleMath+, Text Concatenate, Text Multiline]
members: [图片生成/文生图/动作迁移_1991004865675599874.json, 视频生成/图生视频/1956657681140473857.json, 视频生成/图生视频/1955151856064499714.json, 视频生成/图生视频/1968333951213416449.json, 视频生成/图生视频/1958329470274977793.json, 视频生成/图生视频/1963046419189968898.json, 视频生成/图生视频/2053734676421988353.json, 视频生成/图生视频/2054742996398157826.json, 视频生成/图生视频/2052994688696762369.json, 视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json, 视频生成/图生视频/2042038693006938114.json, 视频生成/图生视频/2042491077948612610.json, 视频生成/图生视频/2045027083465789442.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json, 视频生成/图生视频/1955471370547335170.json, 视频生成/图生视频/2058912825199906818.json, 视频生成/图生视频/2060032983922470914.json, 视频生成/图生视频/2062871890934460417.json, 视频生成/图生视频/2080550651473514498.json, 视频生成/文生视频/1956657681140473857.json, 视频生成/文生视频/1956961863289245697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/动作迁移_1991004865675599874.json、视频生成/图生视频/1956657681140473857.json、视频生成/图生视频/1955151856064499714.json、视频生成/图生视频/1968333951213416449.json、视频生成/图生视频/1958329470274977793.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 21 个 workflow 都包含：
- `ControlNextGetPoses`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 20/21 个有
- `ImageConcatMulti` —— 20/21 个有
- `ImageFromBatch` —— 20/21 个有
- `Int` —— 20/21 个有
- `Primitive float [Crystools]` —— 20/21 个有
- `RHHiddenNodes` —— 20/21 个有
- `ShowText|pysssss` —— 20/21 个有
- `Text Concatenate` —— 20/21 个有
- `WanVideoBlockSwap` —— 20/21 个有
- `WanVideoSLG` —— 20/21 个有
- `ImpactSwitch` —— 19/21 个有
- `WanVideoSetBlockSwap` —— 19/21 个有
- `RH_Captioner` —— 17/21 个有
- `ImpactInt` —— 3/21 个有
- `LayerUtility: JoyCaptionBeta1` —— 3/21 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 3/21 个有
- `easy showAnything` —— 3/21 个有
- `WanVideoLoraSelect` —— 2/21 个有
- `WanVideoLoraSelectMulti` —— 2/21 个有
- `WanVideoModelLoader` —— 2/21 个有
- `GetImageRangeFromBatch` —— 1/21 个有
- `ImageBatchMulti` —— 1/21 个有
- `ImageUpscaleWithModel` —— 1/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/21 个有
- `LayerUtility: PurgeVRAM V2` —— 1/21 个有
- `RepeatImageBatch` —— 1/21 个有
- `UpscaleModelLoader` —— 1/21 个有
- `WanVideoEmptyEmbeds` —— 1/21 个有
- `easy forLoopEnd` —— 1/21 个有
- `easy forLoopStart` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Primitive float [Crystools]、Primitive integer [Crystools]、SimpleMath+、Text Concatenate、Text Multiline
