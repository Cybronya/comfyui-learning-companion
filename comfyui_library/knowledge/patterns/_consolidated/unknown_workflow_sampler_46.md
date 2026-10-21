---
name: unknown_workflow_sampler_46
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6385
common_nodes: [CR Text, CreateVideo, Int, JoyAI_Echo_SM_Clip, JoyAI_Echo_SM_Encoder, JoyAI_Echo_SM_KSampler, JoyAI_Echo_SM_Model, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/JoyAI Echo 单人vlog长视频_2064087168896815106.json, 视频生成/文生视频/JoyAI Echo 数字人长视频_2063963745671536641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_46

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/JoyAI Echo 单人vlog长视频_2064087168896815106.json、视频生成/文生视频/JoyAI Echo 数字人长视频_2063963745671536641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CreateVideo`
- `Int`
- `JoyAI_Echo_SM_Clip`
- `JoyAI_Echo_SM_Encoder`
- `JoyAI_Echo_SM_KSampler`
- `JoyAI_Echo_SM_Model`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3.21244e+08 | - | 2 | 55% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 121 | - | 2 | 100% |
| 调度器 | 24 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 3.21244e+08，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 4.65849e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
