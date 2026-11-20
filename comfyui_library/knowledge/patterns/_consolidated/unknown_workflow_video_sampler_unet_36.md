---
name: unknown_workflow_video_sampler_unet_36
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.87675
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json, 视频生成/图生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086780909889613825.json, 视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json, 视频生成/图生视频/自动化高质量多参视频流_2087788893096734722.json, 视频生成/文生视频/Minimax H3原版BF16微表情10秒768P模板_2090352182716624897.json, 视频生成/文生视频/Minimax H3原版BF16微表情15秒768P模板_2090352189364596737.json, 视频生成/文生视频/Minimax H3原版BF16微表情5秒768P模板_2090351939925135361.json, 视频生成/文生视频/Minimax H3原版BF16高动态10秒768P模板_2090351907796774913.json, 视频生成/文生视频/Minimax H3原版BF16高动态15秒768P模板_2090354634069204994.json, 视频生成/文生视频/Minimax H3原版BF16高动态5秒768P模板_2090351927031848962.json, 视频生成/文生视频/Minimax+H3+多参考int8高质量原版sage加速-max模式_2092079805448675329.json, 视频生成/文生视频/Minimax+H3+首尾帧int8高质量原版sage加速-max模式_2092079816949452801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_36

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json、视频生成/图生视频/开源版Minimax H3视频全功能加速图片参考turbo4步加速短视频生成_2086780909889613825.json、视频生成/图生视频/智能体专用版MinimaxH3开源版-全能多参支持视频参考-加速版_2095034413850644482.json、视频生成/图生视频/自动化高质量多参视频流_2087788893096734722.json、视频生成/文生视频/Minimax H3原版BF16微表情10秒768P模板_2090352182716624897.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/12 个有
- `CR Prompt Text` —— 9/12 个有
- `KSamplerSelect` —— 9/12 个有
- `LayerUtility: PurgeVRAM V2` —— 9/12 个有
- `LoraLoaderBypassModelOnly` —— 3/12 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `LoadAudio` —— 2/12 个有
- `VHS_LoadVideo` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `MemoryCleaner` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `WujiCleaner` —— 1/12 个有
- `XB_ROCmMemCleaner` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
