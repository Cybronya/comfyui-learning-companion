---
name: unknown_workflow_lora_sampler_clip_57
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.936444
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LayerUtility: TextJoin, LoadImage, LoraLoader, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键真人照片转绘泡泡玛特3d风格_1936073081570103298.json, 图片生成/图生图/全能图片G-4o 同款 Q版手办玩偶套装_1912381711098019841.json, 图片生成/图生图/全能图片G4o同款 3D卡通人物玩偶+名字_1921402683154972673.json, 图片生成/图生图/卡通风格人物一键转换_1927654415660892161.json, 图片生成/图生图/照片转简洁q版卡通手办-全能图片G-4o同款_1920801534802591746.json, 图片生成/图生图/生成你的专属Labubu_1935175886897610753.json, 图片生成/图生图/面部迁移 + 人物手办｜全能图片G4o 同款_1920290508118364161.json, 图片生成/文生图/一键真人转3d泡泡玛特风格_1924656165467115521.json, 平台全量/【真人转3D卡通】肖像转动漫可爱人物3D卡通形象 皮克斯_1984514941183016962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/一键真人照片转绘泡泡玛特3d风格_1936073081570103298.json、图片生成/图生图/全能图片G-4o 同款 Q版手办玩偶套装_1912381711098019841.json、图片生成/图生图/全能图片G4o同款 3D卡通人物玩偶+名字_1921402683154972673.json、图片生成/图生图/卡通风格人物一键转换_1927654415660892161.json、图片生成/图生图/照片转简洁q版卡通手办-全能图片G-4o同款_1920801534802591746.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two_advanced` —— 8/9 个有
- `Joy_caption_two_load` —— 8/9 个有
- `Joy_extra_options` —— 8/9 个有
- `TextInput_` —— 8/9 个有
- `ApplyPulidFlux` —— 6/9 个有
- `ApplyTeaCachePatch` —— 6/9 个有
- `PulidFluxInsightFaceLoader` —— 6/9 个有
- `PulidFluxModelLoader` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `EcomIDEvaClipLoader` —— 4/9 个有
- `PulidFluxEvaClipLoader` —— 2/9 个有
- `easy imageScaleDownToSize` —— 2/9 个有
- `DeepTranslatorTextNode` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `LP-TranslateToEN` —— 1/9 个有
- `Miaoshouai_Tagger` —— 1/9 个有
- `RepeatLatentBatch` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 9 | 87% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1.5 | 9 | 80% |
| LoRA 文本强度 | 1 | 0.8 - 1.5 | 9 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，9 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1.5，9 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1.5，9 个样本，取值集中（一致性 80%）
