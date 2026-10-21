---
name: unknown_workflow_sampler_unet_vae_194
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.837333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 网格图参考生视频_2084506699142094850.json, 视频生成/图生视频/Minimax H3 多图参考生视频_2084688978254581762.json, 视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 网格图参考生视频_2084506699142094850.json、视频生成/图生视频/Minimax H3 多图参考生视频_2084688978254581762.json、视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MiniMaxH3BlockCacheT8` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `AnySwitch` —— 1/3 个有
- `DuckHideNode` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有
- `TTP_text_mix` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
