---
name: unknown_workflow_sampler_vae_31
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.871667
common_nodes: [CFGGuider, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json, 视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json, 视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json, 视频生成/图生视频/LTX2.3数字人V2—支持双人，自动计算帧数_2073315948735586306.json, 视频生成/图生视频/LTX2.3数字人V3 Prompt Relay提示词分段控制_2073319876273463297.json, 视频生成/图生视频/LTX2.3数字人—支持双人_2073313777977745410.json, 视频生成/图生视频/danotebook-ltx2.3-digital_2062522880226848770.json, 视频生成/图生视频/【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json, 视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_31

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_MSR  电商产品_人物 唱歌跳舞   是参考视频生成新的视频 适合爆款视频清洗_2070081600632741890.json、视频生成/图生视频/LTX-2.3_MSR RV2V参考生视频_2073325475514114050.json、视频生成/图生视频/LTX-2.3_MSR V2多参数字人_2078871582214279170.json、视频生成/图生视频/LTX2.3数字人V2—支持双人，自动计算帧数_2073315948735586306.json、视频生成/图生视频/LTX2.3数字人V3 Prompt Relay提示词分段控制_2073319876273463297.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 8/9 个有
- `LTXVPreprocess` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `ResizeImagesByLongerEdge` —— 8/9 个有
- `ComfyMathExpression` —— 7/9 个有
- `LoadAudio` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `PrimitiveInt` —— 7/9 个有
- `TrimAudioDuration` —— 7/9 个有
- `CheckpointLoaderSimple` —— 6/9 个有
- `LTXVImgToVideoInplace` —— 6/9 个有
- `LTXVLatentUpsampler` —— 6/9 个有
- `LatentUpscaleModelLoader` —— 6/9 个有
- `ResizeImageMaskNode` —— 6/9 个有
- `VAEDecodeTiled` —— 6/9 个有
- `PrimitiveBoolean` —— 5/9 个有
- `AudioInfo` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `LTX2_NAG` —— 3/9 个有
- `LTXAddVideoICLoRAGuide` —— 3/9 个有
- `LTXICLoRALoaderModelOnly` —— 3/9 个有
- `LiconMSR` —— 3/9 个有
- `LowVRAMCheckpointLoader` —— 3/9 个有
- `PrimitiveFloat` —— 3/9 个有
- `PromptRelayEncode` —— 3/9 个有
- `VAEDecode` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `GetImageSize` —— 2/9 个有
- `HeartMuLa_Generate` —— 2/9 个有
- `HeartMuLa_Transcribe` —— 2/9 个有
- `LTXVImgToVideoConditionOnly` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `SaveAudio` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text _O` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `MelBandRoFormerModelLoader` —— 1/9 个有
- `MelBandRoFormerSampler` —— 1/9 个有
- `PromptRelaySmartEncode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
