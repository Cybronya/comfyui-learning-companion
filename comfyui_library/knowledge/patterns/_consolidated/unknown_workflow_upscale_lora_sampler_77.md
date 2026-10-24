---
name: unknown_workflow_upscale_lora_sampler_77
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.917333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxSampler, ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/沙雕动漫提示词都市动漫图片FLUX_1934960733677658114.json, 图片生成/文生图/沙雕动画场景{中文提示词输入开跑版}_1934978430360592385.json, 图片生成/文生图/沙雕动画场景专用工作流_2075008312994787329.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/沙雕动漫提示词都市动漫图片FLUX_1934960733677658114.json、图片生成/文生图/沙雕动画场景{中文提示词输入开跑版}_1934978430360592385.json、图片生成/文生图/沙雕动画场景专用工作流_2075008312994787329.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSampler`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `DeepTranslatorTextNode` —— 2/3 个有
- `ttN concat` —— 2/3 个有
- `Bjornulf_ShowStringText` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `CR Upscale Image` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SDVN Translate` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1344 | 1024 - 1344 | 3 | 88% |
| 高度 | 768 | 768 - 768 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1344，观测区间 1024 - 1344，3 个样本，取值集中（一致性 88%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
