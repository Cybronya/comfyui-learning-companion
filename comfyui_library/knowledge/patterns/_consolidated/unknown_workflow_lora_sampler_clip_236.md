---
name: unknown_workflow_lora_sampler_clip_236
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.923
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, PrimitiveStringMultiline, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json, 视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json, 视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json、视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json、视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `LTXVImgToVideoConditionOnly` —— 2/3 个有
- `LTXVPreprocess` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `AudioInfo` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
