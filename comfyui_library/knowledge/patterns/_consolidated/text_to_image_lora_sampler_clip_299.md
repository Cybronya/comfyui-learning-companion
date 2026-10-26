---
name: text_to_image_lora_sampler_clip_299
type: Text To Image
frequency: 7
level: strong
coverage: 0.767143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageFlip+, ImageStitch, KSampler, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片-【批量】提取印花_1977365722563256322.json, 图片生成/图生图/图片-提取印花图案_1977701065699328001.json, 图片生成/图生图/批量提取印花  zip上传印花_图案提取 多用途图片编辑 高清4K放大_2090320942332465153.json, 图片生成/图生图/批量提取印花_1952199748902178817.json, 图片生成/图生图/批量提取印花_zip上传印花_图案提取_多用途图片编辑_高清4K放大_2091706266757455873.json, 图片生成/图生图/批量提取印花_zip上传印花_图案提取_多用途图片编辑_高清4K放大_2091836879619584002.json, 图片生成/图生图/提取印花图案+四方图案生成_1952654604807913474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_299

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图片-【批量】提取印花_1977365722563256322.json、图片生成/图生图/图片-提取印花图案_1977701065699328001.json、图片生成/图生图/批量提取印花  zip上传印花_图案提取 多用途图片编辑 高清4K放大_2090320942332465153.json、图片生成/图生图/批量提取印花_1952199748902178817.json、图片生成/图生图/批量提取印花_zip上传印花_图案提取_多用途图片编辑_高清4K放大_2091706266757455873.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageFlip+`
- `ImageStitch`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 6/7 个有
- `RHBatchImages:` —— 6/7 个有
- `RHExtractImage` —— 6/7 个有
- `RHUploadZip` —— 6/7 个有
- `easy forLoopEnd` —— 6/7 个有
- `easy forLoopStart` —— 6/7 个有
- `easy imageCount` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `CR Seed` —— 5/7 个有
- `ImageResize+` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `easy imageRemBg` —— 4/7 个有
- `easy imageConcat` —— 2/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `MuyeLoadImage` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1504 | 7 | 85% |
| 高度 | 1024 | 1024 - 1504 | 7 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1504，7 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1504，7 个样本，取值集中（一致性 85%）
