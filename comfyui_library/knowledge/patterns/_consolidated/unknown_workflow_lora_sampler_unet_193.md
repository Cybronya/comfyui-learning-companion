---
name: unknown_workflow_lora_sampler_unet_193
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.65125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json, comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json, comfyui-workflow-templates-json/video_minimax_h3_r2v.json, 平台全量/MiniMax-H3多控制信号融合工作流_2109678679352766465.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_193

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json、comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json、comfyui-workflow-templates-json/video_minimax_h3_r2v.json、平台全量/MiniMax-H3多控制信号融合工作流_2109678679352766465.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/4 个有
- `GetVideoComponents` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `MiniMaxH3FunControlNetApply` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Video Slice` —— 2/4 个有
- `622cceeb-7ba3-4dd9-b0e8-00066c5222a4` —— 1/4 个有
- `Canny` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DepthAnything_V3` —— 1/4 个有
- `DownloadAndLoadDepthAnythingV3Model` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `MiniMaxH3AddGuide` —— 1/4 个有
- `RTDETR_detect` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有
- `SDPoseDrawKeypoints` —— 1/4 个有
- `SDPoseKeypointExtractor` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
