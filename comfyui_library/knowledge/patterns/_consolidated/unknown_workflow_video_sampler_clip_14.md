---
name: unknown_workflow_video_sampler_clip_14
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.8093
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanImageToVideo, easy showAnything]
problems: []
missing: [CR Text, MathExpression|pysssss, RIFE VFI, Text Concatenate, easy cleanGpuUsed, CR Text Input Switch (4 way)]
members: [视频生成/图生视频/2054361569718489089.json, 视频生成/图生视频/2052573232586346497.json, 视频生成/图生视频/2053725147890241538.json, 视频生成/文生视频/1950112023776550913.json, 视频生成/文生视频/1979519177214038018.json, 视频生成/文生视频/1979531854162333698.json, 视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json, 视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json, 视频生成/文生视频/“唐朝最美公主看牡丹”文生视频_2046107018011877377.json, 视频生成/文生视频/文生视频 高动态  Remix Wan2.2_1988515169389207553.json, 视频生成/文生视频/文生视频 高动态 高遵循_1987454682459213825.json, 视频生成/文生视频/文生视频 高动态 高遵循_2047578194169044994.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2041402091670872066.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2043496476206174210.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json, 视频生成/文生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052183737944821762.json, 视频生成/文生视频/文生视频+高动态_2046506744934830082.json, 视频生成/文生视频/文生视频+高动态_2046755281899622401.json, 视频生成/文生视频/高动态文生视频_2044729094360797185.json, 视频生成/文生视频/高动态文生视频_2045376789752586241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2054361569718489089.json、视频生成/图生视频/2052573232586346497.json、视频生成/图生视频/2053725147890241538.json、视频生成/文生视频/1950112023776550913.json、视频生成/文生视频/1979519177214038018.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 20 个 workflow 都包含：
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
- `RIFE VFI` —— 19/20 个有
- `wanBlockSwap` —— 19/20 个有
- `GetNode` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `CR Text Input Switch (4 way)` —— 17/20 个有
- `ImpactSwitch` —— 3/20 个有
- `Fast Groups Bypasser (rgthree)` —— 2/20 个有
- `easy cleanGpuUsed` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 20 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 20 | 100% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler_ancestral | - | 20 | 100% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，20 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，20 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，20 个样本，一致性 100%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、MathExpression|pysssss、RIFE VFI、Text Concatenate、easy cleanGpuUsed
