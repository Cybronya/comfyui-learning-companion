---
name: unknown_workflow_video_lora_clip_7
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8505
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ImpactSwitch, JjkText, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy clearCacheAll, easy float, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1956004146719719426.json, 视频生成/图生视频/1953334432444895233.json, 视频生成/文生视频/1955876808312979457.json, 视频生成/文生视频/1953684315559395330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1956004146719719426.json、视频生成/图生视频/1953334432444895233.json、视频生成/文生视频/1955876808312979457.json、视频生成/文生视频/1953684315559395330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImpactSwitch`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy float`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 3/4 个有
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `WanMoeKSampler` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `TorchCompileModelWanVideoV2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 11.5 | 8 - 15 | 4 | 70% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | uni_pc | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 11.5，观测区间 8 - 15，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 uni_pc，4 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
