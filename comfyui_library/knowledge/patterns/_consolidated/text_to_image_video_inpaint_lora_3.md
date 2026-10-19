---
name: text_to_image_video_inpaint_lora_3
type: Text To Image
frequency: 3
level: strong
coverage: 0.697333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatch, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, EmptyLatentImage, Florence2Run, Florence2toCoordinates, GetNode, ImageComposite+, ImageConcanate, ImageFromBatch, ImageResizeKJ, ImageToMask, InpaintPreprocessor, JjkText, KSampler, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, PreviewImage, Primitive float [Crystools], Primitive integer [Crystools], PrimitiveString, RHHiddenNodes, RH_Captioner, RH_Translator, Sam2Segmentation, SetNode, SimpleMath+, Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy showAnything, preview_mask, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/区域锁定人物替换｜视频数字人动作迁移生成_2092181873786179585.json, 视频生成/文生视频/区域锁定技术 视频指定位置人物精准替换不掉错_2094820103434100738.json, 视频生成/文生视频/视频「区域锁定」人物替换​文生视频数字人动作迁移_2087322497158049793.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/区域锁定人物替换｜视频数字人动作迁移生成_2092181873786179585.json、视频生成/文生视频/区域锁定技术 视频指定位置人物精准替换不掉错_2094820103434100738.json、视频生成/文生视频/视频「区域锁定」人物替换​文生视频数字人动作迁移_2087322497158049793.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatch`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `EmptyLatentImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetNode`
- `ImageComposite+`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintPreprocessor`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive float [Crystools]`
- `Primitive integer [Crystools]`
- `PrimitiveString`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_Translator`
- `Sam2Segmentation`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy showAnything`
- `preview_mask`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
