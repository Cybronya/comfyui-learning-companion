---
name: unknown_workflow_video_sampler_clip_10
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.364739
common_nodes: [Any2ListNode, AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetNode, ImageBatch, ImageFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, ModelPatchLoader, PreviewAny, PrimitiveFloat, SetNode, TextInput_, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy int, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/单人InfiniteTalk官方版工作流_2053384334404530178.json, 数字人/数字人/数字人对口型_2093326224767672322.json, 数字人/数字人/鼎子-InfiniteTalk数字人单人图像驱动-32秒版本_2049680487425290242.json, 视频生成/图生视频/2044648353442566146.json, 视频生成/图生视频/2032340272989872130.json, 视频生成/图生视频/2033825767792054274.json, 视频生成/图生视频/YZ金鱼-单人InfiniteTalk官方版工作流_2016086037126189058.json, 视频生成/图生视频/YZ金鱼-单人InfiniteTalk官方版工作流_2110324012046966785.json, 视频生成/图生视频/2058730777491369986.json, 视频生成/图生视频/2054726545402548226.json, 视频生成/图生视频/2056896899143262209.json, 视频生成/图生视频/2059550534989864961.json, 视频生成/图生视频/2071583964170641410.json, 视频生成/图生视频/2040337221068263426.json, 视频生成/图生视频/2074322051434901506.json, 视频生成/图生视频/2074419354204196865.json, 视频生成/图生视频/2066133635832565762.json, 视频生成/图生视频/数字人口播工作流最长25秒 生产力版_2096966156518248449.json, 视频生成/图生视频/2019751062122536962.json, 视频生成/图生视频/2052234366641815554.json, 视频生成/图生视频/2050130108794580993.json, 视频生成/图生视频/2039859675247677441.json, 视频生成/文生视频/直播搭建带货数字人，_2073822907255578625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（数字人/数字人/单人InfiniteTalk官方版工作流_2053384334404530178.json、数字人/数字人/数字人对口型_2093326224767672322.json、数字人/数字人/鼎子-InfiniteTalk数字人单人图像驱动-32秒版本_2049680487425290242.json、视频生成/图生视频/2044648353442566146.json、视频生成/图生视频/2032340272989872130.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：36%

## 共有节点

全部 23 个 workflow 都包含：
- `Any2ListNode`
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewAny`
- `PrimitiveFloat`
- `SetNode`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy indexAnything`
- `easy int`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 20/23 个有
- `MathExpression|pysssss` —— 20/23 个有
- `PreviewAudio` —— 20/23 个有
- `PreviewImage` —— 20/23 个有
- `Fast Groups Bypasser (rgthree)` —— 4/23 个有
- `Any To String (mtb)` —— 1/23 个有
- `Apply Whisper` —— 1/23 个有
- `IndexTTS2Run` —— 1/23 个有
- `Label (rgthree)` —— 1/23 个有
- `MelBandRoFormerModelLoader` —— 1/23 个有
- `MelBandRoFormerSampler` —— 1/23 个有
- `PrimitiveStringMultiline` —— 1/23 个有
- `SaveAudio` —— 1/23 个有
- `ZML_ImageEncryption` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | normal | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 151/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 normal，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（151/23 个样本）：Steps较低可能导致细节不足
