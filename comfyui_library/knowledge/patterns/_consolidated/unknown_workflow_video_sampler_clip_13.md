---
name: unknown_workflow_video_sampler_clip_13
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.409792
common_nodes: [Any2ListNode, Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageFromBatch, KSampler, LoadAudio, LoadImage, ModelPatchLoader, PreviewAny, SetNode, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy indexAnything, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/41duikouxin_2050023991196307457.json, 图片生成/文生图/最新增强版InfiniteTalk无限时长数字偶像Pro对口型工作流 V3.0_2033995490647351297.json, 平台全量/单人对口型  InfiniteTalk官方版工作流_2082389624382640129.json, 平台全量/固定机位口播1.0_2116749028733046786.json, 平台全量/固定机位口播2.0_2117270218337771521.json, 数字人/数字人/4超真实感数字人口播 虚拟人口播 短视频运营利器_2074112151891046401.json, 数字人/数字人/AI代码侠土豆-官流全自动循环流数字人_2018705105180168194.json, 数字人/数字人/【海小川AIGC】-InfiniteTalk数字人_2031910229612437505.json, 数字人/数字人/图生对口型-全自动循环-数字人-模板（001）_2074755476276994049.json, 数字人/数字人/官流全自动循环流数字人_2019433133229215745.json, 数字人/数字人/直播搭建带货数字人，_2073461491130519553.json, 数字人/数字人/自用InfiniteTalk工作流（搬运自”YZ金鱼“）_2075866010003005441.json, 数字人/数字人/超真实数字人口播_2059744867659640833.json, 数字人/数字人/鼎子-InfiniteTalk数字人单人图像驱动-32秒版本_2049680487425290242.json, 视频生成/图生视频/1FINAL-SZR-SING-TALK - YZ金鱼-InfiniteTalk_2044648353442566146.json, 视频生成/图生视频/InfiniteTalk-comfui官方版工作流_2032340272989872130.json, 视频生成/图生视频/InfiniteTalk图片数字人对口型_2033825767792054274.json, 视频生成/图生视频/YZ金鱼-单人InfiniteTalk官方版工作流_2016086037126189058.json, 视频生成/图生视频/YZ金鱼-单人InfiniteTalk官方版工作流_2110324012046966785.json, 视频生成/图生视频/克隆自己_克隆他人声音做数字人长视频（官流稳定版）_2026533442996932609.json, 视频生成/图生视频/图生对口型-rh-全自动循环-数字人-模板_2019209695591927810.json, 视频生成/图生视频/高质量图片对口型数字人（电商、带货、短剧等实用场景）_2036376532473614337.json, 视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2039982412008005633.json, 视频生成/文生视频/图生对口型-全自动循环-数字人-模板_2065338337707253762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/反推提示词/41duikouxin_2050023991196307457.json、图片生成/文生图/最新增强版InfiniteTalk无限时长数字偶像Pro对口型工作流 V3.0_2033995490647351297.json、平台全量/单人对口型  InfiniteTalk官方版工作流_2082389624382640129.json、平台全量/固定机位口播1.0_2116749028733046786.json、平台全量/固定机位口播2.0_2117270218337771521.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 24 个 workflow 都包含：
- `Any2ListNode`
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
- `AudioCrop` —— 23/24 个有
- `DiffusionModelLoaderKJ` —— 20/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/24 个有
- `PreviewAudio` —— 16/24 个有
- `ImageBatch` —— 15/24 个有
- `MathExpression|pysssss` —— 15/24 个有
- `PreviewImage` —— 15/24 个有
- `PrimitiveFloat` —— 15/24 个有
- `TextInput_` —— 15/24 个有
- `easy int` —— 15/24 个有
- `ColorMatch` —— 9/24 个有
- `Float` —— 9/24 个有
- `Int` —— 9/24 个有
- `PainterAudioCut` —— 9/24 个有
- `SimpleMath+` —— 9/24 个有
- `Text` —— 9/24 个有
- `easy batchAnything` —— 9/24 个有
- `easy forLoopEnd` —— 9/24 个有
- `easy forLoopStart` —— 9/24 个有
- `easy lengthAnything` —— 9/24 个有
- `ImageResizeKJv2` —— 4/24 个有
- `LoraLoaderModelOnly` —— 4/24 个有
- `UNETLoader` —— 4/24 个有
- `Fast Groups Bypasser (rgthree)` —— 3/24 个有
- `CR Prompt Text` —— 1/24 个有
- `CR Text` —— 1/24 个有
- `FB_Qwen3TTSVoiceClone` —— 1/24 个有
- `ImpactSwitch` —— 1/24 个有
- `RunningHub_VoxCPM_Generate` —— 1/24 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/24 个有
- `VHS_AudioToVHSAudio` —— 1/24 个有
- `VHS_LoadVideo` —— 1/24 个有
- `VHS_VHSAudioToAudio` —— 1/24 个有
- `WhisperSTT` —— 1/24 个有
- `ZML_ImageEncryption` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | normal | - | 24 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 124/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 normal，24 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（124/24 个样本）：Steps较低可能导致细节不足
