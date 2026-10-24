---
name: unknown_workflow_sampler_unet_vae_68
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.876846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 FL2VA 文生视频_2085360642407616513.json, 视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json, 视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json, 视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json, 视频生成/文生视频/MiniMax H3 Larry Turbo 加速_2086411713435492353.json, 视频生成/文生视频/MiniMax H3 Larry+attention+cache 满血加速版_2086444236236484609.json, 视频生成/文生视频/MiniMax H3 LightX2V Turbo 加速_2086332815146311681.json, 视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速优化版_2091125673569112066.json, 视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速版_2090781925186301953.json, 视频生成/文生视频/MiniMax H3 文生视频_2084544656423088130.json, 视频生成/文生视频/MiniMax_H3多图参考视频生成_2095691860177149954.json, 视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_68

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 FL2VA 文生视频_2085360642407616513.json、视频生成/文生视频/MiniMax H3 FL2VA-文生视频-优化版_2088069601203671041.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-图像 音频参考生视频  DiT int8加速版_2090416308562251777.json、视频生成/文生视频/MiniMax H3 INT8 W4A8 加速_2086411704518406146.json、视频生成/文生视频/MiniMax H3 Larry + Sageattention加速_2086411824722956290.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
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
- `PrimitiveFloat` —— 11/13 个有
- `ResolutionSelector` —— 11/13 个有
- `LoadImage` —— 10/13 个有
- `MiniMaxH3ImageToVideo` —— 9/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `ImageResizeKJv2` —— 7/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `EasyCache` —— 6/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `MiniMaxH3ReferenceToVideo` —— 4/13 个有
- `ShowAnything|Mie` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `LoadAudio` —— 3/13 个有
- `DF_Int_to_Float` —— 2/13 个有
- `ImpactSwitch` —— 2/13 个有
- `Int` —— 2/13 个有
- `SolAttnPatch` —— 2/13 个有
- `intToFloat _O` —— 2/13 个有
- `JjkText` —— 1/13 个有
- `PatchFlashAttentionKJ` —— 1/13 个有
- `ReroutePrimitive|pysssss` —— 1/13 个有
- `SpectrumApplyMiniMaxH3` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
