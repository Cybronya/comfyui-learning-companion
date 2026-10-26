---
name: unknown_workflow_video_lora_sampler_1024
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9055
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyHunyuanLatentVideo, ImpactInt, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, Note Plus (mtb), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/wan2.2 fun奖励LORA【更好动态 更多细节】_1967387631761940481.json, 视频生成/文生视频/🐳wan2.2 文生视频 加速出图版【官方模型】🦋_1949998908119367682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1024

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/wan2.2 fun奖励LORA【更好动态 更多细节】_1967387631761940481.json、视频生成/文生视频/🐳wan2.2 文生视频 加速出图版【官方模型】🦋_1949998908119367682.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `Note Plus (mtb)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `WanVideoNAG` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 50% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 80% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
