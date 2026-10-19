---
name: unknown_workflow_sampler_unet_vae_23
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.863176
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 FL2VA 文生视频_2085360642407616513.json, 视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json, 视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json, 视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json, 视频生成/文生视频/MiniMax H3 Larry Turbo 加速_2086411713435492353.json, 视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json, 视频生成/文生视频/MiniMax H3 LightX2V Turbo 加速_2086332815146311681.json, 视频生成/文生视频/MiniMax H3 Ref2VA 剧本直出｜六段式自动生成+自动校验 · 9图参考成片 · H3原生音画同步版_2088206128625840130.json, 视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json, 视频生成/文生视频/MiniMax H3 首尾帧图生视频_2084850865038520322.json, 视频生成/文生视频/MiniMax H3_文生视频工作流_2084504955460866050.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速24GB通用版_2086411696771522561.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速48GB高配版_2086411679377743873.json, 视频生成/文生视频/MiniMax H3图生视频6倍加速80GB满配版_2086411651821170689.json, 视频生成/文生视频/MiniMax H3多图参考生视频（速度提升2倍+提示词自动优化）_2086492553964253185.json, 视频生成/文生视频/多图参考生视频（速度提升2倍+提示词自动优化）_2086268908348207105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_23

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 FL2VA 文生视频_2085360642407616513.json、视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json、视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json、视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `LoadImage` —— 14/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `MiniMaxH3ImageToVideo` —— 13/17 个有
- `ImageResizeKJv2` —— 9/17 个有
- `LoraLoaderModelOnly` —— 8/17 个有
- `PathchSageAttentionKJ` —— 8/17 个有
- `EasyCache` —— 6/17 个有
- `MiniMaxH3BlockCacheT8` —— 4/17 个有
- `MiniMaxH3ReferenceToVideo` —— 4/17 个有
- `RHLLMChatNode` —— 3/17 个有
- `SolAttnPatch` —— 3/17 个有
- `easy showAnything` —— 3/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/17 个有
- `ShowText|pysssss` —— 2/17 个有
- `Text Multiline` —— 2/17 个有
- `JjkText` —— 1/17 个有
- `PatchFlashAttentionKJ` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `SpectrumApplyMiniMaxH3` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
