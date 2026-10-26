---
name: unknown_workflow_sampler_unet_vae_210
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9342
common_nodes: [BasicScheduler, CLIPLoader, ColorCorrect, EmptyLatentImage, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/boogu_Edit动漫转写实真人_2077355581987450882.json, 图片生成/图生图/boogu_Edit动漫转写实真人boogu_Anything2RealCharacters_2088253881942888449.json, 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json, 图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json, 图片生成/图生图/boogu_Edit动漫转真人_2078698914928218114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_210

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/boogu_Edit动漫转写实真人_2077355581987450882.json、图片生成/图生图/boogu_Edit动漫转写实真人boogu_Anything2RealCharacters_2088253881942888449.json、图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）_2076639003436208129.json、图片生成/图生图/boogu_Edit动漫转写实真人（boogu_Anything2RealCharacters）反推_2076580842612289538.json、图片生成/图生图/boogu_Edit动漫转真人_2078698914928218114.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ColorCorrect`
- `EmptyLatentImage`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `Text` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
