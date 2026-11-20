---
name: unknown_workflow_sampler_unet_vae_260
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7645
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3・图生 _ 文生・四合一视频工作流_2084274079045083138.json, 视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json, 视频生成/文生视频/MiniMaxH3文生・四合一视频工作流・图生ENGENG_2087094142475268097.json, 视频生成/文生视频/Minimax H3 全系列工作流【AI小王子】_2084162640192032770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_260

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3・图生 _ 文生・四合一视频工作流_2084274079045083138.json、视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json、视频生成/文生视频/MiniMaxH3文生・四合一视频工作流・图生ENGENG_2087094142475268097.json、视频生成/文生视频/Minimax H3 全系列工作流【AI小王子】_2084162640192032770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `MiniMaxH3ImageToVideo` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `RegexReplace` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `VRAM_Debug` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `easy string` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `ttN int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
