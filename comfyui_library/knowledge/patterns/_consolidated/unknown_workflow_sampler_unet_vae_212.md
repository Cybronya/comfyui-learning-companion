---
name: unknown_workflow_sampler_unet_vae_212
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.749857
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3-二采不崩高清_2092900896651964417.json, 视频生成/图生视频/Minimax H3 Ref 顶级多参，不偏色，不油光_2101574282240421890.json, 视频生成/图生视频/Minimax H3 人类机甲重组变身 工作流_2106558180313624577.json, 视频生成/图生视频/Minimax H3 人类机甲重组变身 工作流_2115720488566743041.json, 视频生成/图生视频/Minimax H3 地铁变装_2096857300303699969.json, 视频生成/图生视频/Minimax H3 多参打斗V2_2096763661741281282.json, 视频生成/图生视频/Minimax_H3_Ref_顶级多参，不偏色，不油光_2114879175034236930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_212

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3-二采不崩高清_2092900896651964417.json、视频生成/图生视频/Minimax H3 Ref 顶级多参，不偏色，不油光_2101574282240421890.json、视频生成/图生视频/Minimax H3 人类机甲重组变身 工作流_2106558180313624577.json、视频生成/图生视频/Minimax H3 人类机甲重组变身 工作流_2115720488566743041.json、视频生成/图生视频/Minimax H3 地铁变装_2096857300303699969.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `BasicGuider` —— 4/7 个有
- `CLIPTextEncode` —— 4/7 个有
- `QwenH3PromptLocal` —— 4/7 个有
- `YC_ShowText` —— 4/7 个有
- `CFGGuider` —— 3/7 个有
- `ConcatTextOfUtils` —— 2/7 个有
- `H3DistanceAttentionPatcher` —— 2/7 个有
- `H3DynamicCFGScheduler` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `LayerColor: Brightness & Contrast` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `SplitSigmas` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有
- `Yuan_H3Upscale3D` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
