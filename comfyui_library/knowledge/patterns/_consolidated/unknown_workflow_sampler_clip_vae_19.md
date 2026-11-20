---
name: unknown_workflow_sampler_clip_vae_19
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.921583
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/吉卜力风格化_1905893406915088385.json, 图片生成/图生图/图片一键转灵魂画手风格_2024788264820936705.json, 图片生成/图生图/提取物品_1947232272145666049.json, 图片生成/图生图/文字编辑图片 Flux kontext dev_1938542570844938242.json, 图片生成/图生图/电商服装去除图片人物_1943097905094025218.json, 图片生成/图生图/移除物品_1947235737038168065.json, 平台全量/万物迁移 便利贴版_1950400459452407810.json, 平台全量/图片转灵魂画手风格_1949809882229817346.json, 平台全量/电商一键生成国风背景产品图_1946939348957687810.json, 平台全量/电商产品图换背景 kontext_1956251539327340546.json, 平台全量/电商去除图片马赛克_1938881900268474369.json, 平台全量/真人转彩铅画_1955107741595570178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/吉卜力风格化_1905893406915088385.json、图片生成/图生图/图片一键转灵魂画手风格_2024788264820936705.json、图片生成/图生图/提取物品_1947232272145666049.json、图片生成/图生图/文字编辑图片 Flux kontext dev_1938542570844938242.json、图片生成/图生图/电商服装去除图片人物_1943097905094025218.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 11/12 个有
- `FluxKontextImageScale` —— 11/12 个有
- `ReferenceLatent` —— 11/12 个有
- `CheckpointLoaderSimple` —— 10/12 个有
- `RepeatLatentBatch` —— 9/12 个有
- `easy imageSize` —— 8/12 个有
- `LoraLoader` —— 7/12 个有
- `Text` —— 4/12 个有
- `RH_Translator` —— 3/12 个有
- `GetImageSize` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `PrimitiveString` —— 2/12 个有
- `StringReplace` —— 2/12 个有
- `UNETLoader` —— 2/12 个有
- `ImageResize+` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
