---
name: unknown_workflow_lora_sampler_clip_123
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9385
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json, 视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064287550000422914.json, 视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064563859888885761.json, 视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json, 视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json, 视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/LTX-2.3_MSR RV2V邪修之视频参考生视频_2079329374129713153.json、视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064287550000422914.json、视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064563859888885761.json、视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json、视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 5/6 个有
- `LTX2_NAG` —— 4/6 个有
- `LTXVAudioVAEEncode` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `PromptRelayEncode` —— 4/6 个有
- `SetLatentNoiseMask` —— 4/6 个有
- `SolidMask` —— 4/6 个有
- `GetImageSize` —— 3/6 个有
- `LTXVImgToVideoConditionOnly` —— 3/6 个有
- `LTXVPreprocess` —— 3/6 个有
- `ResizeImagesByLongerEdge` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `LTXVEmptyLatentAudio` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `AudioInfo` —— 1/6 个有
- `ComfyMathExpression` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | - | 2 | 100% |
| 高度 | 50 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
