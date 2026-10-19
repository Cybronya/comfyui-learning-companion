---
name: unknown_workflow_video_lora_sampler_222
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.868
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, SamplerCustom, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2058444254300696577.json, 视频生成/图生视频/2070137230106124289.json, 视频生成/图生视频/2060633763377410049.json, 视频生成/图生视频/2055882037822795778.json, 视频生成/图生视频/2069942311760523265.json, 视频生成/图生视频/2057812163363950593.json, 视频生成/图生视频/2069309703959695362.json, 视频生成/图生视频/2073463668316323840.json, 视频生成/图生视频/2076823460927598594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2058444254300696577.json、视频生成/图生视频/2070137230106124289.json、视频生成/图生视频/2060633763377410049.json、视频生成/图生视频/2055882037822795778.json、视频生成/图生视频/2069942311760523265.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `PrimitiveBoolean` —— 8/9 个有
- `LTXDirectorGuide` —— 7/9 个有
- `LTXVAudioVAEEncode` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `MelBandRoFormerModelLoader` —— 7/9 个有
- `MelBandRoFormerSampler` —— 7/9 个有
- `PreviewAudio` —— 7/9 个有
- `SetLatentNoiseMask` —— 7/9 个有
- `SolidMask` —— 7/9 个有
- `LTXDirector` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `GuHaiAutoImageSplit` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `CS-LTXGridDirector` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `PreviewAny` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `RH_LLMAPI_Pro_Node` —— 3/9 个有
- `YusuLTXDirectorGuide` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `LTXVChunkFeedForward` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
