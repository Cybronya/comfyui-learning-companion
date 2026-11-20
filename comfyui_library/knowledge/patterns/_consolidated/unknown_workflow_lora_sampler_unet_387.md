---
name: unknown_workflow_lora_sampler_unet_387
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.772
common_nodes: [AudioCrop, BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, MultiTextConcatenate, PreviewAudio, PrimitiveFloat, PrimitiveStringMultiline, ProcessString, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, SimpleMath+, UNETLoader, VAEDecodeAudio, VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/H3_声音克隆_2117482049799020545.json, 平台全量/全能参考H3 声音克隆_2118277197566926849.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_387

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/H3_声音克隆_2117482049799020545.json、平台全量/全能参考H3 声音克隆_2118277197566926849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MultiTextConcatenate`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ProcessString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
