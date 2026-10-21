---
name: unknown_workflow_sampler_unet_vae_12
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8249
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json, 数字人/数字人/图生视频教学工作流_2091871574247952386.json, 数字人/数字人/首尾帧逻辑_2087967441874931713.json, 视频生成/图生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V3_2086166525018464258.json, 视频生成/图生视频/(10Eros-Max)MinimaxH3开源版 图生视频BF16高质量加速版_2085691291077271554.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2085552878504206337.json, 视频生成/图生视频/(10Eros-Max)Minimax图生视频BF16高质量加速版V2_2086152176455475202.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085215256233725953.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085648828052631554.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085258096615710722.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085265592797450241.json, 视频生成/图生视频/2图参考生视频minimax_2110625760905089026.json, 视频生成/图生视频/3图参考空白工作流miniimaxh3_2099113484138143745.json, 视频生成/图生视频/H3+LightX2V+二采高清参考生视频_2087551828098633730.json, 视频生成/图生视频/加速高质开源MiniMax+H3+FL2VA开源版-首尾帧参考生视频+++_2084152775365189633.json, 视频生成/文生视频/MINIMAX-H3 多参+二采2K直出-官方API_2086843177985732610.json, 视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_12

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/【遇见AI】Minimax H3二采提速，高分辨率生成，细节修复，修脸去伪影_2088472535468953602.json、数字人/数字人/图生视频教学工作流_2091871574247952386.json、数字人/数字人/首尾帧逻辑_2087967441874931713.json、视频生成/图生视频/(10Eros-Max V3)Minimax图生视频BF16高质量加速版V3_2086166525018464258.json、视频生成/图生视频/(10Eros-Max)MinimaxH3开源版 图生视频BF16高质量加速版_2085691291077271554.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 19/20 个有
- `SaveVideo` —— 19/20 个有
- `VAEDecode` —— 19/20 个有
- `VAEDecodeAudio` —— 19/20 个有
- `PrimitiveStringMultiline` —— 16/20 个有
- `LoraLoaderModelOnly` —— 14/20 个有
- `PathchSageAttentionKJ` —— 13/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/20 个有
- `MiniMaxH3ReferenceToVideo` —— 12/20 个有
- `MiniMaxH3ImageToVideo` —— 9/20 个有
- `CR Prompt Text` —— 7/20 个有
- `ImageResizeKJv2` —— 5/20 个有
- `MiniMaxH3BlockCacheT8` —— 5/20 个有
- `PT_H3ConcatAVLatent` —— 5/20 个有
- `VAEEncode` —— 5/20 个有
- `LoadAudio` —— 4/20 个有
- `VAEEncodeAudio` —— 4/20 个有
- `VHS_LoadVideo` —— 4/20 个有
- `VHS_VideoCombine` —— 4/20 个有
- `Fast Groups Bypasser (rgthree)` —— 3/20 个有
- `MiniMaxChunkFeedForward` —— 3/20 个有
- `GetNode` —— 2/20 个有
- `ModelAttentionBackend` —— 2/20 个有
- `SetNode` —— 2/20 个有
- `Any Switch (rgthree)` —— 1/20 个有
- `Int` —— 1/20 个有
- `MiniMaxH3AVDecodeT8` —— 1/20 个有
- `MiniMaxH3SigmaShift` —— 1/20 个有
- `MiniMaxLowVRAMAttention` —— 1/20 个有
- `PreviewAny` —— 1/20 个有
- `RHLLMChatNode` —— 1/20 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/20 个有
- `easy cleanGpuUsed` —— 1/20 个有
- `孤海注释` —— 1/20 个有
- `忽略多组孤海` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
