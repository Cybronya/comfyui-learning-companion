---
name: unknown_workflow_sampler_clip_checkpoint_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【遇见AI】sd3_medium_clip_T5文生图_2039206218757054465.json, 图片生成/文生图/咕咕嘎嘎_2041014883361234945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【遇见AI】sd3_medium_clip_T5文生图_2039206218757054465.json、图片生成/文生图/咕咕嘎嘎_2041014883361234945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeSD3` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 97% |
| Prompt 约束强度(CFG) | 5.75 | - | 2 | 78% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 5.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
