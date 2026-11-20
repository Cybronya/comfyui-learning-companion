---
name: image_to_image_sampler_clip_unet_60
type: Image To Image
frequency: 9
level: strong
coverage: 0.913222
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/毛坯房精装_1961470526113910786.json, 平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json, 平台全量/电商服装加模特_Kontext-DEV开源ComfyUI官方版_1938530614842687490.json, 平台全量/精准区域局部修改_Kontext-DEV精准区域编辑_1940156604991885314.json, 平台全量/线稿转写实人物_Kontext-DEV图像编辑_1938965124994490369.json, 平台全量/老照片修复(实用)   增加细节_2036312893628616706.json, 平台全量/老照片修复(实用)_1942747308364902402.json, 平台全量/老照片修复(实用)_1955467234828173314.json, 平台全量/老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/毛坯房精装_1961470526113910786.json、平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json、平台全量/电商服装加模特_Kontext-DEV开源ComfyUI官方版_1938530614842687490.json、平台全量/精准区域局部修改_Kontext-DEV精准区域编辑_1940156604991885314.json、平台全量/线稿转写实人物_Kontext-DEV图像编辑_1938965124994490369.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `LoaderGGUF` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `RepeatLatentBatch` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageAndMaskPreview` —— 1/9 个有
- `InvSRSampler` —— 1/9 个有
- `LoadInvSRModels` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
