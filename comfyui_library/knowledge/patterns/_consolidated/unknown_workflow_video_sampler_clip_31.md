---
name: unknown_workflow_video_sampler_clip_31
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.397
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageFromBatch, KSampler, LoadAudio, LoadImage, ModelPatchLoader, PreviewAny, SetNode, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/41duikouxin_2050023991196307457.json, 图片生成/文生图/最新增强版InfiniteTalk无限时长数字偶像Pro对口型工作流 V3.0_2033995490647351297.json, 数字人/数字人/4超真实感数字人口播 虚拟人口播 短视频运营利器_2074112151891046401.json, 数字人/数字人/AI代码侠土豆-官流全自动循环流数字人_2018705105180168194.json, 数字人/数字人/Fishaudio+单人InfiniteTalk官方版工作流东源自然数字人长视频_2033511522793693185.json, 数字人/数字人/InfiniteTalk （官方流）图片驱动、数字人单人对口型_2019726268798869506.json, 数字人/数字人/InfiniteTalk数字人_2065228820231311362.json, 数字人/数字人/Jian Wei 单人InfiniteTalk官方版工作流（无限流）_2037806085641347074.json, 数字人/数字人/【海小川AIGC】-InfiniteTalk数字人_2031910229612437505.json, 数字人/数字人/三七—单人口播（sanqi）_2039235549533310978.json, 数字人/数字人/单人InfiniteTalk官方版工作流_2053384334404530178.json, 数字人/数字人/单人InfiniteTalk官方版工作流_2066423963697373186.json, 数字人/数字人/图生对口型-全自动循环-数字人-模板（001）_2074755476276994049.json, 数字人/数字人/官流全自动循环流数字人_2019433133229215745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/41duikouxin_2050023991196307457.json、图片生成/文生图/最新增强版InfiniteTalk无限时长数字偶像Pro对口型工作流 V3.0_2033995490647351297.json、数字人/数字人/4超真实感数字人口播 虚拟人口播 短视频运营利器_2074112151891046401.json、数字人/数字人/AI代码侠土豆-官流全自动循环流数字人_2018705105180168194.json、数字人/数字人/Fishaudio+单人InfiniteTalk官方版工作流东源自然数字人长视频_2033511522793693185.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 14 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageFromBatch`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewAny`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy indexAnything`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any2ListNode` —— 13/14 个有
- `AudioCrop` —— 13/14 个有
- `DiffusionModelLoaderKJ` —— 13/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/14 个有
- `ImageBatch` —— 10/14 个有
- `MathExpression|pysssss` —— 10/14 个有
- `PreviewAudio` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `PrimitiveFloat` —— 10/14 个有
- `TextInput_` —— 10/14 个有
- `easy int` —— 10/14 个有
- `easy forLoopEnd` —— 5/14 个有
- `easy forLoopStart` —— 5/14 个有
- `ColorMatch` —— 4/14 个有
- `Float` —— 4/14 个有
- `Int` —— 4/14 个有
- `PainterAudioCut` —— 4/14 个有
- `SimpleMath+` —— 4/14 个有
- `Text` —— 4/14 个有
- `easy batchAnything` —— 4/14 个有
- `easy lengthAnything` —— 4/14 个有
- `Audio To Text (mtb)` —— 1/14 个有
- `Bjornulf_ShowInt` —— 1/14 个有
- `CR Prompt Text` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `FishS2VoiceCloneTTS` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `Load Whisper (mtb)` —— 1/14 个有
- `LoadVideo` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有
- `PlaySound|pysssss` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `UNETLoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | normal | - | 14 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 101/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 normal，14 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（101/14 个样本）：Steps较低可能导致细节不足
