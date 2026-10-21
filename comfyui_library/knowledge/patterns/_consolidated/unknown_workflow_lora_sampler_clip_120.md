---
name: unknown_workflow_lora_sampler_clip_120
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.861333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2文生图呀_2068421815818612737.json, 图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json, 图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2文生图呀_2068421815818612737.json、图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json、图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/3 个有
- `DuckQREncodeNode` —— 1/3 个有
- `Int Literal` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
