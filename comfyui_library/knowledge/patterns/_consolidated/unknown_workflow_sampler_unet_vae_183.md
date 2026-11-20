---
name: unknown_workflow_sampler_unet_vae_183
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8305
common_nodes: [DualCLIPLoader, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json, 图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json, 图片生成/文生图/Flux canny线条控制工作流_1965638484138577921.json, 图片生成/文生图/flux tool Canny、Depth工作流_1896762902793920513.json, 图片生成/文生图/flux_depth_lora工作流_1990967018591563778.json, 图片生成/文生图/flux模型canny细致线控制工作流_1988873413324312577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_183

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】flex2-preview 控制pose，depth，canny_2053036057029033985.json、图片生成/文生图/FLUX.1-Canny-dev 完整版工作流_1990952011577372674.json、图片生成/文生图/Flux canny线条控制工作流_1965638484138577921.json、图片生成/文生图/flux tool Canny、Depth工作流_1896762902793920513.json、图片生成/文生图/flux_depth_lora工作流_1990967018591563778.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/6 个有
- `InstructPixToPixConditioning` —— 5/6 个有
- `FluxGuidance` —— 4/6 个有
- `Canny` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `CLIPTextEncodeFlux` —— 1/6 个有
- `Flex2Conditioner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 6 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | normal | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，6 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 normal，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
