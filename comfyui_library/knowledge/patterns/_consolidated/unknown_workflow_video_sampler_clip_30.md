---
name: unknown_workflow_video_sampler_clip_30
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.822267
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanImageToVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json, 视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json, 视频生成/文生视频/“唐朝最美公主看牡丹”文生视频_2046107018011877377.json, 视频生成/文生视频/文生视频 高动态  Remix Wan2.2_1988515169389207553.json, 视频生成/文生视频/文生视频 高动态  Smooth Mix Wan2.2_1979531854162333698.json, 视频生成/文生视频/文生视频 高动态 高遵循_1987454682459213825.json, 视频生成/文生视频/文生视频 高动态 高遵循_2047578194169044994.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2041402091670872066.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2043496476206174210.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json, 视频生成/文生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052183737944821762.json, 视频生成/文生视频/文生视频+高动态_2046506744934830082.json, 视频生成/文生视频/文生视频+高动态_2046755281899622401.json, 视频生成/文生视频/高动态文生视频_2044729094360797185.json, 视频生成/文生视频/高动态文生视频_2045376789752586241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json、视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json、视频生成/文生视频/“唐朝最美公主看牡丹”文生视频_2046107018011877377.json、视频生成/文生视频/文生视频 高动态  Remix Wan2.2_1988515169389207553.json、视频生成/文生视频/文生视频 高动态  Smooth Mix Wan2.2_1979531854162333698.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanImageToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 14/15 个有
- `GetNode` —— 14/15 个有
- `RIFE VFI` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `wanBlockSwap` —— 14/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `ImpactSwitch` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 15 | 100% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler_ancestral | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，15 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
