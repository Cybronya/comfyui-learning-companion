---
name: unknown_workflow_video_lora_sampler_649
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.937
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DF_Int_to_Float, DualCLIPLoader, Int, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, SamplerCustom, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, VisualizeSigmasKJ, easy getNode, easy setNode]
problems: []
missing: []
members: [数字人/数字人/LTX2.3视频扩展_2051830363772731393.json, 视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json, 视频生成/文生视频/LTX2.3视频扩展_2050800965619601409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_649

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/LTX2.3视频扩展_2051830363772731393.json、视频生成/文生视频/LTX2.3-亲子对话-文生视频工作流--搞笑视频_2083450669406711809.json、视频生成/文生视频/LTX2.3视频扩展_2050800965619601409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `DualCLIPLoader`
- `Int`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SamplerCustom`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `VisualizeSigmasKJ`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/3 个有
- `LTXVAudioVAEEncode` —— 2/3 个有
- `LTXVAudioVideoMask` —— 2/3 个有
- `VAEEncodeTiled` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `EmptyLTXVLatentVideo` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXVEmptyLatentAudio` —— 1/3 个有
- `LTXVImgToVideoConditionOnly` —— 1/3 个有
- `LTXVPreprocess` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
