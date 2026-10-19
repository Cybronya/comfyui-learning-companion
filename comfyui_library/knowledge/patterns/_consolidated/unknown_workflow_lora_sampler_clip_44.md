---
name: unknown_workflow_lora_sampler_clip_44
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.681
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageBatch, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAELoader, WanInfiniteTalkToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2042859514055106562.json, 视频生成/图生视频/2066742321412136962.json, 视频生成/图生视频/2018130782031716354.json, 视频生成/图生视频/2018136601624317954.json, 视频生成/图生视频/2018500999857577985.json, 视频生成/图生视频/2019387715191578626.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2042859514055106562.json、视频生成/图生视频/2066742321412136962.json、视频生成/图生视频/2018130782031716354.json、视频生成/图生视频/2018136601624317954.json、视频生成/图生视频/2018500999857577985.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/6 个有
- `CreateVideo` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `AudioConcat` —— 1/6 个有
- `CLIPVisionEncode` —— 1/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `FL_Audio_Crop` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `FlashVSRInitPipe` —— 1/6 个有
- `FlashVSRNodeAdv` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
