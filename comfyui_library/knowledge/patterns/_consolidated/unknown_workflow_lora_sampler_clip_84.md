---
name: unknown_workflow_lora_sampler_clip_84
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.926
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImpactInt, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最美证件照-Kontext 自动矫正_2068967063636500481.json, 图片生成/图生图/证件排版+美颜-Kontext 自动矫正  证件照-多种背景_服饰选择 证件照生成_2067814898117210113.json, 图片生成/图生图/证件照一键生成，排版+美颜-Kontext（自动矫正）_2023654966904229890.json, 图片生成/图生图/证件照一键生成，排版+美颜-Kontext（自动矫正）_2063496200963321857.json, 图片生成/图生图/🥎Kontext图案提取测试🤹_1946740951667601410.json, 图片生成/图生图/🥎【大炮工具】Kontext 证件照一键排版【微美颜】🤹_1947908863526875138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/最美证件照-Kontext 自动矫正_2068967063636500481.json、图片生成/图生图/证件排版+美颜-Kontext 自动矫正  证件照-多种背景_服饰选择 证件照生成_2067814898117210113.json、图片生成/图生图/证件照一键生成，排版+美颜-Kontext（自动矫正）_2023654966904229890.json、图片生成/图生图/证件照一键生成，排版+美颜-Kontext（自动矫正）_2063496200963321857.json、图片生成/图生图/🥎Kontext图案提取测试🤹_1946740951667601410.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImpactInt`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Image Border` —— 5/6 个有
- `ImageConcanateOfUtils` —— 5/6 个有
- `ImageFromBatch` —— 5/6 个有
- `ImageListToImageBatch` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ReActorImageDublicator` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `String` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `CR Text` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
