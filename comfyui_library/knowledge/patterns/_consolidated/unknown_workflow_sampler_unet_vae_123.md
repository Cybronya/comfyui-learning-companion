---
name: unknown_workflow_sampler_unet_vae_123
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.849333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json, 视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json, 视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json, 视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json, 视频生成/文生视频/MiniMax H3文生视频（Sage加速）2608_2085826303927869442.json, 视频生成/文生视频/MiniMax-H3文生视频人物类特效数字人工作流_2090000867746476033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生视频Org开源版_2084176715890380801.json、视频生成/文生视频/MiniMax H3文生视频_2087738976793882626.json、视频生成/文生视频/MiniMax H3文生视频_2089703538363555842.json、视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json、视频生成/文生视频/MiniMax H3文生视频（Sage加速）2608_2085826303927869442.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `EasyCache` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `FlashVSRInitPipe` —— 1/6 个有
- `FlashVSRNodeAdv` —— 1/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `SpectrumSDXL` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
