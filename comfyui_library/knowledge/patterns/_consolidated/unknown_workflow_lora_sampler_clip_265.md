---
name: unknown_workflow_lora_sampler_clip_265
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.965
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, GetVideoComponents, ImageScaleToMaxDimension, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConditioning, LTXVLoopingSampler, LTXVSpatioTemporalTiledVAEDecode, LoadVideo, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SaveVideo, VAEEncodeTiled, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/LTX-2.3-视频超清无损放大_2090946784209231873.json, 平台全量/LTX-2_V2V_Detailer（视频生视频放大-细节添加）_2009167763440410626.json, 平台全量/视频生视频放大-细节添加_2042479853584257025.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_265

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/LTX-2.3-视频超清无损放大_2090946784209231873.json、平台全量/LTX-2_V2V_Detailer（视频生视频放大-细节添加）_2009167763440410626.json、平台全量/视频生视频放大-细节添加_2042479853584257025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `GetVideoComponents`
- `ImageScaleToMaxDimension`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVLoopingSampler`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SaveVideo`
- `VAEEncodeTiled`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `LTXVGemmaCLIPModelLoader` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `RIFEInterpolation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
