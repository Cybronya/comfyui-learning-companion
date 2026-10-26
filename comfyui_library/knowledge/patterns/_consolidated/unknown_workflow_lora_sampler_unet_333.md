---
name: unknown_workflow_lora_sampler_unet_333
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.832
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, GetImageSize, ImageCompositeMasked, ImageScale, ImageScaleBy, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ImageToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, QwenImage21Cache, RandomNoise, ResolutionSelector, SamplerCustom, SamplerCustomAdvanced, SaveImage, SaveVideo, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/桌面女友_2110568224566890498.json, 视频生成/图生视频/桌面女友_2111091294834614273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_333

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/桌面女友_2110568224566890498.json、视频生成/图生视频/桌面女友_2111091294834614273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `GetImageSize`
- `ImageCompositeMasked`
- `ImageScale`
- `ImageScaleBy`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ImageToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `QwenImage21Cache`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Wan_Organic_Skin` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
