---
name: unknown_workflow_video_lora_sampler_743
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.881
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3视频-四川话-版本（支持多参加速）_2088296997613817858.json, 视频生成/图生视频/邻家唯美｜H3八步·积分版自然互动_2102207203225718786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_743

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3视频-四川话-版本（支持多参加速）_2088296997613817858.json、视频生成/图生视频/邻家唯美｜H3八步·积分版自然互动_2102207203225718786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `Float` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MiniMaxH3EasyMediaBridge` —— 1/2 个有
- `Note _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
