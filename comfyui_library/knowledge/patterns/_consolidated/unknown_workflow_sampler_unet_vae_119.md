---
name: unknown_workflow_sampler_unet_vae_119
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.758714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/A-3_MiniMax-H3_文生视频_开源版_2100205096012443649.json, 视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json, 视频生成/文生视频/API专用--MiniMax H3 多参生视频--基础工作流_2084516866738974722.json, 视频生成/文生视频/DG_多参考图+视频参考｜minimax_h3 sage加速视频生成_2086004965662875649.json, 视频生成/文生视频/MINIMAX-H3-多参考生视频_2084144392893452289.json, 视频生成/文生视频/MiniMaxH3三合一简易稳定生产力Pro_2087108217645133826.json, 视频生成/文生视频/minimax_h3 多参考图+视频参考+sage加速_2089945454745313281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_119

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/A-3_MiniMax-H3_文生视频_开源版_2100205096012443649.json、视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json、视频生成/文生视频/API专用--MiniMax H3 多参生视频--基础工作流_2084516866738974722.json、视频生成/文生视频/DG_多参考图+视频参考｜minimax_h3 sage加速视频生成_2086004965662875649.json、视频生成/文生视频/MINIMAX-H3-多参考生视频_2084144392893452289.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `CreateVideo` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `LoadAudio` —— 2/7 个有
- `VideoInfoLoaded` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Getter` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `MiniMaxH3AVDecodeT8` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Setter` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
