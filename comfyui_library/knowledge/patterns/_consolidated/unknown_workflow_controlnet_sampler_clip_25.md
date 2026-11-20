---
name: unknown_workflow_controlnet_sampler_clip_25
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92725
common_nodes: [AIO_Preprocessor, BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, ImageResizeKJ, Int, KSamplerSelect, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [平台全量/取出第一帧转绘（局部重绘+IP-Adapter）_1906969797710553090.json, 平台全量/取出第一帧转绘（局部重绘+lora）_1906959797013422082.json, 平台全量/取出第一帧转绘（整体重绘+IP-Adapter精准风格迁移）_1906975038485176321.json, 平台全量/取出第一帧转绘（整体重绘+IP-Adapter）_1906971554637389826.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/取出第一帧转绘（局部重绘+IP-Adapter）_1906969797710553090.json、平台全量/取出第一帧转绘（局部重绘+lora）_1906959797013422082.json、平台全量/取出第一帧转绘（整体重绘+IP-Adapter精准风格迁移）_1906975038485176321.json、平台全量/取出第一帧转绘（整体重绘+IP-Adapter）_1906971554637389826.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `ImageResizeKJ`
- `Int`
- `KSamplerSelect`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `ACN_AdvancedControlNetApply_v2` —— 3/4 个有
- `IPAdapterUnifiedLoader` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `IPAdapterAdvanced` —— 2/4 个有
- `ImageToMask` —— 2/4 个有
- `InpaintModelConditioning` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `IPAdapterMS` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.6 - 0.8 | 4 | 90% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 90%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
