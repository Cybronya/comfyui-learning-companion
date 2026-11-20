---
name: unknown_workflow_lora_sampler_clip_42
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.976
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EG_TC_Node, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, Int, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/43yijianbatu_2050078089400602626.json, 图片生成/反推提示词/小红书人物多角度多姿势场景一致性_1927579469643681793.json, 图片生成/图生图/F1.极度真实日常生活照小红书超写实生活照3.0_1906155298510540801.json, 图片生成/图生图/人物换背景，多角度多姿势不同服装，小红书风格_1986367612152147969.json, 图片生成/图生图/小红书网感美女 双图融合  模特套图_2037782440806191106.json, 图片生成/图生图/小红书风格-人物换背景，多角度多姿势不同服装_2034538251595292674.json, 图片生成/文生图/人物多角度多姿势场景一致性（一次4张图）_1924977832982999041.json, 图片生成/文生图/小红书高质量美女图 网感美女 轻松涨粉_2034169411594100738.json, 图片生成/文生图/小红书高质量美女图，轻松涨粉_1828492510539993089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/43yijianbatu_2050078089400602626.json、图片生成/反推提示词/小红书人物多角度多姿势场景一致性_1927579469643681793.json、图片生成/图生图/F1.极度真实日常生活照小红书超写实生活照3.0_1906155298510540801.json、图片生成/图生图/人物换背景，多角度多姿势不同服装，小红书风格_1986367612152147969.json、图片生成/图生图/小红书网感美女 双图融合  模特套图_2037782440806191106.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EG_TC_Node`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 8/9 个有
- `CR Text Replace` —— 5/9 个有
- `DisableNoise` —— 5/9 个有
- `Joy_caption_two` —— 5/9 个有
- `Joy_caption_two_load` —— 5/9 个有
- `LayerUtility: PurgeVRAM` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `SplitSigmasDenoise` —— 5/9 个有
- `TextInput_` —— 5/9 个有
- `Fast Bypasser (rgthree)` —— 4/9 个有
- `ImageResize+` —— 4/9 个有
- `LayerMask: BiRefNetUltraV2` —— 4/9 个有
- `LayerMask: LoadBiRefNetModel` —— 4/9 个有
- `LayerUtility: ImageBlendAdvance` —— 4/9 个有
- `TeaCache` —— 4/9 个有
- `ApplyPulidFlux` —— 1/9 个有
- `FloatSlider` —— 1/9 个有
- `PortraitMaster_中文版` —— 1/9 个有
- `PulidFluxEvaClipLoader` —— 1/9 个有
- `PulidFluxInsightFaceLoader` —— 1/9 个有
- `PulidFluxModelLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 9 | 100% |
| 高度 | 512 | 512 - 512 | 9 | 100% |
| LoRA 模型强度 | 0.5 | 0.2 - 0.5 | 9 | 59% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，9 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.2 - 0.5，9 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
