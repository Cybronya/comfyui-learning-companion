---
name: unknown_workflow_video_lora_sampler_118
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.828125
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2113475763625349121.json, 平台全量/MiniMax H3 视频复刻：视频翻拍、二创与指定角色替换_2109500526458134530.json, 平台全量/MiniMax H3 视频复刻：视频翻拍、二创与指定角色替换_2109628460296658946.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2106734702446075906.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2114297778703785986.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）_2106724867256176641.json, 数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）_2114313913683759106.json, 数字人/数字人/MiniMax H3视频复刻数字人｜换人换产品不换文案保留原视频语音版_2114624800655237121.json, 数字人/数字人/MiniMax H3视频复刻数字人｜视频换人换产品换文案并替换原视频语音_2114622814899761153.json, 数字人/数字人/音频驱动-Dasiwa V1-MiniMax H3数字人-加速版_2095011177205166081.json, 视频生成/图生视频/(b25-49+ema600)MiniMax H3数字人加速版V1_2094796122115108866.json, 视频生成/图生视频/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2105605446362030081.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2088583576190279681.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频(9图3视频3音频)_2091128915946459138.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频_2086885673054855170.json, 视频生成/文生视频/MiniMax H3 4步加速 全能参考生视频_2091121872074272770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_118

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2113475763625349121.json、平台全量/MiniMax H3 视频复刻：视频翻拍、二创与指定角色替换_2109500526458134530.json、平台全量/MiniMax H3 视频复刻：视频翻拍、二创与指定角色替换_2109628460296658946.json、数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2106734702446075906.json、数字人/数字人/MiniMax H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）_2114297778703785986.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 12/16 个有
- `SolAttnMiniMax` —— 12/16 个有
- `VHS_LoadVideo` —— 10/16 个有
- `LoadVideo` —— 8/16 个有
- `孤海注释` —— 8/16 个有
- `LoadAudio` —— 6/16 个有
- `GetVideoComponents` —— 4/16 个有
- `AnyBooleanSwitch` —— 1/16 个有
- `CR Font File List` —— 1/16 个有
- `CompressImages` —— 1/16 个有
- `ImpactConditionalBranch` —— 1/16 个有
- `LoadFolderFromDir` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `VHS_SelectFilename` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
