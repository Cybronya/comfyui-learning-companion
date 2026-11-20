---
name: unknown_workflow_sampler_clip_unet_373
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86575
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2+gemma4自动写提示词文生图工作流_2053683049765851138.json, 图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json, 图片生成/文生图/flux2-klein基础文生图工作流_2033541606950834177.json, 平台全量/FLUX2 高质感写实图生成_2059204061316075522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_373

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux2+gemma4自动写提示词文生图工作流_2053683049765851138.json、图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json、图片生成/文生图/flux2-klein基础文生图工作流_2033541606950834177.json、平台全量/FLUX2 高质感写实图生成_2059204061316075522.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Int` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1008 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
