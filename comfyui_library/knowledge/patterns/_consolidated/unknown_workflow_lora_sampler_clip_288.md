---
name: unknown_workflow_lora_sampler_clip_288
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7565
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json, 图片生成/文生图/Anima8步极速工作流_2055609870266707970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_288

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/01 Qwen image 批量文生图 亚马逊平台外国儿童模特_2009990778717741058.json、图片生成/文生图/Anima8步极速工作流_2055609870266707970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ResolutionMaster` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
