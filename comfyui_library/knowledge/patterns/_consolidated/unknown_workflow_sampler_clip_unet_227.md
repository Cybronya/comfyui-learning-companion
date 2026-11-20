---
name: unknown_workflow_sampler_clip_unet_227
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.880286
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2003736045457973250.json, 图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2041331289025945602.json, 图片生成/文生图/FLUX2文生图_1994284131244851202.json, 图片生成/文生图/FLUX2文生图基础工作流_1993578946742730753.json, 图片生成/文生图/FLUX2文生图基础工作流_1993609903375843329.json, 图片生成/文生图/Flux2文生图工作流--直出2K_1926661482686353410.json, 图片生成/文生图/flux2文生图1.0_1998240533703196674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_227

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2003736045457973250.json、图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2041331289025945602.json、图片生成/文生图/FLUX2文生图_1994284131244851202.json、图片生成/文生图/FLUX2文生图基础工作流_1993578946742730753.json、图片生成/文生图/FLUX2文生图基础工作流_1993609903375843329.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Text Multiline` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `Int` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR Seed` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ReferenceLatent` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
