---
name: unknown_workflow_sampler_clip_unet_92
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8165
common_nodes: [BasicScheduler, CLIPTextEncode, DualCFGGuider, InstructPixToPixConditioning, KSamplerSelect, LoadImage, QuadrupleCLIPLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/hidream_e1_1.json, comfyui-workflow-templates-json/hidream_e1_full.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/hidream_e1_1.json、comfyui-workflow-templates-json/hidream_e1_full.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCFGGuider`
- `InstructPixToPixConditioning`
- `KSamplerSelect`
- `LoadImage`
- `QuadrupleCLIPLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
