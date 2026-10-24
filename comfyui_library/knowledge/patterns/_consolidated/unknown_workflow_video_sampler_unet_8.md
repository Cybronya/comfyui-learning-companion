---
name: unknown_workflow_video_sampler_unet_8
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.887345
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 文生视频_2087105033031737345.json, 视频生成/文生视频/Minimax H3原版BF16微表情10秒768P模板_2090352182716624897.json, 视频生成/文生视频/Minimax H3原版BF16微表情15秒768P模板_2090352189364596737.json, 视频生成/文生视频/Minimax H3原版BF16微表情5秒768P模板_2090351939925135361.json, 视频生成/文生视频/Minimax H3原版BF16高动态10秒768P模板_2090351907796774913.json, 视频生成/文生视频/Minimax H3原版BF16高动态15秒768P模板_2090354634069204994.json, 视频生成/文生视频/Minimax H3原版BF16高动态5秒768P模板_2090351927031848962.json, 视频生成/文生视频/Minimax+H3+多参考int8-4步加速lora-6步-match模式_2092079778638680066.json, 视频生成/文生视频/Minimax+H3+多参考int8-8步加速lora-10步-match模式_2092079794623172610.json, 视频生成/文生视频/Minimax+H3+多参考int8高质量原版sage加速-max模式_2092079805448675329.json, 视频生成/文生视频/Minimax+H3+首尾帧int8高质量原版sage加速-max模式_2092079816949452801.json, 视频生成/文生视频/Minimax+H3-Dasiwa-动漫-4步加速lora-6步_2093976759384498178.json, 视频生成/文生视频/Minimax+H3-Dasiwa-动漫多参考-8步加速lora-10步_2093976770788810754.json, 视频生成/文生视频/Minimax+H3混合模型b+20-49多参考更强、画质提升_2091486566232444930.json, 视频生成/文生视频/Minimax+H3混合模型b+25-49+4步加速lora-多参考更好的画质_2091486581453578241.json, 视频生成/文生视频/Minimax+H3混合模型b+25-49+8步加速lora-多参考更好的画质_2091486592572682241.json, 视频生成/文生视频/Minimax+H3混合模型b+25-49多参考更好的画质_2091486602953580545.json, 视频生成/文生视频/Minimax+H3首尾帧int8-4步加速lora-6步-match模式_2092079829788221441.json, 视频生成/文生视频/Minimax+H3首尾帧int8-8步加速lora-10步-match模式_2092081714205122562.json, 视频生成/文生视频/Minimax-H3-4步加速（T8节点+提示词强化）_2086825206148063234.json, 视频生成/文生视频/Minimax-H3极速4分钟出15秒480P-文生视频(双时钟-8步lora)_2086317767086665729.json, 视频生成/文生视频/Minimax-H3极速视频编辑(双时钟-8步lora)_2086326048232398850.json, 视频生成/文生视频/minimax三图工作流_2090738092591378434.json, 视频生成/文生视频/minimax三图工作流_2091847130888630274.json, 视频生成/文生视频/minimax九图工作流_2091582636920758274.json, 视频生成/文生视频/minimax九图工作流_2092593622448427010.json, 视频生成/文生视频/minimax九图工作流_2102148767163183105.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V2（加速版）_2085937471304585218.json, 视频生成/文生视频/万象AI--MiniMax H3 多参生视频-V3（加速提示词优化版）_2086606105207205889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 文生视频_2087105033031737345.json、视频生成/文生视频/Minimax H3原版BF16微表情10秒768P模板_2090352182716624897.json、视频生成/文生视频/Minimax H3原版BF16微表情15秒768P模板_2090352189364596737.json、视频生成/文生视频/Minimax H3原版BF16微表情5秒768P模板_2090351939925135361.json、视频生成/文生视频/Minimax H3原版BF16高动态10秒768P模板_2090351907796774913.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 27/29 个有
- `MiniMaxH3AudioConditioningT8` —— 27/29 个有
- `CR Prompt Text` —— 26/29 个有
- `BasicScheduler` —— 18/29 个有
- `KSamplerSelect` —— 18/29 个有
- `LayerUtility: PurgeVRAM V2` —— 18/29 个有
- `LoraLoaderBypassModelOnly` —— 11/29 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/29 个有
- `LoraLoaderModelOnly` —— 8/29 个有
- `PrimitiveStringMultiline` —— 3/29 个有
- `VHS_LoadVideo` —— 3/29 个有
- `MiniMaxH3ImageToVideo` —— 2/29 个有
- `MiniMaxH3ReferenceToVideo` —— 2/29 个有
- `RHLLMChatNode` —— 2/29 个有
- `ImageScaleToTotalPixels` —— 1/29 个有
- `ShowText|fofo` —— 1/29 个有
- `ShowText|pysssss` —— 1/29 个有
- `Text Multiline` —— 1/29 个有
- `easy showAnything` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
