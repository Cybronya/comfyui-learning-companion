---
name: unknown_workflow_video_sampler_unet_13
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.846846
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax H3角色替换_2114369929238634497.json, 平台全量/MiniMax H3角色替换（单人_指定角色）_2113661965217386498.json, 平台全量/Minimax H3 + 加速 Pika H3 Flex LoRA_2118130662212460546.json, 平台全量/Minimax-H3真实人物质感表现_2119001590475616258.json, 平台全量/minimax-H3-视频角色替换_2095487446925529089.json, 平台全量/多种lora加速对比-H3官方流-单采极速_2119302591355121665.json, 平台全量/静物美食视频H3_2113806098586230786.json, 数字人/数字人/免费开源MiniMax H3人物替换（单人_指定角色+视频编辑）_2115601379749359618.json, 视频生成/图生视频/H3_武戏_2116328274744922114.json, 视频生成/图生视频/H3_武戏_2116373714152542210.json, 视频生成/图生视频/H3官流最强武戏_2114882954718699522.json, 视频生成/图生视频/H3官流（终极版）231_2108222613133811714.json, 视频生成/图生视频/H3高清快速出视频_2105232331433930754.json, 视频生成/图生视频/MiniMax H3 AI人物演技提升_2112162919822741505.json, 视频生成/图生视频/MiniMax H3 超燃角色PV制作_2094985739380543489.json, 视频生成/图生视频/MiniMax H3单人快速替换（支持长视频+视频编辑）_2114911112603983873.json, 视频生成/图生视频/MiniMax H3角色替换_2114925978391760898.json, 视频生成/图生视频/MiniMax H3角色替换（单人_指定角色+视频编辑）_2109856895799480322.json, 视频生成/图生视频/MiniMax H3角色替换（单人_指定角色+视频编辑）_2113183349119475714.json, 视频生成/图生视频/MiniMax H3角色替换（单人_指定角色）_2114606760924368898.json, 视频生成/图生视频/MiniMax_H3_AI人物演技提升_2114903637058211842.json, 视频生成/图生视频/MiniMax_H3_AI人物演技提升_2115223579024519169.json, 视频生成/图生视频/MiniMax_H3角色替换单人_指定角色+视频编辑_2113769825045663745.json, 视频生成/图生视频/MiniMax_H3角色替换单人_指定角色+视频编辑_2113783898885939201.json, 视频生成/图生视频/api横屏640p坤坤H3官流无lora12步_2114189872008351746.json, 视频生成/图生视频/minimaxH3多参考视频工作流pv（备用方案）_2097327651475247106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（平台全量/MiniMax H3角色替换_2114369929238634497.json、平台全量/MiniMax H3角色替换（单人_指定角色）_2113661965217386498.json、平台全量/Minimax H3 + 加速 Pika H3 Flex LoRA_2118130662212460546.json、平台全量/Minimax-H3真实人物质感表现_2119001590475616258.json、平台全量/minimax-H3-视频角色替换_2095487446925529089.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 25/26 个有
- `LoadImage` —— 25/26 个有
- `LoraLoaderModelOnly` —— 25/26 个有
- `MiniMaxH3ReferenceToVideo` —— 25/26 个有
- `ModelAttentionBackend` —— 25/26 个有
- `ModelPreviewOverrideKJ` —— 25/26 个有
- `PrimitiveFloat` —— 25/26 个有
- `PrimitiveStringMultiline` —— 25/26 个有
- `BlockSparseAttention` —— 23/26 个有
- `ManualSigmas` —— 23/26 个有
- `VAEDecodeAudio` —— 23/26 个有
- `VHS_LoadVideo` —— 20/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/26 个有
- `MiniMaxH3SigmaShift` —— 17/26 个有
- `Label (rgthree)` —— 14/26 个有
- `ConditioningZeroOut` —— 13/26 个有
- `Fast Groups Bypasser (rgthree)` —— 13/26 个有
- `BasicScheduler` —— 12/26 个有
- `MiniMaxH3Unified` —— 12/26 个有
- `LoadAudio` —— 8/26 个有
- `PreviewImage` —— 5/26 个有
- `EmptyImage` —— 3/26 个有
- `ImageResizeKJv2` —— 1/26 个有
- `MiniMaxH3AddGuide` —— 1/26 个有
- `MiniMaxH3ImageToVideo` —— 1/26 个有
- `SelfLiftH3Sampler` —— 1/26 个有
- `VHS_SelectImages` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
