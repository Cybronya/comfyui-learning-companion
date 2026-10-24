---
name: unknown_workflow_sampler_unet_vae_13
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.956905
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/F.1+流浪汉_1945170907587596289.json, 图片生成/文生图/F.1+皮克斯_1946922717151158273.json, 图片生成/文生图/F.1+纪实摄影_1938572723696099330.json, 图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json, 图片生成/文生图/F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json, 图片生成/文生图/F.1-文生图+LORA_2041721521340682242.json, 图片生成/文生图/F.1生图工作流加速版_2054191053686747138.json, 图片生成/文生图/FLIX文生图｜产品写实 超逼真_1896248747091427329.json, 图片生成/文生图/FLUX+LORA一键生成可爱卡通形象_1948753188301221890.json, 图片生成/文生图/FLUX插画动物_1904908786933633026.json, 图片生成/文生图/FLUX毛绒数字_1904904736871469057.json, 图片生成/文生图/FLUX磨砂玻璃图标_1904907559919357954.json, 图片生成/文生图/FLUX膨胀气球字母_1904906707053776898.json, 图片生成/文生图/Flux-DEV-Schnell文生图工作流_1942877686643798017.json, 图片生成/文生图/Flux-lora快速出图_1920279185280143362.json, 图片生成/文生图/Flux1微胖性感美女生成大胸美女图123_2002414890683908097.json, 图片生成/文生图/Flux文生图-中文提示词_2078378003817656321.json, 图片生成/文生图/【FLUX】IP设计三视图_1904909104412807170.json, 图片生成/文生图/一键生成古装表情包丨角色一致性_1915288629995048961.json, 图片生成/文生图/微胖性感美女生成+大胸美女-抖音、小红书美女写真_2039975468539060225.json, 图片生成/文生图/微胖性感美女生成+大胸美女-抖音、小红书美女写真_2040333322827599873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/F.1+流浪汉_1945170907587596289.json、图片生成/文生图/F.1+皮克斯_1946922717151158273.json、图片生成/文生图/F.1+纪实摄影_1938572723696099330.json、图片生成/文生图/F.1-FLUX文生图工作流+LORA（一键运行）_1911723649815015426.json、图片生成/文生图/F.1-FLUX文生图工作流（一键运行）(双LORA)_1915296194967306242.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 16/21 个有
- `LoraLoaderModelOnly` —— 13/21 个有
- `LoraLoader` —— 8/21 个有
- `TextInput_` —— 6/21 个有
- `CLIPTextEncode` —— 5/21 个有
- `Int` —— 5/21 个有
- `RH_Translator` —— 4/21 个有
- `SeargePromptCombiner` —— 4/21 个有
- `JjkText` —— 3/21 个有
- `ChinesePrompt_Mix` —— 1/21 个有
- `FluxGuidance` —— 1/21 个有
- `RescaleCFG` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1536 | 21 | 76% |
| 高度 | 1024 | 512 - 1960 | 21 | 68% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 8 | 83% |
| LoRA 文本强度 | 1 | 0 - 1 | 8 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1536，21 个样本
- 高度 中位数 1024，观测区间 512 - 1960，21 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，8 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 0 - 1，8 个样本
