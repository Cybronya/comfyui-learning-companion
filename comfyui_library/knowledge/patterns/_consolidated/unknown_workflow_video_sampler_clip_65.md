---
name: unknown_workflow_video_sampler_clip_65
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.3703
common_nodes: [Any2ListNode, AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetNode, ImageBatch, ImageFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, ModelPatchLoader, PreviewAny, PrimitiveFloat, SetNode, TextInput_, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy int, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2040337221068263426.json, 视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2074322051434901506.json, 视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2074419354204196865.json, 视频生成/图生视频/图生视频-单人InfiniteTalk官方版工作流_2066133635832565762.json, 视频生成/图生视频/数字人口播工作流最长25秒 生产力版_2096966156518248449.json, 视频生成/图生视频/无限时长视频-InfiniteTalk数字人_2019751062122536962.json, 视频生成/图生视频/无限时长音频+超自然数字人_2052234366641815554.json, 视频生成/图生视频/电商带货版 InfiniteTalk 单人数字人官方版_2050130108794580993.json, 视频生成/图生视频/震撼！效果太牛了！超真实感数字人口播 虚拟人口播 短视频运营利器_2039859675247677441.json, 视频生成/文生视频/直播搭建带货数字人，_2073822907255578625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2040337221068263426.json、视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2074322051434901506.json、视频生成/图生视频/单人数字人InfiniteTalk官方版工作流_2074419354204196865.json、视频生成/图生视频/图生视频-单人InfiniteTalk官方版工作流_2066133635832565762.json、视频生成/图生视频/数字人口播工作流最长25秒 生产力版_2096966156518248449.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：37%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Audio Duration (mtb)` —— 7/10 个有
- `MathExpression|pysssss` —— 7/10 个有
- `PreviewAudio` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `Apply Whisper` —— 1/10 个有
- `IndexTTS2Run` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `MelBandRoFormerModelLoader` —— 1/10 个有
- `MelBandRoFormerSampler` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `ZML_ImageEncryption` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 63/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（63/10 个样本）：Steps较低可能导致细节不足
