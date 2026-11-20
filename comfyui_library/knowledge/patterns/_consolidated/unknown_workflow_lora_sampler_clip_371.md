---
name: unknown_workflow_lora_sampler_clip_371
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8315
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, GetVideoComponents, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConditioning, LTXVCropGuides, LoadVideo, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [平台全量/LTX-2.3_ICLoRA_HDR_Distilled 视频转视频（V2V）HDR 增强工作流_2054561103870480386.json, 平台全量/ltx视频超清放大_2053706378300141569.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_371

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX-2.3_ICLoRA_HDR_Distilled 视频转视频（V2V）HDR 增强工作流_2054561103870480386.json、平台全量/ltx视频超清放大_2053706378300141569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LoadVideo`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `GemmaAPITextEncode` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LTXVHDRDecodePostprocess` —— 1/2 个有
- `LTXVTiledVAEDecode` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VAEDecodeTiled` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
