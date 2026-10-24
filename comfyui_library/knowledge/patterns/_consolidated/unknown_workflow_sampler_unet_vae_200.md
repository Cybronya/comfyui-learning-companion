---
name: unknown_workflow_sampler_unet_vae_200
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9342
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSamplerSelect, LayerUtility: TextJoin, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ai滤镜应用版_1985270833641832449.json, 图片生成/图生图/全能图片G4o同款 3D卡通人物玩偶+名字_1921402683154972673.json, 图片生成/图生图/照片转全能图片G-4o卡通人像形象丨一键在线运行_1911405677586149377.json, 图片生成/图生图/照片转简洁q版卡通手办-全能图片G-4o同款_1920801534802591746.json, 图片生成/文生图/反推提示词+在线生图v1.0_1946032541281251330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_200

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ai滤镜应用版_1985270833641832449.json、图片生成/图生图/全能图片G4o同款 3D卡通人物玩偶+名字_1921402683154972673.json、图片生成/图生图/照片转全能图片G-4o卡通人像形象丨一键在线运行_1911405677586149377.json、图片生成/图生图/照片转简洁q版卡通手办-全能图片G-4o同款_1920801534802591746.json、图片生成/文生图/反推提示词+在线生图v1.0_1946032541281251330.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSamplerSelect`
- `LayerUtility: TextJoin`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `DisplayText` —— 3/5 个有
- `CLIPTextEncodeFlux` —— 2/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `ReduxAdvanced` —— 2/5 个有
- `StyleModelLoader` —— 2/5 个有
- `CR Latent Batch Size` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1024 | 4 | 85% |
| 高度 | 1024 | 720 - 1400 | 4 | 77% |
| LoRA 模型强度 | 0.95 | 0.9 - 1 | 4 | 95% |
| LoRA 文本强度 | 0.95 | 0.9 - 1 | 4 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1024，4 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 720 - 1400，4 个样本
- LoRA 模型强度 中位数 0.95，观测区间 0.9 - 1，4 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 0.95，观测区间 0.9 - 1，4 个样本，取值集中（一致性 95%）
