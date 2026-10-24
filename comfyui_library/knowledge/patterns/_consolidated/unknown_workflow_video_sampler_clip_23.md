---
name: unknown_workflow_video_sampler_clip_23
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.824
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json, 视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json, 视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json, 视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json, 视频生成/文生视频/“唐朝最美公主看牡丹”文生视频_2046107018011877377.json, 视频生成/文生视频/文生视频 高动态  Remix Wan2.2_1988515169389207553.json, 视频生成/文生视频/文生视频 高动态  Smooth Mix Wan2.2_1979531854162333698.json, 视频生成/文生视频/文生视频 高动态 高遵循_1987454682459213825.json, 视频生成/文生视频/文生视频 高动态 高遵循_2047578194169044994.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2041402091670872066.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2043496476206174210.json, 视频生成/文生视频/文生视频+高动态++Remix+Wan2.2_2044223069518045185.json, 视频生成/文生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052183737944821762.json, 视频生成/文生视频/文生视频+高动态_2046506744934830082.json, 视频生成/文生视频/文生视频+高动态_2046755281899622401.json, 视频生成/文生视频/高动态文生视频_2044729094360797185.json, 视频生成/文生视频/高动态文生视频_2045376789752586241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json、视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json、视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json、视频生成/文生视频/Wan2.2 文生视频 高动态  Remix_2042857101634052097.json、视频生成/文生视频/Wan2.2_Smooth Mix高动态文生视频【官版】_1950112023776550913.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 17/18 个有
- `Text Concatenate` —— 17/18 个有
- `Wan22PromptSelector` —— 17/18 个有
- `WanImageToVideo` —— 17/18 个有
- `wanBlockSwap` —— 17/18 个有
- `GetNode` —— 16/18 个有
- `SetNode` —— 16/18 个有
- `CR Text Input Switch (4 way)` —— 14/18 个有
- `ImpactSwitch` —— 4/18 个有
- `Fast Groups Bypasser (rgthree)` —— 3/18 个有
- `CLIPVisionEncode` —— 1/18 个有
- `CLIPVisionLoader` —— 1/18 个有
- `ImageConcanate` —— 1/18 个有
- `ImageResizeKJ` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `LoadImage` —— 1/18 个有
- `WanFirstLastFrameToVideo` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 18 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 18 | 100% |
| 采样算法 | 1 | 1 - 1 | 18 | 100% |
| 调度器 | euler_ancestral | - | 18 | 100% |
| 重绘幅度 | simple | - | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，18 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，18 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，18 个样本，一致性 100%
- 重绘幅度 最常用 simple，18 个样本，一致性 100%
