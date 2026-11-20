---
name: unknown_workflow_video_lora_sampler_180
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.370182
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageBatch, ImageFromBatch, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/凤希AI单数字人无限时长对口型（默认80秒）_2021523374865915905.json, 数字人/数字人/InfiniteTalk-Comfyui官流长视频无衰减_2017911925878820866.json, 数字人/数字人/infinitetalk官流_2018550714829643777.json, 视频生成/图生视频/InfiniteTalk 音频驱动 无衰减超长视频生成  一键数字人视频生成_2019318204899794946.json, 视频生成/图生视频/InfiniteTalk-Comfyui官流长视频无衰减_2018199752789204993.json, 视频生成/图生视频/InfiniteTalk-Comfyui官流长视频无衰减_2018680802581684225.json, 视频生成/图生视频/InfiniteTalk-Comfyui官流长视频无衰减_2018684694845460482.json, 视频生成/图生视频/InfiniteTalk-Comfyui官流长视频无衰减版，需要更多长度直接复制采样即可！_2027300224661721090.json, 视频生成/图生视频/【阿良绘】数字人长视频无衰减（分段生成）InfiniteTalk_2020782430164094977.json, 视频生成/图生视频/新InfiniteTalk-Comfyui官方流多段组合无限长视频数字人_2018872300161998849.json, 视频生成/图生视频/最新infinite模型长视频无色差 20s视频只要12分钟_2018523773288321026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_180

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/凤希AI单数字人无限时长对口型（默认80秒）_2021523374865915905.json、数字人/数字人/InfiniteTalk-Comfyui官流长视频无衰减_2017911925878820866.json、数字人/数字人/infinitetalk官流_2018550714829643777.json、视频生成/图生视频/InfiniteTalk 音频驱动 无衰减超长视频生成  一键数字人视频生成_2019318204899794946.json、视频生成/图生视频/InfiniteTalk-Comfyui官流长视频无衰减_2018199752789204993.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：37%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 10/11 个有
- `AudioSeparation` —— 10/11 个有
- `ConditioningZeroOut` —— 10/11 个有
- `INTConstant` —— 10/11 个有
- `ModelSamplingSD3` —— 10/11 个有
- `PreviewAudio` —— 10/11 个有
- `CreateVideo` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `MelBandRoFormerModelLoader` —— 1/11 个有
- `MelBandRoFormerSampler` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `StringConcatenate` —— 1/11 个有
- `easy imageScaleDown` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 87/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（87/11 个样本）：Steps较低可能导致细节不足
