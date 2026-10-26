---
name: unknown_workflow_sampler_clip_unet_330
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.915
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2文生图1.0_1998240533703196674.json, 图片生成/文生图/【Flux2】一键生成影视级CG工作流（电影光柔焦质感）_2041504457069957122.json, 图片生成/文生图/【GUGU】FLUX2.0文生图_1993486400035160066.json, 图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_330

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux2文生图1.0_1998240533703196674.json、图片生成/文生图/【Flux2】一键生成影视级CG工作流（电影光柔焦质感）_2041504457069957122.json、图片生成/文生图/【GUGU】FLUX2.0文生图_1993486400035160066.json、图片生成/文生图/🍕最强开源 FLUX2系列之文生图【题词自动优化】_1993551504671965186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `CR Text` —— 2/4 个有
- `CR Seed` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Int Literal` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
