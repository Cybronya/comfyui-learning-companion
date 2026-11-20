---
name: unknown_workflow_lora_sampler_clip_44
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.927333
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, MaskToSEGS, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SEGSPreview, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3D Pixar 皮克斯风格头像_1910151890116771841.json, 图片生成/图生图/4格动漫表情包生成 Flux 卡通人物_1921028630795714561.json, 图片生成/图生图/Airbnb 同款 3D 拟物图标_1926835855200260098.json, 图片生成/图生图/【最新】一键生成卡通3D收藏娃娃_1914669593783402497.json, 图片生成/图生图/一键雕琢精致商业图标v1.0_1911401582112768002.json, 图片生成/图生图/上传图片｜一键卡通可爱四宫格漫画_1913221382929379329.json, 图片生成/图生图/全能图片G-4o真人转水晶球摆件V2_1916741073857609730.json, 图片生成/图生图/定制人像专属冰箱贴_2023641529029496833.json, 图片生成/图生图/真人转全能图片G-4o卡通3D盲盒手办套装_1916399661408784386.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/3D Pixar 皮克斯风格头像_1910151890116771841.json、图片生成/图生图/4格动漫表情包生成 Flux 卡通人物_1921028630795714561.json、图片生成/图生图/Airbnb 同款 3D 拟物图标_1926835855200260098.json、图片生成/图生图/【最新】一键生成卡通3D收藏娃娃_1914669593783402497.json、图片生成/图生图/一键雕琢精致商业图标v1.0_1911401582112768002.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `MaskToSEGS`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 8/9 个有
- `LayerUtility: TextJoin` —— 6/9 个有
- `ModelSamplingFlux` —— 6/9 个有
- `SDXLAspectRatioSelector` —— 6/9 个有
- `ConstrainImage|pysssss` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `FluxResolutionNode` —— 3/9 个有
- `JanusImageUnderstanding` —— 3/9 个有
- `JanusModelLoader` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `RH_Captioner` —— 3/9 个有
- `Text _O` —— 3/9 个有
- `TextCombinerTwo` —— 3/9 个有
- `DownloadAndLoadFlorence2Model` —— 2/9 个有
- `ImageUpscaleWithModel` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `UpscaleModelLoader` —— 2/9 个有
- `RH_Prompter` —— 1/9 个有
- `RH_Translator` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 832 | 9 | 96% |
| 高度 | 1216 | 1024 - 1216 | 9 | 92% |
| LoRA 模型强度 | 1 | 0.2 - 1 | 9 | 69% |
| LoRA 文本强度 | 1 | 0.2 - 1 | 9 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 832，9 个样本，取值集中（一致性 96%）
- 高度 中位数 1216，观测区间 1024 - 1216，9 个样本，取值集中（一致性 92%）
- LoRA 模型强度 中位数 1，观测区间 0.2 - 1，9 个样本
- LoRA 文本强度 中位数 1，观测区间 0.2 - 1，9 个样本
