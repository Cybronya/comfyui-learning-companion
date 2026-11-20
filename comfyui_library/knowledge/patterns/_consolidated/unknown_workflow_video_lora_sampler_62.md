---
name: unknown_workflow_video_lora_sampler_62
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.6224
common_nodes: [ControlNextGetPoses, GetImageSizeAndCount, GetNode, ImageResizeKJ, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], SetNode, SimpleMath+, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/动作迁移_1991004865675599874.json, 视频生成/图生视频/wan2.2+Fun Control动作迁移_1955151856064499714.json, 视频生成/图生视频/wan2.2+bro-lora+动作迁移_1968333951213416449.json, 视频生成/图生视频/wan2.2+动作迁移_1958329470274977793.json, 视频生成/图生视频/wan2.2+动作迁移_1963046419189968898.json, 视频生成/图生视频/wan2.2-动作迁移-超真实_2053734676421988353.json, 视频生成/图生视频/wan2.2-动作迁移-超真实_2054742996398157826.json, 视频生成/图生视频/wan2.2-真实感-动作迁移_2052994688696762369.json, 视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json, 视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2042038693006938114.json, 视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2042491077948612610.json, 视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2045027083465789442.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_1955471370547335170.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_2058912825199906818.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_2060032983922470914.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_2062871890934460417.json, 视频生成/图生视频/真实感-wan2.2+动作迁移_2080550651473514498.json, 视频生成/文生视频/wan2.2  图生视频动作迁移_1956657681140473857.json, 视频生成/文生视频/【动作迁移】真实感-wan2.2_1956961863289245697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/动作迁移_1991004865675599874.json、视频生成/图生视频/wan2.2+Fun Control动作迁移_1955151856064499714.json、视频生成/图生视频/wan2.2+bro-lora+动作迁移_1968333951213416449.json、视频生成/图生视频/wan2.2+动作迁移_1958329470274977793.json、视频生成/图生视频/wan2.2+动作迁移_1963046419189968898.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 20 个 workflow 都包含：
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
- `ColorMatch` —— 19/20 个有
- `ImageConcatMulti` —— 19/20 个有
- `ImageFromBatch` —— 19/20 个有
- `Int` —— 19/20 个有
- `Primitive float [Crystools]` —— 19/20 个有
- `RHHiddenNodes` —— 19/20 个有
- `ShowText|pysssss` —— 19/20 个有
- `Text Concatenate` —— 19/20 个有
- `WanVideoBlockSwap` —— 19/20 个有
- `WanVideoSLG` —— 19/20 个有
- `ImpactSwitch` —— 18/20 个有
- `WanVideoSetBlockSwap` —— 18/20 个有
- `RH_Captioner` —— 16/20 个有
- `ImpactInt` —— 3/20 个有
- `LayerUtility: JoyCaptionBeta1` —— 3/20 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 3/20 个有
- `easy showAnything` —— 3/20 个有
- `WanVideoLoraSelect` —— 2/20 个有
- `WanVideoLoraSelectMulti` —— 2/20 个有
- `WanVideoModelLoader` —— 2/20 个有
- `GetImageRangeFromBatch` —— 1/20 个有
- `ImageBatchMulti` —— 1/20 个有
- `ImageUpscaleWithModel` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `RepeatImageBatch` —— 1/20 个有
- `UpscaleModelLoader` —— 1/20 个有
- `WanVideoEmptyEmbeds` —— 1/20 个有
- `easy forLoopEnd` —— 1/20 个有
- `easy forLoopStart` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
