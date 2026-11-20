---
name: unknown_workflow_sampler_clip_unet_141
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9698
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux Klein 9b FP8 文生图 极简工作流_2015298868837093378.json, 图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json, 图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json, 图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json, 图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json, 图片生成/文生图/Flux.2+Klein+9B无限制文生图_2028848965118070785.json, 图片生成/文生图/Flux.2_Klein_9B文生图_2069068665672265729.json, 图片生成/文生图/Flux2文生图_1995379549791825922.json, 图片生成/文生图/Flux2文生图呀_2068421815818612737.json, 图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_141

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Flux Klein 9b FP8 文生图 极简工作流_2015298868837093378.json、图片生成/文生图/Flux.2 Klein 9B_fp16文生图_2066061172897574913.json、图片生成/文生图/Flux.2 Klein 9B二次元CG动漫_2025780362521088001.json、图片生成/文生图/Flux.2 Klein 9B无限制文生图_2022518673075871745.json、图片生成/文生图/Flux.2 Klein 9B满血版文生图_2066862519515435010.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
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
- `FluxGuidance` —— 9/10 个有
- `CompressImages` —— 6/10 个有
- `Int Literal` —— 6/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `ModelPatchTorchSettings` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `CFGGuider` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `DuckQREncodeNode` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `ReferenceLatent` —— 1/10 个有
- `WidthHeightPicker` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
