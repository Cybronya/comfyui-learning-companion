---
name: unknown_workflow_sampler_clip_unet_226
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.886333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2+gemma4自动写提示词文生图工作流_2053683049765851138.json, 图片生成/文生图/flux2-klein基础文生图工作流_2033541606950834177.json, 图片生成/文生图/【遇见AI】FLUX2-klein-4b，文生图_2012008988237373441.json, 图片生成/文生图/【遇见AI】FLUX2-klein-9b，文生图_2012015997716271105.json, 图片生成/文生图/【遇见AI】FLUX2-klein-base-4b，文生图_2012011674202546178.json, 图片生成/文生图/【遇见AI】FLUX2-klein-base-9b，文生图_2012019877464248321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_226

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/flux2+gemma4自动写提示词文生图工作流_2053683049765851138.json、图片生成/文生图/flux2-klein基础文生图工作流_2033541606950834177.json、图片生成/文生图/【遇见AI】FLUX2-klein-4b，文生图_2012008988237373441.json、图片生成/文生图/【遇见AI】FLUX2-klein-9b，文生图_2012015997716271105.json、图片生成/文生图/【遇见AI】FLUX2-klein-base-4b，文生图_2012011674202546178.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `Int` —— 1/6 个有
- `ShowAnything|Mie` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1008 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
