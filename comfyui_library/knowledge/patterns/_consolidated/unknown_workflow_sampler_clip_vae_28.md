---
name: unknown_workflow_sampler_clip_vae_28
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.892857
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-dev文生图_1993862047901433857.json, 图片生成/文生图/FLUX2-dev文生图工作流_1993549884353609730.json, 图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2003736045457973250.json, 图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2041331289025945602.json, 图片生成/文生图/FLUX2文生图_1994284131244851202.json, 图片生成/文生图/FLUX2文生图基础工作流_1993578946742730753.json, 图片生成/文生图/FLUX2文生图基础工作流_1993609903375843329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/FLUX2-dev文生图_1993862047901433857.json、图片生成/文生图/FLUX2-dev文生图工作流_1993549884353609730.json、图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2003736045457973250.json、图片生成/文生图/FLUX2文生图-大图【LLM辅助】_2041331289025945602.json、图片生成/文生图/FLUX2文生图_1994284131244851202.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

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
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `Text Multiline` —— 3/7 个有
- `Int` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
