---
name: unknown_workflow_lora_sampler_clip_131
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.866333
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 Licon-MSR长镜头版_2064866981614014466.json, 视频生成/图生视频/Ltx2.3--Licon-MSR--全能参考生视频_2063821663644512257.json, 视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2068123966476210177.json, 视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2100051839176765442.json, 视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2100132977069084673.json, 视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2100931168920227841.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 Licon-MSR长镜头版_2064866981614014466.json、视频生成/图生视频/Ltx2.3--Licon-MSR--全能参考生视频_2063821663644512257.json、视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2068123966476210177.json、视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2100051839176765442.json、视频生成/图生视频/image2+LTX-MSR多参3分镜图生视频_2100132977069084673.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
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
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 5/6 个有
- `StringReplace` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `RH_RhartImageG2ImageToImage` —— 4/6 个有
- `TextConcatenate_UTK` —— 4/6 个有
- `easy imageSplitGrid` —— 4/6 个有
- `easy indexAnything` —— 4/6 个有
- `CreateVideo` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `GoogleTranslator` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `SaveVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 6 | 100% |
| 高度 | 50 | 50 - 50 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，6 个样本，取值集中（一致性 100%）
- 高度 中位数 50，观测区间 50 - 50，6 个样本，取值集中（一致性 100%）
