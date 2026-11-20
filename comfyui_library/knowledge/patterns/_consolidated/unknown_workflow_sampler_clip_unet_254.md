---
name: unknown_workflow_sampler_clip_unet_254
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.858333
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowStringText, CLIPTextEncode, DualCLIPLoader, ImageResize+, JjkText, KSamplerSelect, LoadImage, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextCombinerTwo, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux图生图_1819700411573145602.json, 图片生成/图生图/Flux图生图_2045033605507850241.json, 图片生成/图生图/Flux图生图，精美，值得推荐！_2034854654676307970.json, 图片生成/图生图/Flux图生图，精美，值得推荐！_2047520744250286082.json, 图片生成/图生图/设计手稿转真人（真实还原）_2028393801617776641.json, 平台全量/服装设计4-手稿转真人_1909915350702718978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_254

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux图生图_1819700411573145602.json、图片生成/图生图/Flux图生图_2045033605507850241.json、图片生成/图生图/Flux图生图，精美，值得推荐！_2034854654676307970.json、图片生成/图生图/Flux图生图，精美，值得推荐！_2047520744250286082.json、图片生成/图生图/设计手稿转真人（真实还原）_2028393801617776641.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowStringText`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageResize+`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `RH_Prompter`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 4/6 个有
- `SeedGenerator` —— 4/6 个有
- `ImageResizeKJ` —— 2/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 0.5 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
