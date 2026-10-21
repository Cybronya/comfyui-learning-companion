---
name: unknown_workflow_sampler_clip_unet_250
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVPreprocess, LTXVScheduler, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/ltx25_flf2v_videoonly_2091465515121340417.json, 视频生成/图生视频/ltx25_i2v_videoonly_2091431518022496258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_250

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/ltx25_flf2v_videoonly_2091465515121340417.json、视频生成/图生视频/ltx25_i2v_videoonly_2091431518022496258.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVAddGuide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
