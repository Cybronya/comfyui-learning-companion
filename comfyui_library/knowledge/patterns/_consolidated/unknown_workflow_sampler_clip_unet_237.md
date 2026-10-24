---
name: unknown_workflow_sampler_clip_unet_237
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.851
common_nodes: [BasicGuider, BasicScheduler, Bjornulf_ShowStringText, CLIPTextEncode, DualCLIPLoader, ImageResize+, JjkText, KSamplerSelect, LoadImage, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextCombinerTwo, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux图生图_1819700411573145602.json, 图片生成/图生图/Flux图生图_2045033605507850241.json, 图片生成/图生图/Flux图生图，精美，值得推荐！_2034854654676307970.json, 图片生成/图生图/Flux图生图，精美，值得推荐！_2047520744250286082.json, 图片生成/图生图/设计手稿转真人（真实还原）_2028393801617776641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_237

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux图生图_1819700411573145602.json、图片生成/图生图/Flux图生图_2045033605507850241.json、图片生成/图生图/Flux图生图，精美，值得推荐！_2034854654676307970.json、图片生成/图生图/Flux图生图，精美，值得推荐！_2047520744250286082.json、图片生成/图生图/设计手稿转真人（真实还原）_2028393801617776641.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImpactSwitch` —— 4/5 个有
- `SeedGenerator` —— 4/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
