---
name: unknown_workflow_lora_sampler_clip_154
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82525
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, Lora Loader Stack (rgthree), PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/真人转全能图片G-4o卡通3D玩偶_1913613624995446786.json, 图片生成/文生图/Chibify_1925114613338152962.json, 图片生成/文生图/Flux最强换脸_1894257044323500034.json, 图片生成/文生图/吉卜力风格换脸写真文生图工作流_1906942276495450113.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/真人转全能图片G-4o卡通3D玩偶_1913613624995446786.json、图片生成/文生图/Chibify_1925114613338152962.json、图片生成/文生图/Flux最强换脸_1894257044323500034.json、图片生成/文生图/吉卜力风格换脸写真文生图工作流_1906942276495450113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `Note Plus (mtb)` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
