---
name: unknown_workflow_upscale_lora_sampler_128
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8555
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CreateVideo, ImageBatch, ImageFromBatch, ImageScale, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, SaveVideo, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/12秒+3050 6G_数字人说话唱歌+InfiniteTalk+低显存+接力帧+官方原生_2061820521767071745.json, 视频生成/图生视频/3050 6G_纯Wan图生视频 I2V 低显存_2061999808293990401.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_128

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/12秒+3050 6G_数字人说话唱歌+InfiniteTalk+低显存+接力帧+官方原生_2061820521767071745.json、视频生成/图生视频/3050 6G_纯Wan图生视频 I2V 低显存_2061999808293990401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `ImageBatch`
- `ImageFromBatch`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderEncode` —— 1/2 个有
- `AudioEncoderLoader` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_LoadAudioUpload` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `WanInfiniteTalkToVideo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
