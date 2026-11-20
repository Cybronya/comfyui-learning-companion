---
name: unknown_workflow_video_lora_sampler_668
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.902
common_nodes: [BasicScheduler, CLIPTextEncode, CM_IntToFloat, ConditioningZeroOut, DF_Int_to_Float, DualCLIPLoader, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SamplerCustom, SimpleMath+, UNETLoader, VAEDecode, VAEEncodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, VRAMReserver, VisualizeSigmasKJ, easy getNode, easy setNode, easy showAnything]
problems: []
missing: []
members: [平台全量/LTX2.3视频扩展（视频续写二创）_2058774707096346626.json, 平台全量/LTX2.3视频续写_视频扩展_视频延长_2071750695442796546.json, 数字人/数字人/LTX2.3视频扩展_2051830363772731393.json, 视频生成/文生视频/LTX2.3视频扩展_2050800965619601409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_668

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/LTX2.3视频扩展（视频续写二创）_2058774707096346626.json、平台全量/LTX2.3视频续写_视频扩展_视频延长_2071750695442796546.json、数字人/数字人/LTX2.3视频扩展_2051830363772731393.json、视频生成/文生视频/LTX2.3视频扩展_2050800965619601409.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `DualCLIPLoader`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SamplerCustom`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `VRAMReserver`
- `VisualizeSigmasKJ`
- `easy getNode`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageBatch` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RepeatImageBatch` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `easy compare` —— 2/4 个有
- `easy ifElse` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
