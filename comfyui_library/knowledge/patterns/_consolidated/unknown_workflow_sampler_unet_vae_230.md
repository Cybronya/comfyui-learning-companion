---
name: unknown_workflow_sampler_unet_vae_230
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8795
common_nodes: [AILab_QwenVL, AnySwitch, BasicGuider, BasicScheduler, CLIPLoader, Fast Bypasser (rgthree), ImageFromBatch, KSamplerSelect, PreviewAny, PreviewImage, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TTP_text_mix, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMax-H3 图像编辑(图像合成)_2084939205624553474.json, 图片生成/图生图/MiniMax-H3 图像编辑8步加速_2086059655217893377.json, 图片生成/图生图/MiniMax-H3 图像编辑II_2084940373666918402.json, 音频生成/音频生成/MiniMax-H3 图像生成_2084926468798373889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_230

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/MiniMax-H3 图像编辑(图像合成)_2084939205624553474.json、图片生成/图生图/MiniMax-H3 图像编辑8步加速_2086059655217893377.json、图片生成/图生图/MiniMax-H3 图像编辑II_2084940373666918402.json、音频生成/音频生成/MiniMax-H3 图像生成_2084926468798373889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `AnySwitch`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Bypasser (rgthree)`
- `ImageFromBatch`
- `KSamplerSelect`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_text_mix`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `RepeatImageBatch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
