---
name: unknown_workflow_lora_sampler_clip_75
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.915
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/nunchaku-Flux超快加速文生图_1909949768628666370.json, 图片生成/文生图/nunchaku-flux.1-dev flux秒出图_1910558383181656066.json, 图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json, 图片生成/文生图/nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json, 图片生成/文生图/nunchaku-flux.1-dev-8步快速出图_1942467291403464705.json, 图片生成/文生图/nunchaku-flux.1-dev_1929809956793434113.json, 图片生成/文生图/推文工作流_1923351389630885890.json, 平台全量/IC一致性小说推文_1934543460043300866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/nunchaku-Flux超快加速文生图_1909949768628666370.json、图片生成/文生图/nunchaku-flux.1-dev flux秒出图_1910558383181656066.json、图片生成/文生图/nunchaku-flux.1-dev 个人加速工作流V1_2028335440100597762.json、图片生成/文生图/nunchaku-flux.1-dev 官方加速工作流_1909669429062631425.json、图片生成/文生图/nunchaku-flux.1-dev-8步快速出图_1942467291403464705.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/8 个有
- `FluxGuidance` —— 7/8 个有
- `ModelSamplingFlux` —— 7/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `Upscale Model Loader` —— 2/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Note _O` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
