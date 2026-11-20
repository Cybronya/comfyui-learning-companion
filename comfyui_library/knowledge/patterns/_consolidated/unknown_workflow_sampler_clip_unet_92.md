---
name: unknown_workflow_sampler_clip_unet_92
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.748083
common_nodes: [BasicScheduler, CLIPTextEncode, DF_Int_to_Float, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelSamplingSD3, SamplerCustom, SetNode, ShowText|pysssss, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VisualizeSigmasKJ, easy positive]
problems: []
missing: []
members: [图片生成/反推提示词/107 LTX2.3图生视频_2035341548103147521.json, 图片生成/反推提示词/60nvmotedaihuo_2052393354213773314.json, 图片生成/反推提示词/63tushengshiping(kuai)_2045718888305922049.json, 图片生成/反推提示词/77tusspyhtb_2052669860135616514.json, 图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json, 图片生成/图生图/LTX2.3图生视频-带语音生成-摇动版_2047251943105503234.json, 图片生成/文生图/LTX2.3解说漫对口型_2052615269197066241.json, 平台全量/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2117227002863382529.json, 平台全量/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2117242219970256897.json, 数字人/数字人/LTX2.3 双人对话！图生视频音画同步 自用_2050188003259236354.json, 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2047878626800050178.json, 视频生成/图生视频/LTX2.3-电商带货-上传图片自动生成-音画同步-Distilled-1.1-蒸馏稳定版_2052289650873651201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/107 LTX2.3图生视频_2035341548103147521.json、图片生成/反推提示词/60nvmotedaihuo_2052393354213773314.json、图片生成/反推提示词/63tushengshiping(kuai)_2045718888305922049.json、图片生成/反推提示词/77tusspyhtb_2052669860135616514.json、图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LTXVAudioVAEDecode` —— 11/12 个有
- `LTXVEmptyLatentAudio` —— 11/12 个有
- `PrimitiveInt` —— 10/12 个有
- `ConditioningZeroOut` —— 9/12 个有
- `StringFunction|pysssss` —— 9/12 个有
- `VHS_VideoCombine` —— 9/12 个有
- `AILab_QwenVL_Advanced` —— 8/12 个有
- `JjkText` —— 8/12 个有
- `LayerUtility: BooleanOperatorV2` —— 8/12 个有
- `LayerUtility: If ` —— 8/12 个有
- `LayerUtility: NumberCalculatorV2` —— 8/12 个有
- `PathchSageAttentionKJ` —— 8/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `Text` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `CreateVideo` —— 3/12 个有
- `JoinStrings` —— 3/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `RTXVideoSuperResolution` —— 3/12 个有
- `SaveVideo` —— 3/12 个有
- `SeedGeneratorMira` —— 3/12 个有
- `TTResolutionSelector` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `llama_cpp_instruct_adv` —— 3/12 个有
- `llama_cpp_model_loader` —— 3/12 个有
- `llama_cpp_parameters` —— 3/12 个有
- `CustomAddLabel` —— 2/12 个有
- `LTXVAudioVAEEncode` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `LoraLoader|pysssss` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `Switch` —— 1/12 个有
- `TT_img_enc_v2` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 305 | 305 - 305 | 11 | 100% |
| 高度 | 24 | 24 - 24 | 11 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 305，观测区间 305 - 305，11 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，11 个样本，取值集中（一致性 100%）
