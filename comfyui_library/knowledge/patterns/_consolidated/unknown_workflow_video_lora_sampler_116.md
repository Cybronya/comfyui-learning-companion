---
name: unknown_workflow_video_lora_sampler_116
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.558187
common_nodes: [BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/多角色对话丨MiniMax H3 Hybrid丨三图参考·音画同生_2112093052927037442.json, 平台全量/H3全能参考pika fl2va+selflift（二采）_2117229234686087170.json, 平台全量/H3全能参考pika ref2va单采_2117437821567987714.json, 平台全量/H3全能参考pika 加速二采_2117434377117458433.json, 平台全量/H3全能参考pika_ref2va单采_2117786635826978818.json, 平台全量/H3全能参考pika_加速二采_2117782990985191426.json, 平台全量/JM-H3+终极篇-去油文武破线-支持首尾帧_2118910458345381889.json, 平台全量/MiniMax H3 多参生视频_2120086053490089985.json, 视频生成/图生视频/MiniMax_H3_终极篇-文武双全_2114886750979055618.json, 视频生成/图生视频/YZ金鱼-MiniMax H3 终极篇-文武双全_2113823810985226242.json, 视频生成/图生视频/YZ金鱼-MiniMax H3 终极篇-文武双全_2113860678867046402.json, 视频生成/图生视频/YZ金鱼-MiniMax H3 终极篇-文武双全_2117089269843062785.json, 视频生成/图生视频/minimax H3文武双修（小脸不蹦）_2108335764886085634.json, 视频生成/图生视频/qwen文武_2113903502299852801.json, 视频生成/图生视频/qwen文武_2113913807365033985.json, 视频生成/图生视频/文武双全首尾帧_2112932870200320002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_116

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/多角色对话丨MiniMax H3 Hybrid丨三图参考·音画同生_2112093052927037442.json、平台全量/H3全能参考pika fl2va+selflift（二采）_2117229234686087170.json、平台全量/H3全能参考pika ref2va单采_2117437821567987714.json、平台全量/H3全能参考pika 加速二采_2117434377117458433.json、平台全量/H3全能参考pika_ref2va单采_2117786635826978818.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 16 个 workflow 都包含：
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxChunkFeedForward` —— 14/16 个有
- `GetNode` —— 13/16 个有
- `SetNode` —— 13/16 个有
- `BasicScheduler` —— 12/16 个有
- `ConditioningZeroOut` —— 12/16 个有
- `GoohaiUniversalSlider` —— 11/16 个有
- `SelfLiftH3Sampler` —— 11/16 个有
- `Text` —— 11/16 个有
- `VHS_LoadVideo` —— 11/16 个有
- `忽略多组孤海` —— 11/16 个有
- `CR Prompt Text` —— 5/16 个有
- `Fast Groups Bypasser (rgthree)` —— 5/16 个有
- `BasicGuider` —— 4/16 个有
- `ManualSigmas` —— 4/16 个有
- `RandomNoise` —— 4/16 个有
- `SamplerCustomAdvanced` —— 4/16 个有
- `DisableNoise` —— 2/16 个有
- `MiniMaxH3AddGuide` —— 2/16 个有
- `MiniMaxH3LatentUpscaleCombined` —— 2/16 个有
- `QwenH3PromptLocal` —— 2/16 个有
- `easy showAnything` —— 2/16 个有
- `H3SigmaRefiner` —— 1/16 个有
- `SelfLiftAvatarH3Sampler` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
