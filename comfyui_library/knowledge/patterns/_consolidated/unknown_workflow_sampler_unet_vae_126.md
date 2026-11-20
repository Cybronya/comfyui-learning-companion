---
name: unknown_workflow_sampler_unet_vae_126
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9238
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/minimax_h3(视频编辑)_2088494392536551425.json, 视频生成/图生视频/H3+LightX2V+二采高清参考生视频_2087551828098633730.json, 视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json, 视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2090385859165122562.json, 视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2095839324133744641.json, 视频生成/图生视频/文戏多图参考生视频-MINIMAX-H3 -手动版_2094987834829660161.json, 视频生成/文生视频/MINIMAX-H3 图参考生视频_2091357639291785217.json, 视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json, 视频生成/文生视频/minimax H3-FL2VA单模型_int8_高清重绘_9图3视频3音频版 (1)_2089990413913518082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_126

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/minimax_h3(视频编辑)_2088494392536551425.json、视频生成/图生视频/H3+LightX2V+二采高清参考生视频_2087551828098633730.json、视频生成/图生视频/MINIMAX-H3 多图参考生视频_2093727758789730305.json、视频生成/图生视频/MINIMAX-H3 文戏多图参考生视频-手动版_2092909194184839170.json、视频生成/图生视频/MINIMAX-H3开源 文戏多图参考生视频-手动版_2090385859165122562.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `PT_H3ConcatAVLatent` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `VAEEncodeAudio` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `INTConstant` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 7/10 个有
- `MiniMaxH3AVDecodeT8` —— 7/10 个有
- `ExtendIntermediateSigmas` —— 6/10 个有
- `H3SigmaRefiner` —— 6/10 个有
- `CreateVideo` —— 4/10 个有
- `SaveVideo` —— 4/10 个有
- `VHS_LoadVideo` —— 4/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `SolAttnPatch` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `LTXVConcatAVLatent` —— 1/10 个有
- `LatentUpscaleBy` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/10 个有
- `StringFunction|pysssss` —— 1/10 个有
- `UniBlockSwap` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
