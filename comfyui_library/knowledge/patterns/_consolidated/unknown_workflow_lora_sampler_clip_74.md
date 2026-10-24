---
name: unknown_workflow_lora_sampler_clip_74
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.684
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxDeGuidance, FluxKontextImageScale, ImageConcanate, KSamplerSelect, LayerUtility: ImageMaskScaleAs, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, RandomNoise, ReferenceLatent, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, TextBox, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/13种提示词预设 _ Kontext Presets_1944364168247955457.json, 图片生成/图生图/Kontext Presets 官方预设提示｜提高生图_1947832362266673154.json, 图片生成/图生图/Kontext Presets 官方预设词模版 高效生图_1947214222984945665.json, 图片生成/图生图/Kontext Presets_12种提示词预设_1944911580158156801.json, 图片生成/图生图/Kontext Presets_12种提示词预设_1948205498127527937.json, 图片生成/图生图/单图编辑基础流 _ 双截棍+kontext （速度极快）_1939493492726931458.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/13种提示词预设 _ Kontext Presets_1944364168247955457.json、图片生成/图生图/Kontext Presets 官方预设提示｜提高生图_1947832362266673154.json、图片生成/图生图/Kontext Presets 官方预设词模版 高效生图_1947214222984945665.json、图片生成/图生图/Kontext Presets_12种提示词预设_1944911580158156801.json、图片生成/图生图/Kontext Presets_12种提示词预设_1948205498127527937.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxDeGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `KSamplerSelect`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoaderV2`
- `RandomNoise`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextBox`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 5/6 个有
- `CR Text Replace` —— 5/6 个有
- `GoogleTranslateTextNode` —— 5/6 个有
- `LoadKontextPresets` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `BiRefNet_Hugo` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `Int` —— 4/6 个有
- `LayerMask: RmBgUltra V2` —— 4/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ImpactSwitch` —— 2/6 个有
- `PrimitiveString` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
