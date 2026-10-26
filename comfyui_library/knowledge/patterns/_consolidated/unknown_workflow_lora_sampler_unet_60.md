---
name: unknown_workflow_lora_sampler_unet_60
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7978
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2095826055666950145.json, 图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json, 视频生成/图生视频/H3+LightX2V+二采高清参考生视频_2087551828098633730.json, 视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json, 视频生成/图生视频/Minimax H3 参考图和参考视音频生成视频满血版_2105625287546462210.json, 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜10Eros+LightX2V__2088301741266788353.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json, 视频生成/文生视频/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2087029485995642882.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2095826055666950145.json、图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json、视频生成/图生视频/H3+LightX2V+二采高清参考生视频_2087551828098633730.json、视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json、视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ComfySwitchNode` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `GetVideoComponents` —— 7/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `LoadVideo` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `PT_H3ConcatAVLatent` —— 7/10 个有
- `VAEEncode` —— 7/10 个有
- `VAEEncodeAudio` —— 7/10 个有
- `MiniMaxH3ImageToVideo` —— 6/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `Get Date Time String (JPS)` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `SaveText|pysssss` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `StringFunction|pysssss` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `WidgetToString` —— 2/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `VedaSparseAttention` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
