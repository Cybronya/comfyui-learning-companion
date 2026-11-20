---
name: unknown_workflow_sampler_unet_vae_121
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8277
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2095826055666950145.json, 图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json, 平台全量/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2097248370111901698.json, 数字人/数字人/MINIMAX-H3 8参考_2086224463867236354.json, 数字人/数字人/MINIMAX-H3 9参考_2086239769545232385.json, 数字人/数字人/MINIMAX-H3 9参考_2086338746995265538.json, 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜10Eros+LightX2V__2088301741266788353.json, 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json, 视频生成/文生视频/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2087029485995642882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_121

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【0813】MiniMax H3文 图 参考生视频三合一｜组合加速｜全模式二采增强版 B站@好奇漫步_2095826055666950145.json、图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json、平台全量/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2097248370111901698.json、数字人/数字人/MINIMAX-H3 8参考_2086224463867236354.json、数字人/数字人/MINIMAX-H3 9参考_2086239769545232385.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `LoadAudio` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `LoadVideo` —— 8/10 个有
- `LoraLoaderBypassModelOnly` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `MiniMaxH3ImageToVideo` —— 7/10 个有
- `ComfySwitchNode` —— 6/10 个有
- `GetVideoComponents` —— 6/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `PT_H3ConcatAVLatent` —— 6/10 个有
- `PrimitiveInt` —— 6/10 个有
- `VAEEncode` —— 6/10 个有
- `VAEEncodeAudio` —— 6/10 个有
- `JWString` —— 3/10 个有
- `JoinStrings` —— 3/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `Get Date Time String (JPS)` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `SaveText|pysssss` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `StringFunction|pysssss` —— 2/10 个有
- `WidgetToString` —— 2/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
