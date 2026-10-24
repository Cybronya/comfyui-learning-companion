---
name: unknown_workflow_lora_sampler_clip_315
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8185
common_nodes: [BasicScheduler, CLIPTextEncode, CR Text, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RHHiddenNodes, RHLLMChatNode, SamplerCustom, SaveVideo, String, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/【稳定直出40s] 短剧利器  人物三分镜+9宫格剧情 多参 ltx2.3 短剧_2079672663517261825.json, 视频生成/图生视频/超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_315

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【稳定直出40s] 短剧利器  人物三分镜+9宫格剧情 多参 ltx2.3 短剧_2079672663517261825.json、视频生成/图生视频/超牛叉 ltx2.3 电商带货 自定义 人物 产品 背景 动作 话术  去字幕版_2073463647009259520.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `SamplerCustom`
- `SaveVideo`
- `String`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 1/2 个有
- `LiconMSR` —— 1/2 个有
- `PixaromaShowText` —— 1/2 个有
- `Preview from image [Crystools]` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
