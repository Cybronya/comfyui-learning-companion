---
name: unknown_workflow_sampler_unet_vae_70
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.841
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json, 视频生成/文生视频/MiniMax H3｜Sol Attention｜首尾帧+参考生视频_2098331649598640129.json, 视频生成/文生视频/MiniMax+H3+文生视频_2084466075869208578.json, 视频生成/文生视频/MiniMax+H3+首帧图生视频_2084850825154875394.json, 视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json, 视频生成/文生视频/MiniMax-H3-参考生视频_2085243192571686914.json, 视频生成/文生视频/MiniMax_H3 多参考图生视频（可本地运行）_2084295736807739394.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2084608321469898754.json, 视频生成/文生视频/Minimax H3 - 多参视频生成_2092164049516711938.json, 视频生成/文生视频/Minimax H3 加速工作流_2085691765964754946.json, 视频生成/文生视频/Minimax H3 文生视频_2089487806417694721.json, 视频生成/文生视频/Minimax H3-多功能工作流 _自动_手动提示词切换版_2085177847324438530.json, 视频生成/文生视频/minimax H3-FL2VA单模型_int8_高清重绘_9图3视频3音频版 (1)_2089990413913518082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_70

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json、视频生成/文生视频/MiniMax H3｜Sol Attention｜首尾帧+参考生视频_2098331649598640129.json、视频生成/文生视频/MiniMax+H3+文生视频_2084466075869208578.json、视频生成/文生视频/MiniMax+H3+首帧图生视频_2084850825154875394.json、视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `ComfyMathExpression` —— 11/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `ResolutionSelector` —— 11/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `MiniMaxH3ReferenceToVideo` —— 8/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `EasyCache` —— 5/13 个有
- `LoadAudio` —— 4/13 个有
- `MiniMaxH3ImageToVideo` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `Any Switch (rgthree)` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `ImageResizeKJv2` —— 2/13 个有
- `MiniMaxH3AudioConditioningT8` —— 2/13 个有
- `RHLLMChatNode` —— 2/13 个有
- `SolAttnPatch` —— 2/13 个有
- `StringFunction|pysssss` —— 2/13 个有
- `UniBlockSwap` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `INTConstant` —— 1/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `MiniMaxH3BlockCacheT8` —— 1/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/13 个有
- `MiniMaxH3MemoryEfficientSolAttentionPatch` —— 1/13 个有
- `PT_H3ConcatAVLatent` —— 1/13 个有
- `VAEEncode` —— 1/13 个有
- `VAEEncodeAudio` —— 1/13 个有
- `VHS_VideoCombine` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
