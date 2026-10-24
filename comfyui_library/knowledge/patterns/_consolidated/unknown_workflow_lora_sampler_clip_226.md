---
name: unknown_workflow_lora_sampler_clip_226
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.783
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, GrowMaskWithBlur, KSamplerSelect, LayerMask: MaskPreview, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux一键修手（自动+手动）_1905570787984871426.json, 图片生成/图生图/Flux修手（手动）_1905597707249963010.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux一键修手（自动+手动）_1905570787984871426.json、图片生成/图生图/Flux修手（手动）_1905597707249963010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 1/2 个有
- `BlendInpaint` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CutForInpaint` —— 1/2 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/2 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `easy imageChooser` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
