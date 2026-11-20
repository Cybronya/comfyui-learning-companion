---
name: unknown_workflow_video_sampler_vae_137
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84875
common_nodes: [BBoxesToSAM2, DownloadAndLoadQwenModel, GrowMaskWithBlur, ImageBatchToList+, ImageCompositeMasked, ImageConcanate, ImageListToBatch+, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, QwenVLDetection, SolidMask, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json, 平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json, 平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json, 平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_137

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json、平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json、平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json、平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BBoxesToSAM2`
- `DownloadAndLoadQwenModel`
- `GrowMaskWithBlur`
- `ImageBatchToList+`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageListToBatch+`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `QwenVLDetection`
- `SolidMask`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MaskListToMaskBatch` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `preview_mask` —— 2/4 个有
- `Int` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `SaveImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
