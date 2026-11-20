---
name: unknown_workflow_lora_sampler_clip_164
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90275
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux-4步极速文生图_1954712659226705921.json, 图片生成/文生图/nunchaku 文生图+lora 加速工作流_1920069563512459265.json, 图片生成/文生图/nunchaku-FLUX-FP4秒级中文提示词自动扩写文生图工作流_1918127402818404354.json, 图片生成/文生图/生成拟人化可爱小动物图=艾橘溪_1904465680211611649.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux-4步极速文生图_1954712659226705921.json、图片生成/文生图/nunchaku 文生图+lora 加速工作流_1920069563512459265.json、图片生成/文生图/nunchaku-FLUX-FP4秒级中文提示词自动扩写文生图工作流_1918127402818404354.json、图片生成/文生图/生成拟人化可爱小动物图=艾橘溪_1904465680211611649.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ChinesePrompt_Mix` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
