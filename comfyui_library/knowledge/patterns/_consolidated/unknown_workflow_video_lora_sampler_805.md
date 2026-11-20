---
name: unknown_workflow_video_lora_sampler_805
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.615667
common_nodes: [CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, SamplerCustom, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json, 视频生成/图生视频/LTX2.3 V2V Camera 视频到视频摄像机参考-图生视频工作流_2071613148762824706.json, 视频生成/图生视频/⨝LTX2.3 IC LORA-Camera Control 运镜控制，大师运镜、视频编辑、运镜迁移_2074498263339855873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_805

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/LTX2.3 V2V CrossView Prompt  镜头切换视频生视频工作流_2077360035210027010.json、视频生成/图生视频/LTX2.3 V2V Camera 视频到视频摄像机参考-图生视频工作流_2071613148762824706.json、视频生成/图生视频/⨝LTX2.3 IC LORA-Camera Control 运镜控制，大师运镜、视频编辑、运镜迁移_2074498263339855873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SamplerCustom`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `LTXVAudioVAEDecode` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `LTXVAudioVAELoader` —— 1/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `VHS_LoadVideoPath` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
