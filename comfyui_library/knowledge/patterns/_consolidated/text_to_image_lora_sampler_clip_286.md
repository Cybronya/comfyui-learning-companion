---
name: text_to_image_lora_sampler_clip_286
type: Text To Image
frequency: 7
level: strong
coverage: 0.878714
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, INTConstant, JWStringConcat, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-Klein超强分镜流｜九宫格角色一致性连贯分镜_2097192009663602689.json, 图片生成/图生图/FLUX-Klein超强分镜流｜角色一致性九宫格连贯分镜图生成_2097111527869472770.json, 图片生成/图生图/FLUX2-Klein人物一致性分镜器｜漫剧短剧角色出图_2098725733140090881.json, 图片生成/图生图/FLUX2-Klein人物一致性分镜生成器｜漫剧短剧角色分镜 图生图_2104069316864991234.json, 图片生成/图生图/一致性分镜出图｜FLUX2-Klein图生图角色统一_2093737437481750529.json, 图片生成/图生图/一致性分镜出图｜FLUX2-Klein角色图生图生成_2093413201122775041.json, 图片生成/图生图/影视剧情分镜延展｜FLUX.2.0-Klein9B 灵感工具_2089302498279510018.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_286

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX-Klein超强分镜流｜九宫格角色一致性连贯分镜_2097192009663602689.json、图片生成/图生图/FLUX-Klein超强分镜流｜角色一致性九宫格连贯分镜图生成_2097111527869472770.json、图片生成/图生图/FLUX2-Klein人物一致性分镜器｜漫剧短剧角色出图_2098725733140090881.json、图片生成/图生图/FLUX2-Klein人物一致性分镜生成器｜漫剧短剧角色分镜 图生图_2104069316864991234.json、图片生成/图生图/一致性分镜出图｜FLUX2-Klein图生图角色统一_2093737437481750529.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `INTConstant`
- `JWStringConcat`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `Florence2Run` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `InpaintModelConditioning` —— 2/7 个有
- `LayerMask: MaskPreview` —— 2/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
