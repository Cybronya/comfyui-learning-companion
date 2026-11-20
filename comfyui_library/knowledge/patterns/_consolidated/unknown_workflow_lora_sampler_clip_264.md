---
name: unknown_workflow_lora_sampler_clip_264
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.839
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Prompter, RandomNoise, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Flux + Pulid 固定角色多角度一致性生成_1847270524106817537.json, 平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json, 平台全量/旅行打卡机_1848631345928081409.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux + Pulid 固定角色多角度一致性生成_1847270524106817537.json、平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json、平台全量/旅行打卡机_1848631345928081409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Prompter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DisplayText` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TextBox` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `ConcatStringSingle` —— 1/3 个有
- `Crop Face` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Batch` —— 1/3 个有
- `Load RetinaFace` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
