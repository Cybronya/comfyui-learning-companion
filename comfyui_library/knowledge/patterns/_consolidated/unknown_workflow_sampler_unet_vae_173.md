---
name: unknown_workflow_sampler_unet_vae_173
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.763667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, EasyCache, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3・图生 _ 文生・四合一视频工作流_2084274079045083138.json, 视频生成/文生视频/MiniMax H3图生视频工作流_2084631760146620417.json, 视频生成/文生视频/MiniMaxH3文生・四合一视频工作流・图生ENGENG_2087094142475268097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3・图生 _ 文生・四合一视频工作流_2084274079045083138.json、视频生成/文生视频/MiniMax H3图生视频工作流_2084631760146620417.json、视频生成/文生视频/MiniMaxH3文生・四合一视频工作流・图生ENGENG_2087094142475268097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
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
- `ComfySwitchNode` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RegexReplace` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `VRAM_Debug` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `easy string` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `SpectrumSDXL` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
