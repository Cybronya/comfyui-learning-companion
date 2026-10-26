---
name: unknown_workflow_video_upscale_latent_upscale_50
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.7425
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097216829407186945.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097872678001664001.json, 视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json, 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2100028236955738114.json, 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json, 视频生成/文生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频 口播带货视频_2098680337055444993.json, 视频生成/文生视频/MiniMaxH3数字人视频带货！H3多图生视频！_2098729617451479042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json、视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097216829407186945.json、视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097872678001664001.json、视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json、视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2100028236955738114.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `ManualSigmas` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `CR Text` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `Compare` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fans Text Concatenate` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `Int` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Seed Everywhere` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
