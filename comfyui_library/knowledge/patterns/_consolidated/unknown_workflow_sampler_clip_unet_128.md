---
name: unknown_workflow_sampler_clip_unet_128
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9102
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2 Klein 文生图工作流_2091474310002200578.json, 图片生成/文生图/FLUX2-KLEIN 4B快速文生图_2012166692574601217.json, 图片生成/文生图/FLUX2-KLEIN+lora+快速生图_2012490189339365377.json, 图片生成/文生图/FLUX2-KLEIN-文生图_2086265051199135746.json, 图片生成/文生图/扎染-小帽子lora测l试_2062536155131895810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX2 Klein 文生图工作流_2091474310002200578.json、图片生成/文生图/FLUX2-KLEIN 4B快速文生图_2012166692574601217.json、图片生成/文生图/FLUX2-KLEIN+lora+快速生图_2012490189339365377.json、图片生成/文生图/FLUX2-KLEIN-文生图_2086265051199135746.json、图片生成/文生图/扎染-小帽子lora测l试_2062536155131895810.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
