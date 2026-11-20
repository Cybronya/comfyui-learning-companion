---
name: image_to_image_sampler_clip_vae_18
type: Image To Image
frequency: 14
level: strong
coverage: 0.906214
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, ShowText|pysssss, Text Multiline, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/简易Kontext Dev （nunchaku加速）_1938911346601680897.json, 图片生成/图生图/超强老照片修复_1985490139109597185.json, 图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json, 图片生成/图生图/青铜雕塑_Kontext-DEV-LORA_1946225600609546241.json, 图片生成/图生图/风格转绘_Kontext-DEV_1938521459012599810.json, 图片生成/图生图/风格迁移_KontextComfyUI官方版_1958049410267623425.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1944993249007427586.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1945760609537290241.json, 平台全量/万能抠图Kontext-DEV开源官方版_1938909180499517442.json, 平台全量/人物换背景产品换背景工作流Kontext-DEV图像编辑抠图换背景_1948179125254139906.json, 平台全量/商业设计_Kontext-DEV开源ComfyUI官方版_1942033564731076609.json, 平台全量/图像局部修改_服装编辑_Kontext-DEV开源ComfyUI官方版_1938508216202649602.json, 平台全量/老照片修复_Kontext-DEV开源ComfyUI官方版_1938497983002664962.json, 平台全量/风格迁移_Kontext-DEV开源ComfyUI官方版_1939829086258634753.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_18

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/简易Kontext Dev （nunchaku加速）_1938911346601680897.json、图片生成/图生图/超强老照片修复_1985490139109597185.json、图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json、图片生成/图生图/青铜雕塑_Kontext-DEV-LORA_1946225600609546241.json、图片生成/图生图/风格转绘_Kontext-DEV_1938521459012599810.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 13/14 个有
- `ImageConcatMulti` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `PreviewImage` —— 12/14 个有
- `GoogleTranslateTextNode` —— 9/14 个有
- `LoaderGGUF` —— 7/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `Image Padding` —— 3/14 个有
- `ImagePadKJ` —— 3/14 个有
- `TeaCache` —— 3/14 个有
- `GoogleTranslator` —— 1/14 个有
- `NunchakuFluxDiTLoader` —— 1/14 个有
- `NunchakuFluxLoraLoader` —— 1/14 个有
- `RH_Captioner` —— 1/14 个有
- `Text Concatenate` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 14 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，14 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
