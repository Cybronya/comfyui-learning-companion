---
name: unknown_workflow_sampler_clip_unet_108
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7497
common_nodes: [BasicScheduler, CLIPTextEncode, DF_Int_to_Float, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelSamplingSD3, SamplerCustom, SetNode, ShowText|pysssss, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VisualizeSigmasKJ, easy positive]
problems: []
missing: []
members: [图片生成/反推提示词/107 LTX2.3图生视频_2035341548103147521.json, 图片生成/反推提示词/60nvmotedaihuo_2052393354213773314.json, 图片生成/反推提示词/63tushengshiping(kuai)_2045718888305922049.json, 图片生成/反推提示词/77tusspyhtb_2052669860135616514.json, 图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json, 图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json, 图片生成/文生图/LTX2.3解说漫对口型_2052615269197066241.json, 数字人/数字人/LTX2.3 双人对话！图生视频音画同步 自用_2050188003259236354.json, 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2047878626800050178.json, 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/107 LTX2.3图生视频_2035341548103147521.json、图片生成/反推提示词/60nvmotedaihuo_2052393354213773314.json、图片生成/反推提示词/63tushengshiping(kuai)_2045718888305922049.json、图片生成/反推提示词/77tusspyhtb_2052669860135616514.json、图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DF_Int_to_Float`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ModelSamplingSD3`
- `SamplerCustom`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 9/10 个有
- `LTXVEmptyLatentAudio` —— 9/10 个有
- `PrimitiveInt` —— 8/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `StringFunction|pysssss` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `AILab_QwenVL_Advanced` —— 6/10 个有
- `JjkText` —— 6/10 个有
- `LayerUtility: BooleanOperatorV2` —— 6/10 个有
- `LayerUtility: If ` —— 6/10 个有
- `LayerUtility: NumberCalculatorV2` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `Text` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `CreateVideo` —— 3/10 个有
- `JoinStrings` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `RTXVideoSuperResolution` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `SeedGeneratorMira` —— 3/10 个有
- `TTResolutionSelector` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 3/10 个有
- `llama_cpp_model_loader` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `CustomAddLabel` —— 2/10 个有
- `LTXVAudioVAEEncode` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `LoraLoader|pysssss` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `Switch` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 305 | 305 - 305 | 9 | 100% |
| 高度 | 24 | 24 - 24 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 305，观测区间 305 - 305，9 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，9 个样本，取值集中（一致性 100%）
