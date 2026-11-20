---
name: unknown_workflow_video_lora_sampler_692
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9055
common_nodes: [DrawGaussianNoiseOnImage, DrawMaskOnImage, GetImageSizeAndCount, ImageConcatMulti, ImageRemoveBackground+, ImageResizeKJv2, InvertMask, LoadWanVideoT5TextEncoder, TransparentBGSession+, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUniLumosEmbeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json, 平台全量/一键换视频背景+打光_1996466748704571394.json, 平台全量/一键换视频背景+重新打光，UniLumos模型+ComfyUI！_1988927099337576449.json, 平台全量/重打光-重上色-UniLumos-视频IC-Light_1988123663885049858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_692

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json、平台全量/一键换视频背景+打光_1996466748704571394.json、平台全量/一键换视频背景+重新打光，UniLumos模型+ComfyUI！_1988927099337576449.json、平台全量/重打光-重上色-UniLumos-视频IC-Light_1988123663885049858.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `DrawGaussianNoiseOnImage`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `InvertMask`
- `LoadWanVideoT5TextEncoder`
- `TransparentBGSession+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUniLumosEmbeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `VHS_VideoInfoSource` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
