---
name: image_to_image_lora_sampler_clip_93
type: Image To Image
frequency: 5
level: strong
coverage: 0.9012
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/老妖 - 老照片修复_2002005482082562050.json, 平台全量/老照片修复工作流-Flux Kontext 一键高清_2096574533053542401.json, 平台全量/老照片划痕修复_Flux1 Kontext 底模_2056656950867357697.json, 平台全量/老照片划痕清理终极版+上色_2100236512850964481.json, 平台全量/超好用🔥黑白破旧老照片划痕清理修复终极版_2056626827657048065.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/老妖 - 老照片修复_2002005482082562050.json、平台全量/老照片修复工作流-Flux Kontext 一键高清_2096574533053542401.json、平台全量/老照片划痕修复_Flux1 Kontext 底模_2056656950867357697.json、平台全量/老照片划痕清理终极版+上色_2100236512850964481.json、平台全量/超好用🔥黑白破旧老照片划痕清理修复终极版_2056626827657048065.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 4/5 个有
- `ControlNetLoader` —— 4/5 个有
- `DepthAnythingV2Preprocessor` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `StringConcatenate` —— 4/5 个有
- `DF_Float` —— 3/5 个有
- `DeepTranslatorTextNode` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `easy imageScaleToNormPixels` —— 3/5 个有
- `孤海-浮点滑条` —— 3/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `RH_Translator` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
